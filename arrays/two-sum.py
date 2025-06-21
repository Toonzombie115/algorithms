# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 13:26:17 2025

@author: Toonzombie
"""

"""
Dado un arreglo de enteros nums y un entro target, 
regresa los indices de los dos numeros que suman target.

Restriccion: No puedes usar el mismo elemento dos veces
"""
def TwoSum(nums, target):
    length = len(nums)    
    for i in range(length):
        for j in (i,length - 1):  
            if nums[i] + nums[j] == target:
                return i , j
    return -1
nums = [5, 5, 0, 7, 0 , 2]
target = 9
index = TwoSum(nums, target)
if index == -1:
    print("No se encontro la suma")
else:
    print(f"Los indices son {index[0]} y {index[1]}")