#!/usr/bin/python3

import os
import sqlite3 as sgbd

def cleanup_backslash_n(s:str):
    res = ""
    for c in s:
        if c != '\n':
            res += c
    return res

def print_status(type:str, s:str):
    couleur = 0
    if(type == "warning"):
        couleur = 33
    elif(type == "error"):
        couleur = 31
    elif(type == "success"):
        couleur = 32
    elif(type == "note"):
        couleur = 34
    print(f"\033[1;{couleur}m{s}\033[0m")

# On vérifie qu'on est bien dans le dossier racine et pas dans scripts/
if(os.path.exists("make_db.sql") and not(os.path.exists("bibliothèque.py"))):
    print_status("error", "Il faut être dans le dossier racine, pas dans le dossier scripts.")
    exit(1)

# Si la DB existe déjà on met une alerte
if(os.path.exists("biblio.db")):
    print_status("warning", "La base de donnée existe déjà! Si vous continuez, vous écraserez l'ancienne base de donnée bibliothèque. Continuer?")
    choix_ecraser_db = input("[y/n]? --> ")
    if(choix_ecraser_db not in ['y','Y']):
        print_status("success", "=> D'accord, on annule tout")
        exit(1)
else:
    print_status("note", "La DB n'existe pas.")

print("""
quelle base de donnée voulez vous initialiser?
1. Base de donnée vide pour la production (recommandé) >>>
2. Base de donnée avec des exemples (pour tester le logiciel) >>>

* si vous ne savez pas, tapez '1'
""")

choix_type_db = int(input("--> "))
if(choix_type_db not in [1,2]):
    print_status("error", "1 ou 2 !!!")
    exit(1)

# On ouvre créé la DB
connex = sgbd.connect("biblio.db")
c = connex.cursor()

# volé gracieusement de https://stackoverflow.com/questions/19472922/reading-external-sql-script-in-python
if(choix_type_db == 1):
    fd = open('scripts/script_make_db_mini.sql')
elif(choix_type_db == 2):
    fd = open('scripts/script_make_db_exemples.sql')

script_sql = fd.read()
fd.close()

commandes_sql = cleanup_backslash_n(script_sql).split(';')

for cmd in commandes_sql:
    try:
        c.execute(cmd)
    except sgbd.OperationalError as msg:
        print_status("error", f"""
!!! La commande suivante !!!

{cmd}

!!! A échouée avec l'erreur !!!

{msg}
""")

connex.commit()
connex.close()
