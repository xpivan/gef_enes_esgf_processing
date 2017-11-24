#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages, Command

import os

# Ceci n'est qu'un appel de fonction. Mais il est treeeeeeeeeees long
# et il comporte beaucoup de parametres
setup(
 
    # le nom de votre bibliotheque, tel qu'il apparaitre sur pypi
    name='eudat_gef_enes_processing',
 
    # Liste les packages a inserer dans la distribution
    # plutot que de le faire a la main, on utilise la foncton
    # find_packages() de setuptools qui va cherche tous les packages
    # python recursivement dans le dossier courant.
    # C'est pour cette raison que l'on a tout mis dans un seul dossier:
    # on peut ainsi utiliser cette fonction facilement
    packages=find_packages(),
 
    # votre pti nom
    author="Christian P.",
 
    # Votre email, sachant qu'il sera publique visible, avec tous les risques
    # que ca implique.
    author_email="christian.page@cerfacs.fr",
 
    # Une description courte
    description="Python execution of EUDAT GEF calling ESGF CWT and using icclim Use Case",
 
    # Une description longue, sera affichee pour presenter la lib
    # Generalement on dump le README ici
    long_description=open('README.md').read(),
 
    # Vous pouvez rajouter une liste de dependances pour votre lib
    # et meme preciser une version. A l'installation, Python essayera de
    # les telecharger et les installer.
    #
    # Ex: ["gunicorn", "docutils >= 0.3", "lxml==0.5a7"]
    #
    # Dans notre cas on en a pas besoin, donc je le commente, mais je le
    # laisse pour que vous sachiez que ca existe car c'est tres utile.
    # install_requires= ,
 
    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,
 
    # Une url qui pointe vers la page officielle de votre lib
    url='https://github.com/cerfacs-globc/eudat_gef_enes_processing',
 
)
