# Simplex Method
The simplex method is an algorithm used to solve linear programming 
problems and its main objective is to maximize or minimize a linear 
function. The linear function is subject to linear restrictions 
(equalities or inequialities).

## Algorithm

1.- Transform the restrictions to equialities using a slack variable 's' 
2.- The objective function must be in terms of maximization or 
minimization 
3.- Initialize a matrix with the coeficients of the 
restrictions, objective function, slack variables and solution. 
4.- Select the entry variable. (The most negative for maximization, the most 
possitive for minimization)
5.- Pivoting (Make pivot element = 1 and the other elemets in the row = 0)
6.- Stop until no negative coefficients are left in Z row
