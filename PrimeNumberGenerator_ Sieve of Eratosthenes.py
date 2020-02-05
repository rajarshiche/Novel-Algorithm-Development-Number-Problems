# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 10:52:06 2020

@author: rguha
"""

import numpy as np
import array as arr

N = 1000;
N_sqrt = N**0.5

number=[2]
for i in range (3,N+1):
    number= np.append(number,i)
print(number)
Np = len(number) 


for i in range(0,int(N_sqrt)): # The limit should be till prime number * prime number 
    
    number_temp = []
    

    
    for j in range(0,Np):
        
        if(number[j]<= number[i]):
            number_temp = np.append(number_temp,number[j])
            
        if(number[j]> number[i] and number[j]%number[i] != 0):
            number_temp = np.append(number_temp,number[j])

    
    
    number = number_temp
    Np = len(number)
    
print("\n")    
print("Prime Number Array") 
print(number)   
