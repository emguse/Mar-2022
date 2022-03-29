from tkinter import Y
from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y')

ex1 = -3/2 * x + 6 - y
ex2 = 1/2 * x + 2 - y

print(solve((ex1, ex2)))