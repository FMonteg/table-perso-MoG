import json
import os
import re


project_prefix = "fcp_"

file_name = "nom_fichier"

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'texte_brut.txt')
with open(file_path, encoding='utf-8') as f:
    texte_brut = f.readlines()
print(texte_brut)



table = {}
index = True
while len(texte_brut)>0:
    if index:
        combien = int(texte_brut[0][2:-1])
        index = False

        del texte_brut[0]
        file_name = texte_brut[0][:-1]

        i = 0
    else:
        del texte_brut[0]
        value = texte_brut[0][:-1]
        table[i] = value

        i += 1
        if i == combien:
            index = True

            file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), project_prefix+file_name+'.json')
            with open(file_path, 'w') as json_file:
                json.dump(table, json_file, indent=4)
                pass

            table = {}


    del texte_brut[0]
