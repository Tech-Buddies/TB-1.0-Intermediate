# importing neccessary libraries
import math
def add():
    input_list = []
    while True:
        try:
            n_inp = int(input("How many numbers would you like to add?\n"))
            if (type(n_inp)==int and (n_inp>0)):
                break
        except Exception as e:
            print("Please enter an integer greater than 0")
    print("Enter each of the %d number(s) one after the other" %(n_inp))
    while n_inp>0:
        try:
            numb = float(input())
            if type(numb)==float:
                input_list.append(numb)
                n_inp-=1
        except Exception as a:
            print("Enter only numbers")
    print("The sum of the numbers is: %f" %sum(input_list))
        
#add()  
        
def mult():
    input_list = []
    while True:
        try:
            n_inp = int(input("How many numbers would you like to multiply?\n"))
            if (type(n_inp)==int and (n_inp>0)):
                break
        except Exception as e:
            print("Please enter an integer greater than 0")
    print("Enter each of the %d number(s) one after the other" %(n_inp))
    while n_inp>0:
        try:
            numb = float(input())
            if type(numb)==float:
                input_list.append(numb)
                n_inp-=1
        except Exception as a:
            print("Enter only numbers")
    print("The product of the numbers is: %f" %(math.prod(input_list)))


def Simp_Avg():
    input_list = []
    while True:
        try:
            n_inp = int(input("How many numbers would you like to find their average?\n"))
            if ((type(n_inp)==int) and (n_inp>0)):
                break
        except Exception as e:
            print("Please enter an integer greater than 0")
    print("Enter each of the %d number(s) one after the other" %(n_inp))
    n=n_inp
    while n>0:
        try:
            numb = float(input())
            if type(numb)==float:
                input_list.append(numb)
                n-=1
        except Exception as a:
            print("Enter only numbers")
    print("The average of the numbers is: %f" %(sum(input_list)/n_inp))
#Simp_Avg()

''' A function to return the Weighted Average of a set of numbers 

L_n takes in a set of numbers as a list
L_w takes their corresponding weights as a list and returns a real number
'''
def Wtd_Avg():
    numb_list = []
    w_list = []
    while True:
        try:
            n_inp = int(input("How many numbers would you like to find their average?\n"))
            if ((type(n_inp)==int) and (n_inp>0)):
                break
        except Exception as e:
            print("Please enter an integer greater than 0")
    print("Enter each of the %d number(s) and their corresponding weight one after the other" %(n_inp))
    n=n_inp
    while n>0:
        try:
            numb = float(input("number:\n" ))
            w = float(input("Enter the corresponding weight:\n"))
            if type(numb)==float and type(w)==float:
                numb_list.append(numb)
                w_list.append(w)
                n-=1
        except Exception as a:
            print("Enter only numbers")
    w_sum = sum([num*weight for num in numb_list for weight in w_list if numb_list.index(num)==w_list.index(weight)])
    s_m = sum(w_list)
    print("The weighted average of the numbers is: %f" %(w_sum/s_m))
#Wtd_Avg()

''' A function to return the Geometric Mean of a set of numbers 

L_n takes in a set of numbers as a list and returns a real number
'''
def Geo_Mean():
    input_list = []
    while True:
        try:
            n_inp = int(input("How many numbers would you like to find their Geometric Mean?\n"))
            if ((type(n_inp)==int) and (n_inp>0)):
                break
        except Exception as e:
            print("Please enter an integer greater than 0")
    print("Enter each of the %d number(s) one after the other" %(n_inp))
    n=n_inp
    while n>0:
        try:
            numb = float(input())
            if type(numb)==float:
                input_list.append(numb)
                n-=1
        except Exception as a:
            print("Enter only numbers")
    print("The geometric mean of the numbers is: %f" %(math.prod(input_list)**(1/len(input_list))))
#Geo_Mean()       

''' A function to return the Quadratic root given real numbers a,b and cand b^2-4ac >=0 
for the square root to be real where a>0
output is in form of a turple
'''    
def Quad_root():
    a = float(input("Enter the value of a:\na= " ))
    b = float(input("Enter the value of b4:\nb= "))
    c = float(input("Enter the value of c:\nc= "))
    D = b**2 - 4*a*c
    while c>0:
        try:
            if type(a)==float and type(b)==float and type(c)==float:
                break
        except Exception as k:
            print("Enter only numbers")
    if (D<0):
        print("The solution to the qudaratic equation is:")
        print(str(-b/2*a) + "+" + str(abs(D)**(1/2)/2*a) + "i" +","+ str(-b/2*a) + "-"+ str(abs(D)**(1/2)/2*a) + "i")

    else:
        print("The solution to the qudaratic equation is")
        print((-b/2*a) + (D**(1/2)/2*a)  , (-b/2*a) - (D**(1/2)/2*a))
Quad_root()

