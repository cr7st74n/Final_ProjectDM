# ***************************************************************
#  Final Project - Universal/Existential Quantifier
#
# Purpose: The purpose of this application is to create a program tha create a
# sequence using a loop and from there, the program will calculate the universal/existential
# quantifier.
#
# ***************************************************************
# Name: Cristian Gonzalez
# Date: 4/24/2024
# ************************************************************

# 1: Create sequence A 
A = []

for n in range(1,101):
    A.append((2 * n) + 3)

# 2: Determine the truth values for the quantifier statements
# (2a) Universal quantifier statement
universalFunction = True  #give the function a true value
for x in A:
    if not (5 <= x <= 200):  #Condition when I will check if my sequence is in this range, if not set universalFunction as False
        universalFunction = False
        break

# (2b) Existential quantifier statement
existentialFunction = False #give the function a false value
for x in A:
    if x >= 50: #Condition when I will check if my sequence is in this range, if not set universalFunction as True
        existentialFunction = True
        break


#Comparing the results with the built-in function in Python:

# Universal quantifier 
universal_PythonF = all(5 <= x <= 200 for x in A)

# Existential quantifier 
existential_PythonF = any(x >= 50 for x in A)

# 3: Print the results
print("Final Project Results")

print("My program Results:")

print(" All elements in Sequence A: \n")

print(A, "\n")

print("(3b) The universal quantifier statement is", universalFunction)

print("(3c) The existential quantifier statement is", existentialFunction)

print("\n Python Built-in Function Results:")

#  Print elements 
print(" All elements in Sequence A: \n")
print(A, "\n")

# Built in function! 

print("(3b) The universal quantifier statement is", universal_PythonF)
print("(3c) The existential quantifier statement is", existential_PythonF)    


