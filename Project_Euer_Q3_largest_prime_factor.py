"""
Project Euler problem solutions using Python

by

Charanraj Thimmisetty
charanrajt@gmail.com

Q:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 
"""

import numpy as np
number=600851475143
limit=np.sqrt(number)

def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(np.sqrt(n))+1):
            if n%i==0:
                return False
                break            
            elif i==int(np.sqrt(n)):
                return True
#Solution one            
                
for i in range(int(np.sqrt(number))+1,2,-1):
    if number%i==0:
        if is_prime(i):
            ans=i
            print ans
            break
    
#Solution 2
for i in range(2,int(np.sqrt(number))+1):
    if number%i==0:
        if is_prime(i):
            ans=i
            
print ans                            
