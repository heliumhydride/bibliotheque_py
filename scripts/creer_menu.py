#!/bin/python3

import sys

# Ce script python sert à créer un menu en ascii art; Il ne fait pas partie du programme principal.
# fait à l'arrache, faut pas trop lire :/

def print_usage():
    print("""usage: creer_menu.py [element 1] [element 2] ...
Note: la hauteur est automatique""")

def creer_espaces(n:int) -> str:
    s = ""
    for _ in range(n):
        s += ' '
    return s

espace_entre_bord_et_txt = 4
espaces = creer_espaces(espace_entre_bord_et_txt)
len_str_long=len(max(sys.argv[1:], key=len))

print(sys.argv[1:])

if len(sys.argv) == 1:
    print_usage()
    exit(1)

print("+", end='')
for _ in range(2*len(espaces) + 3 + len_str_long):
    print("-", end='')
print("+")

print("|", end='')
for _ in range(2*len(espaces) + 3 + len_str_long):
    print(" ", end='')
print("|")

for i in range(len(sys.argv[1:])):
    print(f"|{espaces}{i+1}. {sys.argv[i+1]:{len_str_long}s}{espaces}|")

print("|", end='')
for _ in range(2*len(espaces) + 3 + len_str_long):
    print(" ", end='')
print("|")

print("+", end='')
for _ in range(2*len(espaces) + 3 + len_str_long):
    print("-", end='')
print("+")

