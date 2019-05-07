# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import numpy as np

with open('../data/IRMAR-2017-2018.txt') as f:
    data = f.readlines()

org_catalog = ['AGRO', 'INSA', 'R1', 'R2', 'INRIA', 'EXT', 'ENS', 'CNRS']
pos_catalog = ['PR', 'CR', 'DOC', 'MC', 'DR', 'MC-HDR', 'CR-HDR', 'PE',
               'PDOC', 'ADMG', 'TC', 'IR', 'IE', 'AI', 'AGPREP', 'ATER,DOC',
               'ADMG', 'ADM-UFR', 'PRAG', 'CH', 'ADMP', 'CH-HDR', 'ATER', 'LOG']

names, phones, offices, orgs, positions, teams = [], [], [], [], [], []
for m, line in enumerate(data):

    member = line.strip()
    i = member.index('+')
    name = member[:i]
    names.append(name)
    phones.append(member[i:i+17].replace(' ',''))
    remind = member[i+17:].split()
    office = 'NA'
    organization = 'R1'
    team = ['NA']

    # office
    if remind[0].isdigit() or '/' in remind[0]:
        offices.append(remind[0])
        office = remind[0]
        remind.pop(0)
    else:
        offices.append('NA')

    # organization
    if len(remind) > 0 and remind[0] in org_catalog:
        orgs.append(remind[0])
        organization = remind[0]
        remind.pop(0)
    else:
        orgs.append('R1')

    # position
    if len(remind) > 0 and remind[0] in pos_catalog:
        positions.append(remind[0])
        position = remind[0]
        remind.pop(0)
    else:
        position = 'NA'
        positions.append('NA')

    # team
    if len(remind) > 0:
        team = remind[-1].split(',')
        if len(team) == 2:
            teams.append(tuple(team))
        else:
            teams.append(tuple(team+['NA']))
    else:
        teams.append(('ADM','NA'))

irmar = np.zeros(len(data),
dtype={'names': ['name', 'phone', 'office', 'organization', 'position', 'hdr', 'team1', 'team2'],
       'formats': ['U30', 'U17', 'U7', 'U5', 'U6', '?', 'U9', 'U9']})

# %%
irmar['name'] = names
irmar['phone'] = phones
irmar['office'] = offices
irmar['organization'] = orgs

def _hdr(position):
    return any(x in position for x in ['HDR','PR','DR','PE'])
    
irmar['hdr'] = [ _hdr(position) for position in positions]
irmar['position'] = [position.replace('-HDR','') for position in positions]
irmar['team1'] = [team[0] for team in teams]
irmar['team2'] = [team[1] for team in teams]

# %%
import pandas as pd
df = pd.DataFrame(irmar)
df['position'] = df.position.astype('category')
df['team1'] = df.team1.astype('category')
df['team2'] = df.team2.astype('category')
df['organization'] = df.organization.astype('category')
df['hdr'] = df.hdr.astype('bool')

# %%
import json
with open("irmar.json","w") as f:
    json.dump(df.to_json(orient="records"),f)

# %%
df.to_csv("irmar.txt",sep="\t")

# %%
df

# %% [markdown]
# - Combien d'enseignants-chercheurs habilités à diriger des recherches ?

# %%
len(df[df.hdr])

# %% [markdown]
# - Combien d'enseignants-chercheurs de Rennes 2 ?

# %%
len(df[df.organization == 'R2'])

# %%
df.loc[df['name'].str.contains("Guevel")]

# %% [markdown]
# - Liste des MC de l'équipe STATS

# %%
df.loc[df.position == 'MC'].loc[(df.team1 == 'STAT') | (df.team2 == 'STAT')]

# %% [markdown]
# - Pourcentage d'EC non doctorants habilités

# %%
df.loc[df.position != 'DOC'].hdr.sum()/df.loc[df.position != 'DOC'].hdr.count()*100

# %%
res = pd.DataFrame()
for position in ['DOC','PR','MC','CR','DR']:
    res[position] = df.loc[df.position == position].groupby('team1').name.count()

# %%
res = res.drop(['INFO','IREM','BIBLI','ADM'])

# %%
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10,6)

# %%
res.sum().plot.pie(figsize=(8, 8))

# %%
res.sum(axis=1).plot.pie(figsize=(8, 8))

# %% [markdown]
# - Nombre de maitres de conférence

# %%
df['name'].loc[df.position == 'MC'].count()

# %%

# %%
