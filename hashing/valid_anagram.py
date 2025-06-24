# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 12:57:36 2025

@author: Toonzombie
"""
"""
Dado dos strings, determina si son anagramas (tienen las mismas letras, distinto orden).

Input: "listen" y "silent" → Output: True
"""
from collections import defaultdict

def ValidAnagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    dic1 = {}
    dic2 = {}
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    for char in string1: dic1[char] += 1
    for char in string2: dic2[char] += 1
    return True if dic1 == dic2 else False 

text1 = "listen"
text2 = "silent"
print(ValidAnagram(text1, text2))