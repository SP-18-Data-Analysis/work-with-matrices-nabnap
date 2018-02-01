# -*- coding: utf-8 -*-
import numpy as np

#Create a numpy matrix(type:array) of 7 rows and 3 columns
a = np.random.rand(7,3)

#Print the matrix as is.
print("Original Matrix:")
print(a)

#Transpose the matrix into matrix b in order
#to make printing one column per line easier
b = a.T;

#For each row in the transpose, join the rows list
#with a ", " so the printing of the line looks nice
print("\nMatrix Column Per Line:")
for rcol in b:
  print(", ".join(str(x) for x in rcol))

#Note: Could have just print(b) however the assignment
#said to use looping.