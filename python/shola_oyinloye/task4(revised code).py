'''This file entails the week 2 assignment '''

import math
import cmath
import statistics as s
from statistics import mean
import numpy as np



#This function returns the addition of all input
def add():
    '''
    Asks user for multiple values to sum.
    
    Args: 
        None. 

    Returns:
        Sum of inputs.
    '''

    while True:
        try:
            x = [int(float(x)) for x in input('Enter multiple values separated by comma to Add: ').split(',')]
            break
        except Exception:
            print('Please input numbers only.')
            continue

    print('The numbers enterred are: {}'.format(x))
    
    try:
        total = 0
        for i in x:
            total+=i
    except Exception as e:
        print(e)
    else:
        print('The total number is: {}'.format(total))



#This function returns the elementwise subtraction of all input
def subtract():
    '''
    Asks user for multiple values to subtract.
    
    Args: 
        None. 

    Returns:
        Subtraction of inputs.
    '''

    while True:
        try:
            x = [int(float(x)) for x in input('\nEnter multiple values separated by comma to Subtract: ').split(',')]
            break
        except Exception:
            print('Please input numbser only.')
            continue

    print('The numbers enterred are: {}'.format(x))

    try:
        result = 0
        for i in x:
            result-=i
    except Exception as e:
        print(e)
    else:
        print('The result is: {}'.format(result))


#This function returns the elementwise division of all input
def divide():
    '''
    Asks user for multiple values to divide.
    
    Args: 
        None. 

    Returns:
        Division of inputs.
    '''

    while True:
        try:
            x = [int(float(x)) for x in input('\nEnter multiple values separated by comma to Divide: ').split(',')]
            break
        except Exception:
            print('Please input numbser only.')
            continue

    print('The numbers enterred are: {}'.format(x))

    try:
        result = 1
        for i in x:
            result/=i
    except Exception as e:
        print(e)
        print('Please enter a real number')
    else:
        print('The result is: {}'.format(result))



#This function returns the product of all input       
def multiply():
    '''
    Asks user for multiple values to multiple.
    
    Args: 
        None. 

    Returns:
        Multiplication of inputs.
    '''

    while True:
        try:
            x = [float(x) for x in input('\nEnter multiple values separated by comma to Multiply: ').split(',')]
            break
        except Exception:
            print('Please input numbers only.')
            continue

    print('The numbers enterred are: {}'.format(x))
    
    try:
        result = 1
        for i in x:
            result*=i
    except Exception as e:
        print(e)
        print('Please enter a real number')
    else:
        print('The result is: {}'.format(result))



#This function return the simple mean of all input
def simple_avg():
    '''
    Asks user for multiple values to compute the simple mean.
    
    Args: 
        None. 

    Returns:
        Simple Mean of inputs.
    '''

    while True:
        try:
            print('\nPlease provide values to compute the Simple Mean')
            list = [float(x) for x in input('Enter multiple values separated by comma to compute the Simple Average: ').split(',')]
            print(list)
            break
        except Exception:
            print('Please correct input only.')
            continue

    avg = mean(list)
    print('The average number is: {}'.format(avg))



#This function return the geometric average of the input
def geometric_avg():
    '''
    Asks user for multiple values to the geometric avearage.
    
    Args: 
        None. 

    Returns:
        Geometric Average of inputs.
    '''

    while True:
        try:
            print('\nPlease provide values to compute the Geometric Mean')
            value = [float(x) for x in input('Enter multiple values separated by comma: ').split(',')]
            print(value)
            break
        except:
            print('Please input numbers only.')
            continue

    geom_mean = math.prod(value)**(1/len(value))
    print('The Geometric mean is: {}'.format(geom_mean))


#This function return the harmonic average of the input
def harmonic_avg():
    '''
    Asks user for multiple values to the harmonic avearage.
    
    Args: 
        None. 

    Returns:
        Harmonic Average of inputs.
    '''
    
    while True:
        try:
            print('\nPlease provide values to compute the Harmonic Mean')
            harm_list =[float(x) for x in input('Enter multiple values separated by comma to compute the Harmonic Average: ').split(',')]
            break
        except:
            print('Please input numbers only.')
            continue

    harm_mean = s.harmonic_mean(harm_list)
    print('The Harmonic mean is: {}'.format(harm_mean))




#This function return the weighted avarage
def weighted_avg():
    '''
    Asks user for multiple values to the weighted avearage.
    
    Args: 
        None. 

    Returns:
        Weighted Average of inputs.
    '''

    print('\nPlease provide values to compute the Weighted Mean')
    while True:
        try:
            vals = [float(x) for x in input('Enter values for x separated by comma: ').split(',')]
            weight = [float(x) for x in input('Enter values for multiple weights separated by comma: ').split(',')]
            if len(weight) != len(vals):
                print('The values for x and weights are not the same')
                print('Please make the values have the same length')
                continue
            x = np.array(vals)
            break
        except:
            print('Please input numbers only.')
            continue

    w_avg = np.average(x, weights = weight)
    print('The Weighted mean is: {}'.format(w_avg))



#This function return the quadratic root
def quadratic_root():
    '''
    Asks user for multiple values to the quadratic root.
    
    Args: 
        None. 

    Returns:
        Quadratic root of inputs.
    '''

    print('\nPlease provide values to compute the Quadratic root')
    while True:
        try:
            vals = [float(x) for x in input('Enter values for x separated by comma: ').split(',')]
            if len(vals) != 3:
                print('Enter three values only')
                continue
            break
        except:
            print('Please enter correct inputs.')
            continue

    a = vals[0]
    b = vals[1]
    c = vals[2]

    dis = (b**2) - (4 * a*c) #calculating the discriminant
    ans1 = (-b-cmath.sqrt(dis))/(2*a)
    ans2 = (-b + cmath.sqrt(dis))/(2*a)
    print('The root are: ' + str(ans1) + str(ans2))




def main():
    while  True:
        add()
        restart = input('\nWould you like to restart Addition? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break

    while  True:
        subtract()
        restart = input('\nWould you like to restart Subtraction? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break

    while  True:
        divide()
        restart = input('\nWould you like to restart Division? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break

    while  True:
        multiply()
        restart = input('\nWould you like to restart Multiplication? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break

    while  True:
        simple_avg()
        restart = input('\nWould you like to restart Simple Average? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break

    while  True:
        geometric_avg()
        restart = input('\nWould you like to restart Geometric Average? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break

    while  True:
        harmonic_avg()
        restart = input('\nWould you like to restart Harmonic Average? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break

    while  True:
        weighted_avg()
        restart = input('\nWould you like to restart Weight Average? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break

    while  True:
        quadratic_root()
        restart = input('\nWould you like to restart Quadratic Computation? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            break

if __name__ == '__main__':
    main()


