import math
print("Simple Average")
def SimpleAverage(a,b,c,d,e):
    print((a+b+c+d+e)/5)
SimpleAverage(1,2,3,4,5)
print("------------------------------------")
print("Weghted Average")
print("------------------------------------")
def WeightedAverage(w1,w2,w3,w4,w5,x1,x2,x3,x4,x5):
    print((w1*x1+w2*x2+w3*x3+w4*x4+w5*x5)/(w1+w2+w3+w4+w5))
WeightedAverage(1,2,3,4,5,6,7,8,9,10)

print("------------------------------------")
print("Geometric Mean")
print("------------------------------------")
def GeometricMean(x1,x2,x3,x4,x5):
    print((x1+x2+x3+x4+x5)**(1/5))
GeometricMean(1,2,3,4,5)

print("------------------------------------")
print("Harmonic Mean")
print("------------------------------------")
def HarmonicMean(x1,x2,x3,x4,x5):
    print(5/(1/x1+1/x2+1/x3+1/x4+1/x5))
HarmonicMean(1,2,3,4,5)

print("------------------------------------")
print("Quadratic Root")
print("------------------------------------")
def QuadraticRoot(a,b,c):
    print((-b + math.sqrt(b**2+4*a*c))/(4*a), " or ", (-b - math.sqrt(b**2+4*a*c))/(4*a))
QuadraticRoot(1,2,3)