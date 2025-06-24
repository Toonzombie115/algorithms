# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 22:40:55 2025

@author: Toonzombie
"""

"""
Contar frecuenci de letras
Dado un string, cuenta cuantas veces aparece cada letra (usa Counter y sin Counter).
input: "banana" -> Output: {b:1, a:3, n:2}
"""
from collections import Counter
from collections import defaultdict
contador = Counter()

text = 'Pepe pecas pica papas'
text = text.lower()
for char in text:
    contador[char] += 1
print(contador.keys())
print(contador.values())
for key, value in contador.items():
    if key == ' ':
        print("space ",value)
        continue
    print(key, value)
print("\nSin Counter")
myDic = {}
myDic = defaultdict(int)
for char in text:
        myDic[char] += 1
for key, value in contador.items():
    if key == ' ':
        print("space ",value)
        continue
    print(key, value)
    