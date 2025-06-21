# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 14:25:57 2025

@author: Toonzombie
"""

text = "Hola mundo de penes"
inverseText = ""
auxText = ""
for i in range(len(text)):
    if text[-i-1] != ' ':
        auxText += text[-i-1]
    else:
        for j in range(len(auxText)):
            inverseText += auxText[-j-1]
            
        inverseText += text[-i-1]
        auxText = ""    
for j in range(len(auxText)):
    inverseText += auxText[-j-1]
print(inverseText)