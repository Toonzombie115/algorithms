# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 13:48:55 2025

@author: Toonzombie
"""

"""
Dado un string, inviertelo sin usar funciones de libreria como [::-1] o .reverse()

"""
text = "Pene bien rico"
inverseText = ""
for i in range(len(text)):
    inverseText += text[-i - 1]
print(inverseText)