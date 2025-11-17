import random as r
import sqlite3 as sgbd
import datetime as dt

### Fonctions utiles

# On est obligé de faire ça plus la fonction car sinon python va dire que curseur est undefined
curseur = None
def mettre_curseur(c) -> None:
    global curseur
    curseur = c

# de même pour la connexion
connexion = None
def mettre_connexion(cnx) -> None:
    global connexion
    connexion = cnx


def pause() -> None:
    input("\n>>> Appuyez sur entrer pour continuer... <<<")

# def affiche_res_requete(message:str, liste_resultat:list):
#     print(f"""[✅]
#  | 
#  | Requête exécutée avec succès. {len(liste_resultat)} résultat trouvés.
#  | {message} :
#  | """)
#     for i in range(0,len(liste_resultat)):
#         print(f" |--- {i+1}. {liste_resultat[i]}")

def make_code_barre() -> str:
    """
    Donne un code barre aléatoire
    """
    # en soit, notre code barre est juste un nombre à 15 chiffres (par contre faut s'assurer d'avoir des zéros jusqu'au bout, d'ou le délire avec les f-strings)

    code_barre_valide = False
    while not code_barre_valide:
        code_barre = f"{r.randint(0, int(999999999999999)):015d}" # extrêmement moche, mais compact et ça marche
        # on vérifie si le code barre n'existe pas déjà
        curseur.execute("""
        SELECT code_barre FROM USAGER
        WHERE code_barre=?""", [code_barre])
        if(len(curseur.fetchall()) == 0):
            code_barre_valide = True
    return code_barre

def faire_qr_code(nom:str, prenom:str, code_barre:int) -> None:
    pass
    # print(f"Nouveau qr code pour {nom} {prenom} sauvegardé dans le dossier 'output/qr_codes/'")

def date_du_jour() -> str:
    return str(dt.datetime.now()).split(" ")[0]

### Submenu 1
def recherche_emprunt_personne() -> None:
    codebarre = input("code barre? --> ")
    curseur.execute("""SELECT titre, editeur, annee, isbn FROM LIVRE
WHERE isbn=(
    SELECT isbn from EMPRUNT
    WHERE code_barre = ?
)""", [codebarre])

    liste_res = curseur.fetchall()
    if len(liste_res) > 0:
        print(f"[✅] La personne ayant le code barre {codebarre} a emprunté {len(liste_res)} livres. Les voici:")
        for livre in liste_res:
            print(livre)
    else:
        print(f"[❌] La personne ayant le code barre {codebarre} n'a emprunté AUCUN livre... Peut-être serait-il temps ?")

    pause()

def recherche_isbn() -> None: 
    isbn = input("isbn? --> ")

    curseur.execute("""
        SELECT nom,prenom,code_barre FROM USAGER
        WHERE code_barre = (
        	SELECT code_barre FROM EMPRUNT
        	WHERE isbn=?
        )""",
        [isbn]
    )
    personne = curseur.fetchall()
    if(len(personne) >= 1):
        personne = personne[0] # une seule personne peut emprunter !!!

    curseur.execute("""
        SELECT retour FROM EMPRUNT
        WHERE isbn=?
        """,
        [isbn]
    )
    date_retour = curseur.fetchall()

    if(len(personne) >= 1):
        print(f"[✅] Le livre d'ISBN {isbn} a été emprunté.")
        print("")
        print("[📄] EMPRUNT")
        print(f"| Date de retour: {date_retour}")
        print("| Au nom de:")
        print("|   [🧑] USAGER")
        print(f"|   | Prénom, Nom: {personne[1]} {personne[0]}")
        print(f"|   | Code barre: {personne[2]}")
        print("")
    else:
        print(f"[❌] Le livre d'ISBN {isbn} n'a pas été emprunté par une seule personne...")
    
    pause()

def afficher_retards() -> None:
    curseur.execute("""
        SELECT USAGER.code_barre, isbn, retour, nom, prenom FROM
        EMPRUNT JOIN USAGER ON EMPRUNT.code_barre = USAGER.code_barre
        WHERE retour < ?
        """, [date_du_jour()]
    )
    liste_res = curseur.fetchall()

    print(f"[ℹ️] Nous sommes le {date_du_jour()}.")
    if len(liste_res) > 0:
        print(f"[‼️] {len(liste_res)} emprunts n'ont pas étés rendus! Les voici:")
        print("")
        for emprunt in liste_res:
            print("[📄] EMPRUNT (en retard)")
            print(f"| ISBN: {emprunt[1]}")
            print(f"| Date de retour: {emprunt[2]}")
            print("| Au nom de:")
            print("|   [🧑] USAGER")
            print(f"|   | Prénom, Nom: {emprunt[4]} {emprunt[3]}")
            print(f"|   | Code barre: {emprunt[0]}")
            print("")
    else:
        print("[🥳] Aucune personne n'est en retard! Génial!")

    pause()

