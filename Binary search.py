# -*- coding: utf-8 -*-
"""
Created on Mon Mar 09 10:34:47 2020

@author: rguha
"""

import numpy as np
import random


def binarySearch(target,arr):
        
    low = 0
    high = len(arr)



    while(low<=high):
            
        mid = (low + high)/2
    
        if target == arr[mid] :
            print("Target location position after binary search:", mid)
            print("The corresponding array element after binary search :", arr[mid])
            break
        
        else:
                if target < arr[mid]:
                    high = mid-1
                    
                if target > arr[mid]:
                    low = mid+1
                
                
# Driver Code 
if __name__ == '__main__': 

     arr = [1,5,10,15,20,30,50,67,123,679,680,1120,4456,7890,12234,112345,501234,700000]  
     size = len(arr)
     target_index = random.randint(1,size)
     target = arr[target_index]
     print("The random target is:", target)
     binarySearch(target,arr)                    