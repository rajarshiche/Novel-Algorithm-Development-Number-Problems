# -*- coding: utf-8 -*-
"""
Created on Wed Feb 05 11:36:58 2020

@author: rguha
"""
# The following script is a simple and detailed implementation of Radix sort algorithm with maximum 3-digit elements in the array

from sympy import *
from math import  *

import numpy as np
import sympy as sym

arr_const = np.array([60, 300, 33, 7, 193, 11])
arr = arr_const

arr1=[0] # IF YOU JUST DECLERARE arr1 =[], Python will take it as floating array and mess up calculation
arr2=[0]
arr3=[0]

N = len(arr_const )

# Pre-processing of data to get 1st, 2nd & 3rd digits : Not needed for the program
for i in range(0,N):
    arr1= np.append(arr1,arr[i]%10)
    arr2= np.append(arr2,(arr[i]/10)%10)
    arr3 =np.append(arr3,(arr[i]/100)%10)
    
print(arr1)
print(arr2)
print(arr3)

for k in range(0,3):
    
    arr_val=[0]   # You need to have a zero value as the first element, else Python will take it as floating number array and % or mod calculations will be wrong
    arr_index=[0]

    if k==0:
        for i in range(0,N):  # Iterating from 0 to N-1 i.e. N sized arr
            arr_index= np.append(arr_index,arr[i]%10) # to take the rightmost digit as bin index
            arr_val = np.append(arr_val,arr[i])  # add corresponding values of the index to the bin
        
       
    if k==1:
        for i in range(0,N):
            arr_index= np.append(arr_index,(arr[i]/10)%10) # to take the middle digit as bin index
            arr_val = np.append(arr_val,arr[i])            # add corresponding values of the index to the bin
#        break     
      
    if k==2:
        for i in range(0,N):
            arr_index =np.append(arr_index,(arr[i]/100)%10)  # to take the leftmost digit as bin index
            arr_val = np.append(arr_val,arr[i])              # add corresponding values of the index to the bin
#           
#
    a0 =a1=a2=a3=a4=a5=a6=a7=a8=a9=[0]   # Every time we refreshes bins with index arrays: Total 0 - 9 index bins
    arr_new=[0]                          # Every time we refreshes bins with value arrays: Total 0 - 9 value bins
        
    # Arranging or classifying the values to the bins    
    
    for i in range(1,N+1):               # Since the 1st element is zero as per defiition, we iterate from 2nd elemet i.e. index 1 to N+1
        if arr_index[i] == 0:
            a0 = np.append(a0,arr_val[i]) # If the index matches with bin number which is between 0 - 9, we also add the corresponding value to the bin 
                
        if arr_index[i] == 1:
            a1 = np.append(a1,arr_val[i])    
        
        if arr_index[i] == 2:
            a2 = np.append(a2,arr_val[i])  
                
        if arr_index[i] == 3:
            a3 = np.append(a3,arr_val[i])  
                
        if arr_index[i]== 4:
            a4 = np.append(a4,arr_val[i])      
        
        if arr_index[i] == 5:
            a5 = np.append(a5,arr_val[i]) 
                
        if arr_index[i] == 6:
            a6 = np.append(a6,arr_val[i])     
        
        if arr_index[i] == 7:
            a7 = np.append(a7,arr_val[i])      
        
        if arr_index[i]== 8:
            a8 = np.append(a8,arr_val[i]) 
                
        if arr_index[i]== 9:
            a9 = np.append(a9,arr_val[i])
            
        # Merging the values of the bins to a single array   
        
        if i == N:
                
            if len(a0) > 1 :  # We consider after the 1st element which is 0 by definition
                for i in range(1,len(a0)):   # We iterate over 1 to length of the bin, 0-th element being constant in all bins be definition
                    arr_new = np.append(arr_new,a0[i])
            if len(a1) > 1 :
                for i in range(1,len(a1)):
                    arr_new = np.append(arr_new,a1[i])
        
            if len(a2) > 1 :
                for i in range(1,len(a2)):
                    arr_new = np.append(arr_new,a2[i])
        
            if len(a3) > 1 :
                for i in range(1,len(a3)):
                    arr_new = np.append(arr_new,a3[i])
        
            if len(a4) > 1 :
                for i in range(1,len(a4)):
                    arr_new = np.append(arr_new,a4[i])
                        
            if len(a5) > 1 :
                for i in range(1,len(a5)):
                    arr_new = np.append(arr_new,a5[i])
                        
            if len(a6) > 1 :
                for i in range(1,len(a6)):
                    arr_new = np.append(arr_new,a6[i])                
        
            if len(a7) > 1 :
                for i in range(1,len(a7)):
                    arr_new = np.append(arr_new,a7[i]) 
        
            if len(a8) > 1 :
                for i in range(1,len(a8)):
                    arr_new = np.append(arr_new,a8[i]) 
        
            if len(a9) > 1 :
                for i in range(1,len(a9)):
                    arr_new = np.append(arr_new,a9[i]) 
    
    arr=arr_new[1:]  # We take the arr ignoring the 1st element of arr_new which is 0 by definition. This will again go into the iteration.


print("Input or Original Array", arr_const)
print("Sorted Array Using Radix Sort Algorithm", arr)