# -*- coding: utf-8 -*-
"""
Created on Wed Feb 05 11:19:15 2020

@author: rguha
"""

# This problem was developed by Raj Guha and this brute force algorithm was designed by Raj Guha to compare with an efficient version 

# Problem Statement: Given an array of unsorted numbers, find the elemental numbers whose squares and cubes are present in the array
import numpy as np
import math

arr = []        
for i in range(1,1000):
    arr = np.append(arr, np.random.randint(1,1000))  
    
#arr = [1,2,8,64,225,15,512,81] # A simpler test case array
#arr = [1,2,8,64,225,10,15,512,81,1000,100,27,3] # A longer test case array

N = len(arr)
arr_sqr = np.zeros((N, 2))  
arr_cube = np.zeros((N, 2)) 


for i in range(0,N):
    
        sqr = int(math.pow(arr[i],2))
        arr_sqr[i][0] = sqr
        arr_sqr[i][1] = arr[i] # labeling the 2nd element of 2D array as the original number to be squared
        
        cube = int(math.pow(arr[i],3))
        arr_cube[i][0] = cube
        arr_cube[i][1] = arr[i] # labeling the 2nd element of 2D array as the original number to be cubed

       

arr_reference = np.concatenate((arr_sqr,arr_cube),axis=0) # Merging 2 arrays one above another row
Nr = len(arr_reference)
#print(arr_reference)


for i in range(0,Nr):
    
    for j in range(0,N):
        
        if (i<Nr/2):
            del2 = arr[j]- arr_reference[i][0]
            if(abs(del2) == 0.0):
                #print(arr[j],"Squared")
                print(round(arr[j]**0.5), "n which has a n^2")
                break
        
        else:    
            del3 = arr[j] - arr_reference[i][0]
            if(abs(del3) == 0.0):
        
                #print(arr[j],"Cubed")
                print(round(arr[j]**0.333), "n which has a n^3")
                break   
