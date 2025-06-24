# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 13:41:36 2025

@author: Toonzombie
"""

"""
Eliminar duplicados de una lista

Input: [1,2,2,3,4,4,5] → Output: [1,2,3,4,5]
"""
from typing import List, Set
def RemoveDuplicatesList(aList: List[int]) -> Set:
    return set(aList)
data = [1,2,2,3,4,4,5]
print(RemoveDuplicatesList(data))
