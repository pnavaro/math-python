import numpy as np

with open('data/IRMAR-2017-2018.txt') as f:
    data = f.readlines()

org_catalog = ['AGRO', 'INSA', 'R1', 'R2', 'INRIA', 'EXT', 'ENS']
pos_catalog = ['PR', 'CR', 'DOC', 'MC', 'DR', 'MC-HDR', 'CR-HDR', 'PE',
               'PDOC', 'ADMG', 'TC', 'IR', 'IE', 'AI', 'AGPREP', 'ATER,DOC',
               'ADMG', 'ADM-UFR', 'PRAG', 'CH', 'ADMP', 'CH-HDR', 'ATER', 'LOG']


names, phones, offices, orgs, positions, teams = [], [], [], [], [], []
for m, line in enumerate(data):

    member = line.strip()
    i = member.index('+')
    name = member[:i]
    names.append(name)
    phones.append(member[i:i+17])
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
dtype={'names': ['name', 'phone', 'office', 'organization', 'position', 'team'],
       'formats': ['U30', 'U17', 'U7', 'U5', 'U6', 'U9,U9']})

irmar['name'] = names
irmar['phone'] = phones
irmar['office'] = offices
irmar['organization'] = orgs
irmar['position'] = positions
irmar['team'] = teams


