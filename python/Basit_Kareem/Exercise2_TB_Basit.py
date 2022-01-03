from math import *
import cmath as cm
from functools import *

'''
Adding numbers together.
This function adds two or more numbers together and prints out an output.
Example:
x = [1,2,3,5]
add(x)
--------
 The sum of [1,2,3,5] = 11
'''

def add(x):
    sumAnswer = sum(x)
    return sumAnswer

print("""Hello friend! please input the numbers you will like to add together.
Input different values on separate line.
Remember, you are allowed to put negative numbers e.g (-5).
When you are done with all your values, please press the enter key or type 'done'.
""")
b = []
while True:
  try:
    a = input("input :  ")
    b = b + [float(a)]
  except ValueError:
    if a == 'done' or a == '':
      if len(b) > 1:
        break
      else:
        print("You need to give at least two (2) valid numbers")
    else:
      print("only numbers are allowed")

print("Your inputs are ", b)

k = add(b)

print("The sum of {0} = {1}".format(b, k))
#===========================================================================#
'''
Finding differences between a set of numbers.
This function finds the difference between two (2) or more numbers and prints out an output.
Example:
x = [1,2,3,5]
subtract(x)
--------
 The difference between the set of numbers [1,2,3,5] = 1 - 2 - 3 -5 = -9.0
'''

def subtract(x):
    subAnswer = reduce(lambda x, y: x - y, x)
    return subAnswer

print("""\n\n\nHello friend! please input the numbers you will like to work on.
Input different values on separate line.
Remember, you are allowed to put negative numbers e.g (-5).
When you are done with all your values, please press the enter key or type 'done'.
""")
b = []
while True:
  try:
    a = input("input :  ")
    b = b + [float(a)]
  except ValueError:
    if a == 'done' or a == '':
      if len(b) > 1:
        break
      else:
        print("You need to give at least two (2) valid numbers")
    else:
      print("only numbers are allowed")

print("Your inputs are ", b)

k = subtract(b)

print("The difference between the set of numbers {0}= {1:.2f}".format(b, k))
#===========================================================================#
'''
Multiplying numbers together.
This function multiplies two (2) or more numbers and prints out an output.
Example:
x = [1,2,3,5]
multiply(x)
--------
 The product of the set of numbers [1,2,3,5] = 1 x 2 x 3 x 5 = 30.0
'''

def multiply(x):
    multAnswer = reduce(lambda x, y: x*y, x)
    return multAnswer

print("""\n\n\nHello friend! please input the numbers you will like to work on.
Input different values on separate line.
Remember, you are allowed to put negative numbers e.g (-5).
When you are done with all your values, please press the enter key or type 'done'.
""")
b = []
while True:
  try:
    a = input("input :  ")
    b = b + [float(a)]
  except ValueError:
    if a == 'done' or a == '':
      if len(b) > 1:
        break
      else:
        print("You need to give at least two (2) valid numbers")
    else:
      print("only numbers are allowed")

print("Your inputs are ", b)

k = multiply(b)

print("The product of the set of numbers {0} = {1:.2f}".format(b,k))
#===========================================================================#
'''
Division of numbers.
This function divides two (2) or more numbers by each other and prints out an output.
Example:
x = [1,2,3,5]
multiply(x)
--------
 The product of the set of numbers [1,2,3,5] = 1 / 2 / 3 / 5 = 1/30.0 = 0.03
'''

def divide(x):
    divAnswer = reduce(lambda x, y: x/y, x)
    return divAnswer

print("""\n\n\nHello friend! please input the numbers you will like to work on.
Input different values on separate line.
Remember, you are allowed to put negative numbers e.g (-5).
When you are done with all your values, please press the enter key or type 'done'.
""")
b = []
while True:
  try:
    a = input("input :  ")
    if float(a) == 0:
      print("Please let's avoid ZeroDivisionError, input non-zero values only")
     # raise ZeroDivisionError("You can't divide by zero")
    else:
      b = b + [float(a)]
  except ValueError:
    if a == 'done' or a == '':
      if len(b) > 1:
        break
      else:
        print("You need to give at least two (2) valid numbers")
    else:
      print("only numbers are allowed")

print("Your inputs are ", b)

k = divide(b)

print("The division of the set of numbers {0} = {1:.2f}".format(b,k))
#===========================================================================#
def simple_avg(x):
    avgAnswer = sum(x)/len(x)
    return avgAnswer

print("""\n\n\nHello friend! please input the numbers you will like to work on.
Input different values on separate line.
Remember, you are allowed to put negative numbers e.g (-5).
When you are done with all your values, please press the enter key or type 'done'.
""")
b = []
while True:
  try:
    a = input("input :  ")
    b = b + [float(a)]
  except ValueError:
    if a == 'done' or a == '':
      if len(b) > 1:
        break
      else:
        print("You need to give at least two (2) valid numbers")
    else:
      print("only numbers are allowed")

