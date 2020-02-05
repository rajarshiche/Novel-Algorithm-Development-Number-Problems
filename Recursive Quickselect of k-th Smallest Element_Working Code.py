# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:31:47 2020

@author: rguha
"""
import numpy as np


def partition(arr, left, right):
    
    start = left+1
    end = right
    pivot = arr[left]
    
    while (start<=end) :
        
        while arr[start] < pivot:
            start = start + 1
            
        while arr[end] > pivot:
            end = end - 1
            
        if (start >= end):
            break
    
        if (start < end):
            swap(arr,start,end) # switching start index and end index elements at crossover to continue the partition
     

    swap(arr,left,end)     # switching end index and left index elements as end index element is the new pivot
        
    return end    # return the pivot position => k-th smallest element 
         

def swap(arr,index1, index2):
    
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    
    return arr
    
    
    
    
def quickselect(arr,left,right,k):
    
    if(left == right):      # This is required to complete both the left and right conditions i.e. == and the other one is <
        return arr[left]    # return the pivot position
    
    
    if(left<right):
        
    
        pivot_pos = partition(arr, left, right) # This is the actual pivot position in the array
    
    
        if (pivot_pos == k-1):
            return (arr[pivot_pos])  # In one sweep, pivot will be k-th smallest element and there will be k-1 elelments to the left (i.e. smaller)
    
        if (k - 1 < pivot_pos):    # the largest number in split_length or pivot_pos is pivot, so number smaller than that will be in left array
            return quickselect(arr, left, pivot_pos, k)   # Searching in the left array (between left & pivot_pos) with recursion with k
        
        
        if (k - 1 > pivot_pos):    # When k exceeds split_length or pivot_pos, we are actually looking for numbers greater than pivot, because higher the 'smallest kth' means larger number and on the right-hand side array
            return quickselect(arr, pivot_pos + 1, right, k)       # searching in the right array (betwee pivot_pos & right) with recursion with k. 

            
# Driver Code 
if __name__ == '__main__': 
  
#     arr = [12, 3, 5, 7, 4, 19, 26]  
     arr = [3,2,0,-6,6,4,1]  # Test array
#     arr = [7, 10, 4, 3, 20, 15]
     n = len(arr)
     k=7
     print("The k-th smallest element in the array is: ", quickselect(arr, 0, n-1 , k))
     

