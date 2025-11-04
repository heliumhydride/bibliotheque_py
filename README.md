# 📚 bibliothèque.py

[README in English 🇺🇸🇬🇧](https://github.com/heliumhydride/bibliotheque_py/blob/master/README_en.md)

un logiciel de gestion de bibliothèque en [TUI](https://fr.wikipedia.org/wiki/Environnement_en_mode_texte)

### ❓ pourquoi?
C'est pour un projet de NSI en Terminale sur les bases de données.

### 🚀 installation
Clonez ce depôt, puis ouvrez une cmd/un terminal.
Commencez par initialiser une base de données:
```sh
python3 scripts/make_db.py
```

Le processus est guidé:
```
La DB n'existe pas.

quelle base de donnée voulez vous initialiser?
1. Base de donnée vide pour la production (recommandé) >>>
2. Base de donnée avec des exemples (pour tester le logiciel) >>>

* si vous ne savez pas, tapez '1'

--> ...
```

Puis lancez l'interface de gestion:
```sh
python3 bibliothèque.py
```
* !!! Si vous êtes sur Windows, n'utilisez pas 'py', mais bien 'python' ou 'python3'. 'py' n'aime pas le 'è' dans le nom du fichier, je ne sais pas pourquoi. !!!

### 💻 developpement
Les fonctionnalités sont a ajouter dans `lib/fonctions.py`
Les menus / tout en rapport avec l'interface est dans `lib/menu.py`

Il y a un script pour créer des menus très facilement (`scripts/creer_menu.py`)

Utilisation:
```
scripts/creer_menu.py [elt1] [elt2] ...
```

Exemple:
```
scripts/creer_menu.py "Truc 1 ->" "Truc 2 ->" "Fermer (x)"
['Truc 1 ->', 'Truc 2 ->', 'Fermer (x)']
+---------------------+
|                     |
|    1. Truc 1 ->     |
|    2. Truc 2 ->     |
|    3. Fermer (x)    |
|                     |
+---------------------+
```

Il suffit de faire copier coller du terminal dans un print("""...""")
