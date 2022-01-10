from math import *

def add_num(x= 5, y = 7):
    sumAnswer = x + y
    print("sum of {0} and {1} = {2:.2f}".format(x,y,sumAnswer))
    return sumAnswer

def sub_num(x = 4, y = 9):
    subAnswer = x - y
    print("difference between {0} and {1} = {2:.2f}".format(x,y,subAnswer))
    return subAnswer

def multiply_num(x = 3, y = 2):
    multAnswer = x * y
    print("{0} multiplied by {1} = {2:.2f}".format(x,y, multAnswer))
    return multAnswer

def divide_num(x = 8, y = 3):
    divAnswer = x / y
    print("{0} divided by {1} = {2:.2f}".format(x,y,divAnswer))
    return divAnswer

def avg_nums(x = [4,3,9,7,3,2,8]):
    avgAnswer = sum(x)/len(x)
    print("The average of {0} = {1:.2f}".format(x, avgAnswer))
    return avgAnswer

def geoavg_num(x = [4,3,9,7,3,2,8]):
    multvals = 1
    for i in range(0,len(x)):
        multvals = multvals * x[i]
    gmeanAnswer = multvals ** (1/len(x))
    print("The geometric mean of {0} = {1:.2f}".format(x,gmeanAnswer))
    return gmeanAnswer

def harm_mean(x = [4,3,9,7,3,2,8]):
    a = list(map(lambda x : 1.0/x, x))
    harmMean = len(x)/sum(a)
    print("The harmonic mean of {0} = {1:.2f}".format(x,harmMean))
    return harmMean

def weigthedAvg(x = [4,3,9,7,3,2,8], y = [2,8,1,5,9,6,2]):
    weiAvg = sum(list(map(lambda x,y: x * y, x,y)))/sum(x)
    print("The weighted average of weights {0} and occurence {1} = {2:.2f}".format(x,y,weiAvg))
    return weiAvg

def quadroot(a = 2, b = -7, c = 4):
    root1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    root2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    print("The roots of the equation ({0}x^2) + ({1}x) + ({2}) are {3:.2f} and {4:.2f}".format(a,b,c,root1,root2))
    return [root1, root2]


a1 = add_num()
a2 = multiply_num()
a3 = divide_num()
a4 = sub_num()

b1 = avg_nums()
b2 = geoavg_num()
b3 = harm_mean()
b4 = weigthedAvg()
b5 = quadroot()




