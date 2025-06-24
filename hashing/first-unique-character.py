# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 13:33:34 2025

@author: Toonzombie
"""

"""
Primer carácter no repetido

Dado un string, imprime el primer carácter que no se repite.

Input: "aabbccd" → Output: "d"
"""
from collections import defaultdict
def FirstUniqueChar(data):
    myDic = {}
    myDic = defaultdict(int)
    for char in data: myDic[char] +=1
    for key, value in myDic.items():
        if value == 1:
            return key
data = "aabbccde"
print(FirstUniqueChar(data))