# 📚 bibliothèque.py

[README en Français 🇫🇷](https://github.com/heliumhydride/bibliotheque_py/blob/master/README.md)

a [TUI](https://en.wikipedia.org/wiki/Text-based_user_interface)-based library management software

### ❓ why?
It was a project in senior year of high school for programming class.

### 🚀 installation
Clone this repo, then open a cmd/terminal in it.
Start by initializing the database:
```sh
python3 scripts/make_db.py
```

The process is guided:
```
La DB n'existe pas.

quelle base de donnée voulez vous initialiser?
1. Base de donnée vide pour la production (recommandé) >>>
2. Base de donnée avec des exemples (pour tester le logiciel) >>>

* si vous ne savez pas, tapez '1'

--> ...
```

Translation:
```
The DB doesn't exist.

what database would you like to init?
1. Empty database for production (recommended) >>>
2. Database with examples (to test the software) >>>

* in case you don't know, type '1'
```

And then run the management UI:
```sh
python3 bibliothèque.py
```
* !!! If you're on Windows, don't use 'py', but 'python' or 'python3'. 'py' doesn't like the 'è' in the filename for some reason. !!!

### 💻 developement
Functions need to be added to `lib/fonctions.py`
Menus / anything interface related are in `lib/menu.py`

Usage:
```
scripts/creer_menu.py [elt1] [elt2] ...
```

Example:
```
scripts/creer_menu.py "Thing 1 ->" "Thing 2 ->" "Close (x)"
['Thing 1 ->', 'Thing 2 ->', 'Close (x)']
+---------------------+
|                     |
|    1. Thing 1 ->    |
|    2. Thing 2 ->    |
|    3. Close (x)     |
|                     |
+---------------------+
```

Just copy-and-paste from the terminal into a print("""...""") (without the printed list, which is meant to show the args)
