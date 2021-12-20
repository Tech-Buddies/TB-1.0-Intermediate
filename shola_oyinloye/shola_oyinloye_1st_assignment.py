import math
import cmath
import statistics as s
from statistics import mean
import numpy as np


#Addition function
var1=int(input('Enter a number: '))
var2=int(input('Enter another number: '))

def add(var1,var2):
    sum = var1 + var2
    print('\nThe sum of ' + str(var1) + ' and ' + str(var2) + ' is:')
    print(sum)

print(add(var1,var2))


#Subtraction function
def sub(var1,var2):
    sub = var1 - var2
    print('\nThe subtraction of ' + str(var1) + ' and ' + str(var2) + ' is:')
    print(sub)

print(sub(var1,var2))


#Division function
def div(var1,var2):
    div = var1 / var2
    print('\nThe division of ' + str(var1) + ' and ' + str(var2) + ' is:')
    print(div)

div(var1,var2)


#Multiplication function
def mul(var1,var2):
    mul = var1 * var2
    print('\nThe product of ' + str(var1) + ' and ' + str(var2) + ' is:')
    print(mul)

mul(var1,var2)


#Simple Average
nums=input('Enter five numbers separated by comma: ')
list=nums.split(',')
for i in range(len(list)):
    list[i] = int(list[i])
 
def average(list):
    print(mean(list))

average(list)


#Weighted average
x = np.array([5,4,3,7,9])
weight = [0.3,0.5,0.1,0.2,0.3]

def Weighted_avg(x,weight):
    w_avg = np.average(x, weights = weight)
    print(w_avg)

Weighted_avg(x,weight) 


#Geometric mean
vals=[8,16,22,12,41]

def geo_mean(vals):
    geom_mean = math.prod(vals)**(1/len(vals))
    print('The Geometric mean is: ' + str(geom_mean))

geo_mean(vals)


#Harmonic mean
list =[11,32,44,76,99,1]

def har_mean(var):
    harm_mean = s.harmonic_mean(var)
    print('The Harmonic mean is: ' + str(harm_mean))

har_mean(list)


#Quadratic equation
a = 1
b = 4
c = 2

def quad_eqn(a,b,c):
    dis = (b**2) - (4 * a*c) #calculating the discriminant
    ans1 = (-b-cmath.sqrt(dis))/(2*a)
    ans2 = (-b + cmath.sqrt(dis))/(2*a)
    print('The root are: ' + str(ans1) + str(ans2))

quad_eqn(a,b,c)