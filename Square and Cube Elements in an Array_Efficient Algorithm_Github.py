# -*- coding: utf-8 -*-
"""
Created on Wed Feb 05 01:32:32 2020

@author: rguha
"""

# This problem was developed by Raj Guha and solution algorithm was designed by both Sandeep Dey and Raj Guha

# Problem Statement: Given an array of unsorted numbers, find the elemental numbers whose squares and cubes are present in the array

import numpy as np

#arr =  [125,2,8,64,225,3,9,15,11,512,5,81,121,729] # A simple test array
arr = [0]        
for i in range(0,1001):
    arr = np.append(arr, np.random.randint(1,1000))  
arr = arr[1:1000] 
#print(arr)
N = len(arr)
max_arr = np.max(arr) + 1

arr_bool_type =[]
arr_bool_power =[]
arr_bool_element = []
arr_bool_reference= []


for i in range(0,max_arr):
    arr_bool_type= np.append(arr_bool_type,"False") # Storing the square and cube values as True 
    arr_bool_power= np.append(arr_bool_power,"None") # Storing the power as 'Squared' or 'Cubed'
    arr_bool_element = np.append(arr_bool_element,0) # Storing the basic elements of the input array as the squared or cubed indices
    arr_bool_reference = np.append(arr_bool_reference,max_arr+10) # Storing the original input array elements for comparison. 'max_arr+10' is an arbitrary constant element not in the array



for i in range(0,N):
    
    arr_bool_reference[arr[i]] = arr[i]
    
    if(arr[i]**2 <= max_arr ):
        
        index1 = arr[i]**2
        arr_bool_type[index1]= 'True'
        arr_bool_power[index1] = 'Squared'
        arr_bool_element[index1] = arr[i]
       
    arr_bool_reference[arr[i]] = arr[i]    
    
    if(arr[i]**3 <= max_arr):    
        index2 = arr[i]**3
        arr_bool_type[index2]= "True"
        arr_bool_power[index2] = "Cubed"
        arr_bool_element[index2] = arr[i]
        
        

for i in range(0,max_arr):
    if(arr_bool_type[i] == 'True' and arr_bool_power[i]== 'Squared' and arr_bool_reference[i] != max_arr+10):
        print ("Squared element", arr_bool_element[i])
    if(arr_bool_type[i] == 'True' and arr_bool_power[i]== 'Cubed' and arr_bool_reference[i] != max_arr+10):
        print ("Cubed element", arr_bool_element[i])   