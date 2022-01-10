from math import *
import cmath as cm
from functools import *


def acceptInput1():
    
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
    return b

#======================================================================

def acceptInput2():
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
    
    return b

#=========================================================================

def getInput(b):
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
    
    return c

#============================================================================#

def add():
    
    print('''
    Adding numbers together.
    ------------------------
    This function adds two or more numbers together and prints out an output.
    Example:
    x = [1,2,3,5]
    add(x)
    --------
    The sum of [1,2,3,5] = 11
    ''')
    
    x = acceptInput1()
    sumAnswer = sum(x)
    print("The sum of {0} = {1}".format(x, sumAnswer))


#===========================================================================#

def subtract():
    
    print('''
    Finding differences between a set of numbers.
    ----------------------------------------------------------
    This function finds the difference between two (2) or more numbers and prints out an output.
    Example:
    x = [1,2,3,5]
    subtract(x)
    --------
     The difference between the set of numbers [1,2,3,5] = 1 - 2 - 3 -5 = -9.0
    ''')
    
    x = acceptInput1()
    subAnswer = reduce(lambda x, y: x - y, x)
    print("The difference between the set of numbers {0}= {1:.2f}".format(x, subAnswer))

#===========================================================================#

def multiply():
    
    print('''
    Multiplying numbers together.
    ---------------------------------------
    This function multiplies two (2) or more numbers and prints out an output.
    Example:
    x = [1,2,3,5]
    multiply(x)
    --------
     The product of the set of numbers [1,2,3,5] = 1 x 2 x 3 x 5 = 30.0
    ''')
    
    x = acceptInput1()
    multAnswer = reduce(lambda x, y: x*y, x)
    print("The product of the set of numbers {0} = {1:.2f}".format(x,multAnswer))

#===========================================================================#

def divide():
    
    print('''
    Division of numbers.
    This function divides two (2) or more numbers by each other and prints out an output.
    Example:
    x = [1,2,3,5]
    multiply(x)
    --------
     The product of the set of numbers [1,2,3,5] = 1 / 2 / 3 / 5 = 1/30.0 = 0.03
    ''')
    
    x = acceptInput2()
    divAnswer = reduce(lambda x, y: x/y, x)
    print("The division of the set of numbers {0} = {1:.2f}".format(x,divAnswer))

#===========================================================================#

def simple_avg():
    
    x = acceptInput1()
    avgAnswer = sum(x)/len(x)
    print("The average of {0} = {1:.2f}".format(x, avgAnswer))

#===========================================================================#

def geometric_avg():
    
    x = acceptInput1()
    multvals = reduce(lambda x, y: x*y, x)
    gmeanAnswer = multvals ** (1/len(x))
    print("The geometric mean of {0} = {1:.2f}".format(x, gmeanAnswer))

#===========================================================================#

def harmonic_avg():
    
    x = acceptInput1()
    a = list(map(lambda x : 1.0/x, x))
    harmMean = len(x)/sum(a)
    print("The harmonic mean of {0} = {1:.2f}".format(x, harmMean))


#===========================================================================#

def weighted_avg():
    
    print("Hey! we are accepting two different sets of values here!!")
    print("We are starting with the weights!!! so, let's gooo.....")
    x = acceptInput1()
    print('''
    Good! You've done a great job!!
    Now let's accept your occurences
    ''')
    y = getInput(x)
    weiAvg = sum(list(map(lambda x,y: x * y, x,y)))/sum(x)
    print("The weighted average of weights {0} and occurence {1} = {2:.2f}".format(x,y,weiAvg))

#===========================================================================#

def quadroot():
    
    print("""
    Here, you are only going to supply the coefficients of x^2, x and constant c with their sign.
    Remember to input your values in the right order!
    Let's start!!
    """)
    
    # Co-efficient of x^2 (a)
    a = ''
    while True:
      try:
        n = input("enter the co-efficient of x^2 :  ")
        if float(n) == 0:
            print("co-efficient of x^2 cannot be equal to zero")
        else:
            a = float(n)
      except ValueError:
        print("Input a valid number")

      if len(str(a)) > 0:
        break
    
    # Co-efficient of x (b)
    d = ''
    while True:
      try:
        d = float(input("enter the co-efficient of x :  "))
      except ValueError:
        print("Input a valid number")

      if len(str(d)) > 0:
        break

    # Constant C
    r = ''
    while True:
      try:
        r = float(input("enter the constant (c) :  "))
      except ValueError:
        print("Input a valid number")

      if len(str(r)) > 0:
        break

    print("Your co-efficients are {0}, {1}, {2}".format(a, d, r))
    
    
    a,b,c = a,d,r
    opd = b**2 - 4*a*c
    if opd > 0:
      root1 = (-b + sqrt(opd))/(2*a)
      root2 = (-b - sqrt(opd))/(2*a)
    else:
      root1 = (-b + cm.sqrt(opd))/(2*a)
      root2 = (-b - cm.sqrt(opd))/(2*a)
    print("The roots of the equation ({0}x^2) + ({1}x) + ({2}) are {3:.2f} and {4:.2f}".format(a,d,r,root1,root2))