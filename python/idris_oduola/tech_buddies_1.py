import math
#TB1.0 Assignment 1
def add(a,b): #calculates the sum of two values
    return a+b

def minus(a,b): #Returns the difference of two values
    return a-b

def div(a,b): #Returns the division of two values
    return a/b

def mult(a,b): #Returns the product of two values
    return a*b
#Vals is the list of values whose averages are to be calculated

def simp_avg(vals): #Returns the simple average
    simple_avg = sum(vals)/len(vals)
    return simple_avg
#weights is the list of weights
def weighted_avg(weights, vals): #Returns the weighted average
    num = 0
    for i in range(len(weights)):
        num = num + (weights[i]*vals[i])
    weighted_average = num/sum(weights)
    return weighted_average

def geo_mean(vals): #calculates the geomeetric mean
    n = len(vals)
    prodval = 1
    for i in range(n):
        prodval = prodval *vals[i]
    geo_mean = (prodval)**(1/n)
    return geo_mean

def harm_mean(vals): #Calculate the harmonic mean
    recipocals = list() #this stores the recipocals of the values
    for i in range(len(vals)):
        reci = 1/vals[i]
        recipocals.append(reci)

    harmonic_mean = len(vals)/sum(recipocals)
    return harmonic_mean

a = int(input('Enter a value for a:'))
b = int(input('Enter a value for b:'))
c = int(input('Enter a value for c:'))
def quad_roots(a,b,c): #Returns the roots of a quadratic equation
    det = math.sqrt((b)**2 - 4*a*c)
    q1 = (-b + det)/(2*a)
    q2 = (-b - det)/(2*a)
    sol = [q1,q2]
    return sol

#This codes below are supplementary codes to computes the values, the wieghts
vals = list() #declares an empty list
n = 5 #According to the assignment, n = 5
for i in range(n):
    val  = float(input('Enter value for x{}:'.format(i+1)))
    vals.append(val)

weights = list()
for j in range(n):
    weight = float(input('Enter value for w{}:'.format(j+1)))
    weights.append(weight)

#This prints the output of the functions

mean  = simp_avg(vals)
print('The simple average of the above values is {}'.format(mean))
weight_mean = weighted_avg(weights,vals)
print('The weighted average of the above values is {}'.format(weight_mean))
geom = geo_mean(vals)
print('The geometric mean of the above values is {}'.format(geom))
h_mean  = harm_mean(vals)
print('The harmonic mean of the above values is {}'.format(h_mean))
root = quad_roots(a,b,c)
print('The roots of the quadratic equation are {}'.format(root))
