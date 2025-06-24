# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 13:11:57 2025

@author: Toonzombie
"""
"""
Dado un arreglo, indica si hay algún valor que aparece al menos dos veces.

Input: [1,2,3,1] → Output: True
"""

def ContainsDuplicates(data):
    mySet = set()
    for i in data:
        if i not in mySet:
            mySet.add(i)
        else:
            print(f"{i} is a duplicate value")
            return True
    return False

data = [1,2,3,1]
print(ContainsDuplicates(data))