from lib.fonctions import *


def effacer_ecran() -> None:
    print("\033[H\033[J")

def printer_intro():
    print(""" _     _ _     _ _       _   _      __                                 
| |__ (_) |__ | (_) ___ | |_| |__   \\_\\  __ _ _   _  ___   _ __  _   _ 
| '_ \\| | '_ \\| | |/ _ \\| __| '_ \\ / _ \\/ _` | | | |/ _ \\ | '_ \\| | | |
| |_) | | |_) | | | (_) | |_| | | |  __/ (_| | |_| |  __/_| |_) | |_| |
|_.__/|_|_.__/|_|_|\\___/ \\__|_| |_|\\___|\\__, |\\__,_|\\___(_) .__/ \\__, |
                                           |_|            |_|    |___/ 
    """)
    print("Un logiciel de gestion de bibliothèque sérieux pour les gens sérieux")
    print("made with ❤  by yoyo\n")

def menu_helper_choisir(L:list):
    choix = 0
    print("\033[s", end="") # sauvegarder la position du curseur, pour que on reste au même endroit si on fait une erreur d'input
    # ^^^ vient de là   https://github.com/dylanaraps/pure-sh-bible?tab=readme-ov-file#cursor-movement
    while choix not in L:
        choix = input("--> ")
        try:
            choix = int(choix)
        except ValueError:
            choix = 0
        print("\033[u", end="") # restorer la position du curseur (qui a été sauvegardé avant avec le 033 s)
        print("\033[J", end="") # on efface la ligne actuelle sinon l'entrée d'avant reste...
    return choix

def main_menu() -> None:
    effacer_ecran()
    printer_intro()
    print("""
      +----------------------------------------+
      |                                        |
      |      1. Rechercher dans la DB >>>      |
      |      2. Insérer dans la DB >>>         |
      |      3. Mettre à jour la DB >>>        |
      |      4. Supprimer dans la DB >>>       |
      |      5. Terminer [x]                   |
      |                                        |
      +----------------------------------------+
    """)
    entrer_menu = menu_helper_choisir([1,2,3,4,5])
    if entrer_menu != 5:
        entrer_fonction = f"submenu_{entrer_menu}()"
        eval(entrer_fonction)
    print(">>> Au revoir ! 👋 <<<")

def submenu_1() -> None: # Rechercher dans la DB
    effacer_ecran()
    printer_intro()
    print("""
      +---------------------------------------------------------------+
      |                                                               |
      |    1. Rechercher les livres empruntés par une personne >>>    |
      |    2. Rechercher un livre emprunté par ISBN >>>               |
      |    3. Afficher les personnes en retard >>>                    |
      |    4. Rechercher par mot clé >>>                              |
      |    5. Retour [x]                                              |
      |                                                               |
      +---------------------------------------------------------------+
""")
    entrer_menu = menu_helper_choisir([1,2,3,4,5])
    if entrer_menu != 5:
        fonctions = ["recherche_emprunt_personne()", "recherche_isbn()", "afficher_retards()", "recherche_mot_cle()"]
        eval(fonctions[entrer_menu-1])
        submenu_1()
    else:
        main_menu()

def submenu_2() -> None: # Insérer dans le DB
    effacer_ecran()
    printer_intro()
    print("""
      +---------------------------------+
      |                                 |
      |    1. Nouvel usager >>>         |
      |    2. Nouveau livre >>>         |
      |    3. Emprunter un livre >>>    |
      |    4. Retour [x]                |
      |                                 |
      +---------------------------------+
""")
    entrer_menu = menu_helper_choisir([1,2,3,4])
    if entrer_menu != 4:
        fonctions = ["new_usager()", "new_livre()", "new_emprunt()"]
        eval(fonctions[entrer_menu - 1])
        submenu_2()
    else:
        main_menu()

def submenu_3() -> None: # Mettre a jour DB
    effacer_ecran()
    printer_intro()
    print("""
      +-----------------------------------------------+
      |                                               |
      |    1. Changer une date de retour >>>          |
      |    2. Modifier les données d'un usager >>>    |
      |    3. Retour [x]                              |
      |                                               |
      +-----------------------------------------------+
""")
    entrer_menu = menu_helper_choisir([1,2,3])
    if entrer_menu != 3:
        fonctions = ["ch_date_retour_livre()", "submenu_3_menu_usager()"]
        eval(fonctions[entrer_menu - 1])
        submenu_3()
    else:
        main_menu()

def submenu_3_menu_usager() -> None:
    # Frontend pour la fonction "ch_usager(donnée:str)" (prend en compte des strs comme "prenom", "nom", "cp", "ville", "email") 
    effacer_ecran()
    printer_intro()
    print("""
      +--------------------------------------+
      |                                      |
      |    1. Modifier un nom >>>            |
      |    2. Modifier un prénom >>>         |
      |    3. Modifier une adresse >>>       |
      |    4. Modifier un code postal >>>    |
      |    5. Modifier une ville >>>         |
      |    6. Modifier un e-mail >>>         |
      |    7. Retour [x]                     |
      |                                      |
      +--------------------------------------+
""")
    entrer_menu = menu_helper_choisir([1,2,3,4,5,6,7])
    if entrer_menu != 7:
        donnees_a_modif = ["nom","prenom","adresse","cp","ville","email"]
        eval(f"ch_usager('{donnees_a_modif[entrer_menu - 1]}')")
        submenu_3_menu_usager()
    else:
        submenu_3()

def submenu_4() -> None: # Supprimer de la DB
    effacer_ecran()
    printer_intro()
    print("""
      +-----------------------------------+
      |                                   |
      |    1. Supprimer un livre >>>      |
      |    2. Supprimer un emprunt >>>    |
      |    3. Supprimer un usager >>>     |
      |    4. Retour [x]                  |
      |                                   |
      +-----------------------------------+
""")
    entrer_menu = menu_helper_choisir([1,2,3,4])
    if entrer_menu != 4:
        fonctions = ["delete_livre()", "delete_emprunt()", "delete_usager()"]
        eval(fonctions[entrer_menu - 1])
        submenu_4()
    else:
        main_menu()