def recherche_mot_cle() -> None:
    recherche = input("mot clé ? --> ")
    # ATTENTION CA FAIT MAL AUX YEUX!!!
    curseur.execute("""
        SELECT titre, AUTEUR.prenom,AUTEUR.nom, editeur,annee, LIVRE.isbn
        FROM LIVRE JOIN ( 
        	AUTEUR_DE JOIN AUTEUR
        	ON AUTEUR_DE.id_auteur = AUTEUR.id_auteur
        ) ON LIVRE.isbn = AUTEUR_DE.isbn
        WHERE titre LIKE ?""",
        [f"%{recherche}%"]
    )
    liste_res = curseur.fetchall()
    if len(liste_res) > 0:
        print(f"[✅] {len(liste_res)} livres trouvés ayant le mot \"{recherche}\"")
        print("")
        for livre in liste_res:
            print("[📕] LIVRE")
            print(f"| Titre: {livre[0]}")
            print(f"| Auteur: {livre[1]} {livre[2]}")
            print(f"| Editeur: {livre[3]}")
            print(f"| Annee: {livre[4]}")
            print(f"| ISBN: {livre[5]}")
            print("")
    else:
        print(f"[❌] Aucun livre trouvé ayant le mot \"{recherche}\"...")

    pause()

    
### Submenu 2

def new_usager() -> None:
    print("[🧑] USAGER")
    # a mon humble avis ça fait moins moche que de faire 10000000 variables pour rien dans la mémoire, et en plus on créé le tuple d'avance (enfin une liste qu'on converti en tuple)
    liste_info = []
    liste_info.append(input("| Nom: "))
    liste_info.append(input("| Prénom: "))
    liste_info.append(input("| Addresse: "))
    liste_info.append(int(input("| Code postal: ")))
    liste_info.append(input("| Ville: "))
    liste_info.append(input("| E-Mail: "))
    liste_info.append(make_code_barre())
    print(f"| Code barre: {liste_info[6]} (généré automatiquement)")

    curseur.execute("""
INSERT INTO USAGER (nom,prenom,adresse,cp,ville,email,code_barre)
VALUES
(?,?,?,?,?,?,?)
""", liste_info)
    connexion.commit()

    pause()

def new_livre() -> None:
    print("[📕] LIVRE")
    liste_info = []
    liste_info.append(input("| Titre: "))
    liste_info.append(input("| Editeur: "))
    liste_info.append(int(input("| Année: ")))
    liste_info.append(input("| ISBN: "))
    
    curseur.execute("""
INSERT INTO LIVRE (titre,editeur,annee,isbn)
VALUES
(?,?,?,?)
""", liste_info)
    connexion.commit()

    pause()

def new_emprunt() -> None:
    print("[📄] EMPRUNT")
    liste_info = []
    liste_info.append(input("| Code barre de l'usager: "))
    liste_info.append(input("| ISBN du livre: "))
    liste_info.append(input("| Date de retour (yyyy-mm-jj): "))

    curseur.execute("""
INSERT INTO EMPRUNT (code_barre,isbn,retour)
VALUES
(?,?,?)
""", liste_info)
    connexion.commit()

    pause()

### Submenu 3
def ch_date_retour_livre() -> None:
    pause()

def ch_usager(donnee:str) -> None:
    if donnee not in ["nom","prenom","adresse","cp","ville","email"]:
        return

    code_barre = input("code barre du concerné? --> ")
    print(f"[🧑] USAGER -- ({code_barre})")
    if donnee == "nom":
        new_donnee = input("| Nouveau nom: ")
    elif donnee == "prenom":
        new_donnee = input("| Nouveau prénom: ")
    elif donnee == "adresse":
        new_donnee = input("| Nouvelle adresse: ")
    elif donnee == "cp":
        new_donnee = input("| Nouveau code postal: ")
    elif donnee == "ville":
        new_donnee = input("| Nouvelle ville: ")
    elif donnee == "email":
        new_donnee = input("| Nouvel e-mail: ")
    
    curseur.execute(f"""
UPDATE USAGER
SET {donnee}=?
WHERE code_barre=?
""", [new_donnee,code_barre])
    connexion.commit()

    pause()