print("Your inputs are ", b)

k = simple_avg(b)

print("The average of {0} = {1:.2f}".format(b, k))
#===========================================================================#

def geometric_avg(x):
    multvals = multiply(x)
    gmeanAnswer = multvals ** (1/len(x))
    return gmeanAnswer

print("""\n\n\nHello friend! please input the numbers you will like to work on.
Input different values on separate line.
Remember, you are allowed to put negative numbers e.g (-5).
When you are done with all your values, please press the enter key or type 'done'.
""")
b = []
while True:
  try:
    a = input("input :  ")
    b = b + [float(a)]
  except ValueError:
    if a == 'done' or a == '':
      if len(b) > 1:
        break
      else:
        print("You need to give at least two (2) valid numbers")
    else:
      print("only numbers are allowed")

print("Your inputs are ", b)

k = geometric_avg(b)

print("The geometric mean of {0} = {1:.2f}".format(b, k))
#===========================================================================#

def harmonic_avg(x):
    a = list(map(lambda x : 1.0/x, x))
    harmMean = len(x)/sum(a)
    return harmMean

print("""\n\n\nHello friend! please input the numbers you will like to work on.
Input different values on separate line.
Remember, you are allowed to put negative numbers e.g (-5).
When you are done with all your values, please press the enter key or type 'done'.
""")
b = []
while True:
  try:
    a = input("input :  ")
    b = b + [float(a)]
  except ValueError:
    if a == 'done' or a == '':
      if len(b) > 1:
        break
      else:
        print("You need to give at least two (2) valid numbers")
    else:
      print("only numbers are allowed")

print("Your inputs are ", b)

k = harmonic_avg(b)

print("The harmonic mean of {0} = {1:.2f}".format(b, k))
#===========================================================================#

def weighted_avg(x , y):
    weiAvg = sum(list(map(lambda x,y: x * y, x,y)))/sum(x)
    return weiAvg

print("""\n\n\nHello friend! please input the numbers you will like to work on.
Input different values on separate line.
Remember, you are allowed to put negative numbers e.g (-5).
When you are done with all your values, please press the enter key or type 'done'.
""")

print("Hey! we are accepting two different sets of values here!!")
print("We are starting with the weights!!! so, let's gooo.....")

b = []
while True:
  try:
    a = input("input :  ")
    b = b + [float(a)]
  except ValueError:
    if a == 'done' or a == '':
      if len(b) > 1:
        break
      else:
        print("You need to give at least two (2) valid numbers")
    else:
      print("only numbers are allowed")

c = []
while True:
  try:
    a = input("input :  ")
    c = c + [float(a)]
  except ValueError:
    if a == 'done' or a == '':
      if len(c) > 1:
        if len(c) == len(b):
          break
        else:
          print("The number of weights and frequencies must be the same")
      else:
        print("You need to give at least two (2) valid numbers")
    else:
      print("only numbers are allowed")
  
  if len(c) == len(b):
    break

print("Your Weights are ", b)
print("Your Frequencies are ", c)

k = weighted_avg(b, c)

print("The weighted average of weights {0} and occurence {1} = {2:.2f}".format(b,c,k))
#===========================================================================#

def quadroot(a, b, c):
    opd = b**2 - 4*a*c
    if opd > 0:
      root1 = (-b + sqrt(opd))/(2*a)
      root2 = (-b - sqrt(opd))/(2*a)
    else:
      root1 = (-b + cm.sqrt(opd))/(2*a)
      root2 = (-b - cm.sqrt(opd))/(2*a)
    return [root1, root2]

print('''
Welldone! You've really tried,.
One last thing!!!
.
.
.
Let's go quadratic.
Shall we???
''')

print("""Here, you are only going to supply the coefficients of x^2, x and constant c with their sign.
Remember to input your values in the right order!
Let's start!!
""")

# Co-efficient of x^2 (a)
a = ''
l = []
while True:
  try:
    n = input("enter the co-efficient of x^2 :  ")
    if float(n) == 0:
      print("co-efficient of x^2 cannot be equal to zero")
    else:
      a = float(n)
      l = l + [a]
  except ValueError:
    print("Input a valid number")

  if len(l) > 0:
    break

# Co-efficient of x (b)
d = ''
while True:
  try:
    d = float(input("enter the co-efficient of x^2 :  "))
  except ValueError:
    print("Input a valid number")

  if len(d) > 0:
    break

# Constant C
r = ''
while True:
  try:
    r = float(input("enter the co-efficient of x^2 :  "))
  except ValueError:
    print("Input a valid number")

  if len(r) > 0:
    break

print("Your co-efficients are {0}, {1}, {2}", a, d, r)

[k,l] = quadroot(a,d,r)

print("The roots of the equation ({0}x^2) + ({1}x) + ({2}) are {3:.2f} and {4:.2f}".format(a,d,r,k,l))