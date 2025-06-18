# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 12:21:28 2025

@author: Toonzombie
"""
from enum import Enum
import os
def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
def CreateColumnEnum(numberOfVariables, numberOfConstraints):
    labels = {}
    for i in range(numberOfVariables):
        labels[f'x{i+1}'] = len(labels)
    for i in range(numberOfConstraints):
        labels[f's{i+1}'] = len(labels)
    labels['R'] = len(labels)
    return  Enum('ColumnIndex', labels)

class SimplexMethod():
    def __init__(self, numberOfVariables, numberOfConstraints, problemType):
        self.numberOfVariables = numberOfVariables
        self.numberOfConstraints = numberOfConstraints
        self.problemType = problemType
        self.numberOfColumns = numberOfVariables + numberOfConstraints + 1
        self.numberOfRows = numberOfConstraints + 1
        self.tableu = [[0.0 for _ in range(self.numberOfColumns)] for _ in range(self.numberOfRows)]
        #self.basis = ["s" + str(i) for i in range(self.numberOfConstraints + 1)]
        #self.basis[-1] = "Z"
        self.pivotColumn = -1
        self.pivotRow = -1
        self.basis = []
        self.ColumnIndex = CreateColumnEnum(numberOfVariables, numberOfConstraints)
    def initialize(self):
        for i in range(self.numberOfRows):
            print("\n==========================================")
            for j in range(self.numberOfColumns):
                if i > self.numberOfConstraints - 1:
                    if j > self.numberOfVariables-1 and j < self.numberOfConstraints + self.numberOfVariables:
                        self.tableu[i][j] = 0.0
                    elif j > self.numberOfConstraints + self.numberOfVariables - 1:
                        self.tableu[i][j] = 0.0
                        print("==========================================\n")
                    else: 
                        self.tableu[i][j] = -1 * float(input(f"Introduce objective function x{j+1} value: "))
                elif j > self.numberOfVariables-1 and j < self.numberOfConstraints + self.numberOfVariables:
                    if i + self.numberOfVariables == j:
                        self.tableu[i][j] = 1.0
                elif j > self.numberOfConstraints + self.numberOfVariables - 1:
                    self.tableu[i][j] = float(input(f"Introduce constraint number {i+1} right side value: "))
                    print("==========================================\n")
                else: 
                    self.tableu[i][j] = float(input(f"Introduce constraint number {i+1} x{j+1} value: "))
        for i in range(1, self.numberOfConstraints + 1):
            self.basis.append(self.ColumnIndex[f's{i}'])
    def IsOptimalSolution(self):
        if self.problemType == 1: #Minimizacion
            for i in range(self.numberOfColumns - 1):
                if self.tableu[-1][i] > 0:
                    return False
        elif self.problemType == 0: #Maximizacion
            for i in range(self.numberOfColumns - 1):
                if self.tableu[-1][i] < 0:
                    return False
        return True
     
    def UpdateBasisVariables (self):  
        for i in self.ColumnIndex:
            if i.value == self.pivotColumn:
                self.basis[self.pivotRow] = i
                break
    def FindPivotColumnAndRow(self):
        self.pivotColumn = -1
        self.pivotRow = -1
        if self.problemType == 1:
            aux = float('-inf')
            for i in range(self.numberOfColumns - 1):
                if self.tableu[-1][i] > aux:
                    aux = self.tableu[-1][i]
                    self.pivotColumn = i
        elif self.problemType == 0:
            aux = float('inf')
            for i in range(self.numberOfColumns -1):
                if self.tableu[-1][i] < aux:
                    aux = self.tableu[-1][i]
                    self.pivotColumn = i
        if self.pivotColumn == -1:
            return
        minRatio = float('inf')
        for i in range(self.numberOfRows - 1):
            aux = self.tableu[i][self.pivotColumn]
            if aux > 0:     
                ratio = self.tableu[i][-1]/aux
                if ratio < minRatio:
                    minRatio = ratio
                    self.pivotRow = i
    def UpdateTableu(self):
        for i in range(self.numberOfColumns):    
            self.tableu[self.pivotRow][i] = self.tableu[self.pivotRow][i]/self.tableu[self.pivotRow][self.pivotColumn]
        for i in range(self.numberOfRows):
            aux = self.tableu[i][self.pivotColumn]
            if i != self.pivotRow:
                for j in range(self.numberOfColumns):
                    self.tableu[i][j] = self.tableu[i][j] - (aux * self.tableu[self.pivotRow][j])
    def PrintTableu(self, numberOfIteration):
        print(f"\n\nSimplex Tableu (Iteration {numberOfIteration})\n")
        print(" B\t", end="")
        for i in range(self.numberOfVariables):
            print(f" x{i+1}\t",end="")
        for i in range(self.numberOfConstraints):
            print(f" s{i+1}\t",end="")
        print(" R", end= "")
        for i in range(self.numberOfRows):
            for j in range(self.numberOfColumns):
                if j == 0 and i < self.numberOfConstraints:
                    print(f"\n{self.basis[i].name}\t" , end= "")
                    print(f"{self.tableu[i][j]}\t", end = "")
                elif j == 0: 
                    print("\nZ\t", end = "")
                    print(f"{self.tableu[i][j]}\t", end = "")

                else:
                    print(f"{self.tableu[i][j]}\t", end = "")
    def PrintSolution(self):
        print("\n\n==========================================")
        print("\nLa solucion optima es")
        for i in range(self.numberOfConstraints):
            print(f"{self.basis[i].name} = ", end= "")
            print(f"{self.tableu[i][-1]}\t", end="")
        print("Z = ", end="")
        print(f"{self.tableu[-1][-1]}")
        return
    def Solve(self):
        numberOfIteration = 1
        self.PrintTableu(numberOfIteration)
        
        while not self.IsOptimalSolution():
            numberOfIteration += 1
            self.FindPivotColumnAndRow()
            if self.pivotColumn == -1 or self.pivotRow == -1:
                print("\nNo se encontró un pivote válido. Posible solución óptima, no acotada o error.")
                break
            self.UpdateBasisVariables()
            self.UpdateTableu()
            self.PrintTableu(numberOfIteration)
        self.PrintSolution()
            
def main():
    ClearConsole()
    print("\n\n\t\t\t\t==========================================")
    print("\t\t\t\t==============SIMPLEX METHOD==============")
    print("\t\t\t\t==========================================")
    print("\nBefore starting be sure to have the optimization problem in standard form.\n")
    numberOfVariables = int(input("Introduce the number of variables (whithout slack variables): "))
    numberOfConstraints = int(input("Now introduce the number of '<=' constraints: "))
    problemType = int(input("Is is a maximization or a minimization problem? [Max = 0, Min =1]: "))
    solver = SimplexMethod(numberOfVariables, numberOfConstraints, problemType)
    solver.initialize()
    solver.Solve()
if __name__ == "__main__":
    main()