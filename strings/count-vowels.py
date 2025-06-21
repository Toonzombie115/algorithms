# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 14:25:48 2025

@author: Toonzombie
"""
"""
Dado un string, ceunta cuantas vocales y cuantas consonantes contiene. 
Ignora los espacios y signos de puntuacion. No distingue mayusculas de minusculas
"""
vowels = ['a', 'e', 'i', 'o', 'u']

def CountVowels(sentence):
    sentence = sentence.lower()
    numberOfVowels = 0
    numberOfConsonants = 0
    for i in sentence:
        isVowel = False
        for j in range(len(vowels)):
            if i == vowels[j]:
                numberOfVowels += 1
                isVowel = True
                break
        if i.isalpha() and not isVowel:
            numberOfConsonants += 1       
    print(f"Vowels: {numberOfVowels}\tConsonants: {numberOfConsonants}")

text = "Tangamandapio"
CountVowels(text)        
    