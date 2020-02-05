# -*- coding: utf-8 -*-
"""
Created on Tue Jan 07 08:24:33 2020

@author: rguha
"""
# Theis program will search for the minimum number which is both squared and cubed within a range of N_limit 

import numpy as np

N_limit = 1000;
N = 0

for m in range (1,N_limit):
           
    for n in range (1,N_limit):
        
        if (m**2%n**3) == 0:
            print("m & n are", m,n)
            N= (m * m**2/n**3)**2
            print("The minimum number which is squared and cubed both:",N)
            break
        
    if (N > N_limit ):
        break    

  
  
        