#!/bin/python3
# ^^^ pratique pour pouvoir lancer sur linux './bibliothèque.py' (faut juste pas oublier le chmod +x)

import sqlite3 as sgbd
import random as r
# import qrcode
import lib.menu as menu # local, voir ./lib/menu.py
from lib.fonctions import * # local, voir ./lib/fonctions.py


### debut du programme principal
# connecter sqlite a la DB et connecter un curseur
connexion = sgbd.connect("biblio.db")
curseur = connexion.cursor()

mettre_connexion(connexion) # Voir lib/fonctions.py
mettre_curseur(curseur)

menu.main_menu()
connexion.close()
