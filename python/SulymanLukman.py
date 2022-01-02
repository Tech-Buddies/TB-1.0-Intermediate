#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def geometricMean(arr, n) :
    product = 1

    for i in range(0,n) :

        product = product * arr[i]

    gm = (float)(math.pow(product, (1 / n)))

    return (float)(gm)

arr = [ 1, 2, 3, 4, 5]

n = len(arr)

print ('{0:.2f}'.format(geometricMean(arr, n)))


# In[2]:


def weightedMean(X,W,n) :

   sum = 0

   numWeight = 0
   
   i = 0

   while  i < n :

       numWeight = numWeight + X[i] * W[i]

       sum = sum + W[i]

       i = i + 1

   return (float)(numWeight / sum)

X = [1, 2, 3, 4, 5]

W = [1, 2, 3, 4, 5]


n = len(X)

m = len(W) 

print ('{0:.6f}'.format(weightedMean(X, W, n)))


# In[9]:


import math
def equationroots( a, b, c):  
 my = b * b - 4 * a * c  
 sqrt_val = math.sqrt(abs(my))
 return (float) (-b + sqrt_val)/(2 * a) 

 
a = 9
b = 5
c = 3
print ('{0:.3f}'.format(equationroots( a, b, c)))


# In[ ]:





# In[23]:


def simpleaverage (num):
    sumnum = 0
    for t in num :
      sumnum = sumnum + t
    
    avg = sumnum/len(num)
    return avg
print ("your simpleaverage is", simpleaverage ([1,3,3,4,5]))


# In[24]:


def harmonicmean (a,b,c,d,e):
    n = 5
    Harmonic = n / (1/a + 1/b + 1/c + 1/d + 1/e)
    return Harmonic 
print("Your harmonic mean is", harmonicmean(1,2,3,4,5))


# In[ ]:






