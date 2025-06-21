# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 17:25:07 2025

@author: Toonzombie
"""

text = "Ferrocarrilero"
counting = []
letters = []
for i in text:
    aux = text.count(i)
    if aux > 1 and i not in letters:
        letters.append(i)
        counting.append(aux)
print("Las letras repetidas fueron: ")
for i in range(len(letters)):
    print(f"{letters[i]} -> {counting[i]} veces")
        