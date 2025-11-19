#!/bin/python3
# ^^^ pratique pour pouvoir lancer sur linux './bibliothèque.py' (faut juste pas oublier le chmod +x)

import os
import sqlite3 as sgbd
import random as r
# import qrcode
import lib.menu as menu # local, voir ./lib/menu.py
from lib.fonctions import * # local, voir ./lib/fonctions.py

### debut du programme principal

if(not(os.path.exists("biblio.db"))):
    print("""
\033[1;31m!!! La base de donnée n'existe pas !!!\033[0m

\033[1mPour créer la base de données, executez la commande:\033[0m

    python3 scripts/make_db.py
""")
    exit(1)
# connecter sqlite a la DB et connecter un curseur
connexion = sgbd.connect("biblio.db")
curseur = connexion.cursor()

mettre_connexion(connexion) # Voir lib/fonctions.py
mettre_curseur(curseur)

try:
    menu.main_menu()
except KeyboardInterrupt:
    print(">>> Au revoir ! 👋 <<<")

connexion.close()
