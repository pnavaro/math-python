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
#     display_name: Python (math-python)
#     language: python
#     name: math-python
# ---

# %% [markdown]
# # GeoGebra Day data
#
# - Example of cleaning data with pandas
# - csv `data/geogebra.csv` file is exported from LimeSurvey 

# %%
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt

# %%
plt.rcParams['figure.figsize'] = (10,6)
import pandas as pd

# %%
geogebra = pd.read_csv('../data/geogebra.csv', sep=';')
geogebra.head()

# %% [markdown]
# ### Remove all rows where "Prenom - Nom" is Nan

# %%
geogebra = geogebra.dropna(subset=['Prénom - Nom'])
geogebra.head()

# %% [markdown]
# ### Remove some unuseful variables

# %%
geogebra.columns

# %%
geogebra = geogebra.drop(geogebra.columns[0:5], axis=1)

# %%
geogebra = geogebra.reset_index(drop=True)

# %%
geogebra.head()

# %% [markdown]
# ### Replace Nan by 'Non' and count Lunch participants

# %%
geogebra.iloc[:,4] = geogebra.iloc[:,4].fillna('Non')
geogebra.head()

# %%
import numpy as np
len(list(filter(lambda x:x=='Oui',geogebra.iloc[:,4].values)))

# %%
geogebra.iloc[:,4].value_counts()

# %%
lunch_participants = geogebra[geogebra.iloc[:,4] == 'Oui'].iloc[:,0].values
for people in sorted(lunch_participants):
    print(people)

# %%
nolunch_participants = geogebra[geogebra.iloc[:,4] == 'Non'].iloc[:,0].values
for person in nolunch_participants:
    print(person)

# %% [markdown]
# ### GeoGebra participants level

# %%
plt.figure(figsize=(6,6))
geogebra.iloc[:,5] = geogebra.iloc[:,5].astype(int) # convert to int
ax = geogebra.iloc[:,5].value_counts().plot(kind='pie');
ax.set_title("GeoGebra level 1-5")
ax.set_ylabel("");

# %% [markdown]
# ### Participants institution

# %%
geogebra.iloc[:,2].value_counts()

# %%
for people in geogebra[geogebra.iloc[:,2] == "Enseignant du second degré"].iloc[:,0].values:
    print(people)

# %% [markdown]
# ### display participants remarks

# %%
remarks = geogebra.iloc[:,6]
remarks = remarks.dropna()

# %%
with open('remarks.md','w') as f:
    for i, line in enumerate(remarks.values):
        line = line.strip().replace("\n","")
        f.write(str(i)+'. '+line+'\n')

# %% [markdown]
# 0. Fabriquer des animations, faire de la programmation avec GeoGebra...
# 1. En savoir plus !
# 2. geom espace term S et surfaces z = f(x,y)
# 3. Je ne pourrai pas être présente le matin, j'arriverai vers 13 h 30.
# 4. J'utilise GeoGebra pour mes préparations de cours et aussi avec les élèves. Je pense avoir des utilisations très basiques de GeoGebra et j'espère pouvoir découvrir davantage ses possibilités.
# 5. Utiliser le tableur, faire des  calculs formels, et des figures dans l'espace.
# 6. Je souhaiterai voir différentes utilisations de GeoGebra pour les fonctions, les listes ( suites définies par récurrence : représentation graphique par exemple...)
# 7. Pas d'attentes particulières. J'aime bien ce logiciel, mais je pense que je n'utilise que très peu de fonctionnalités....Je voudrais découvrir des nouvelles fonctions et des nouvelles idées pour enrichir mon utilisation en classe (lycée)Par ailleurs, je prépare l'agrégation interne de maths. Pour les épreuves orales, le jury apprécie que les candidats illustrent leurs leçons par des animations logicielles (géogébra, python, scilab, xcas....). Plus je connaitrais Géogébra, et plus j'aurais des idées pour illustrer mes leçons d'oral. Voilà une deuxième motivation pour venir à cette journée.
# 8. Acquisitions de nouvelles méthodes éventuellement rapides
# 9. Les applications de Géogébra pour concevoir les cours, et les activités.
# 10. Connaitre plus les fonctions de calcul formel, de probabilités et de 3D
# 11. Utiliser Géogébra pour la géométrie dans l'espace.
# 12. Géométrie dans l'espace.
# 13. Utilisation de Géogébra en première et terminale.
# 14. Travailler sur la géométrie dans l’espace.
# 15. Étudier ce que l on peut faire d un point de vue pédagogique avec les élèves pour conjecturer/démontrer . Travailler avec des commandes cachées.  Apprendre à utiliser le curseur. Mieux connaître l outil geogebra pour l utiliser dzns la création de mes cours.
# 16. Me sentir plus à l’aise lorsque je propose une activité geogebra aux élèves.
# 17. Yes
# 18. Utilisation des outils "avancés" : calcul formel, tableur Lien entre ces outils "avancés"Possibilité (ou non) d'exploiter une figure geogebra dans une page HTML en tant qu'applet (ce qui était possible dans les anciennes versions en .jar) sans être forcé de l'héberger sur GeogebraTubeSi oui : quelle interaction avec les paramètres prédéfinis ?
# 19. Voir toutes les fonctionnalités de Géogebra pour faire des animations en classe ou pour utiliser avec les élèves. ( Lycee)
# 20. Insérer des images.Créer des animations.Géogébra 3D
# 21. Géométrie dans l'espace nivea
#