### Submenu 4

def delete_livre() -> None:
    print("[📕🗑️] SUPPRIMER UN LIVRE")
    isbn = input("| ISBN: ")
    # vu que supprimer est une opération relativement dangereuse on peut annuler en mettant rien à la place de l'isbn
    if isbn != "":
        # On vérifie si le livre est déjà emprunté, sinon on pourra pas supprimer son emprunt car il existera pas et on aura une erreur...
        curseur.execute("""
    SELECT isbn FROM EMPRUNT
    WHERE isbn=?""", [isbn])
        emprunt_du_livre = curseur.fetchall()

        if len(emprunt_du_livre) >= 1:
            curseur.execute("""DELETE FROM EMPRUNT
        WHERE isbn=?""", [isbn])
            print("[i] l'emprunt du livre correspondant a été supprimé.'")
    
        curseur.execute("""
    DELETE FROM AUTEUR_DE
    WHERE isbn=?""", [isbn])
        curseur.execute("""
    DELETE FROM LIVRE
    WHERE isbn=?""", [isbn])

        connexion.commit()

    pause()

def delete_emprunt() -> None:
    print("[📄🗑️] SUPPRIMER L'EMPREINT D'UN LIVRE")
    isbn = input("| ISBN: ")

    if isbn != "":
        curseur.execute("""DELETE FROM EMPRUNT
    WHERE isbn=?""", [isbn])
        connexion.commit()

    pause()

def delete_usager() -> None:
    print("[🧑🗑️] SUPPRIMER UN USAGER")
    code_barre = input("| Code barre: ")

    if code_barre != "":
        # même logique que quand on supprime un livre, on regard si l'usager a emprunté des livres et on supprimes ses emprunts d'abord
        curseur.execute("""
        SELECT code_barre FROM EMPRUNT
        WHERE code_barre=?""", [code_barre])
        emprunts = curseur.fetchall()

        if len(emprunts) >= 1:
            curseur.execute("""
        DELETE FROM EMPRUNT
        WHERE code_barre=?""", [code_barre])

        curseur.execute("""DELETE FROM USAGER
    WHERE code_barre=?""", [code_barre])
        connexion.commit()

    pause()

### Submenu 5

def info_livre() -> None:
    isbn = input("isbn? --> ")
    curseur.execute("""
        SELECT titre, AUTEUR.prenom,AUTEUR.nom, editeur,annee
        FROM LIVRE JOIN ( 
        	AUTEUR_DE JOIN AUTEUR
        	ON AUTEUR_DE.id_auteur = AUTEUR.id_auteur
        ) ON LIVRE.isbn = AUTEUR_DE.isbn
        WHERE LIVRE.isbn = ?""",
        [isbn]
    )
    liste_res = curseur.fetchall()

    if(len(liste_res) >= 1):
        print(f"[📕] LIVRE ({isbn})")
        print(f"| Titre: {liste_res[0][0]}")
        print(f"| Auteur: {liste_res[0][1]} {liste_res[0][2]}")
        print(f"| Editeur: {liste_res[0][3]}")
        print(f"| Annee: {liste_res[0][4]}")
        print("")
    else:
        print(f"[❌] Livre d'ISBN '{isbn}' introuvable")
    
    pause()

def info_usager() -> None:
    code_barre = input("code barre? --> ")
    curseur.execute("""
        SELECT prenom, nom, email, adresse, ville, cp FROM USAGER
        WHERE code_barre = ?
        """,
        [code_barre]
    )
    liste_res = curseur.fetchall()

    liste_res = liste_res[0] # de toute façon on a qu'un seul résultat
    if(len(liste_res) >= 1):
        print(f"[🧑] USAGER ({code_barre})")
        print(f"| Prénom, Nom: {liste_res[0]} {liste_res[1]}")
        print(f"| E-mail: {liste_res[2]}")
        print(f"| Adresse: {liste_res[3]}")
        print(f"| Ville: {liste_res[4]}")
        print(f"| Code postal: {liste_res[5]}")
        print("")
    else:
        print(f"[❌] Aucune personne avec le code barre {code_barre} trouvée.")
    pause()
