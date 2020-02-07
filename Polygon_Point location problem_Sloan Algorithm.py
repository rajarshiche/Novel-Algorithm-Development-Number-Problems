# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 13:16:29 2020

@author: rguha
"""
# This program evaluates whether for a given non-self intersecting polygon geometry, a test point in located inside, on the side or outside of polygon or not

import numpy as np
import matplotlib.pyplot as plt


coord = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
coord.append(coord[0]) #repeat the first point to create a 'closed loop'

xs, ys = zip(*coord) #create lists of x and y values

plt.figure()
plt.plot(xs,ys) 
plt.show() 
#--------------------------------------------------------------------------------------------------------------------------------------------------------        
## Sloan Algorithm for convex/ concave polygon  
       
## For calculating whether the vertex is concave or convex: We will take 3 consecutive points annticlockwise, if the determinant > 0 they are anticlockwise and mid-vertex is convex. If determinant < 0 they are clockwise and mid vertex is concave  

coord_new = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
coord_new.append(coord_new[0]) #repeat the first point to create a 'closed loop' needed for considering 3 points consecutively
coord_new.append(coord_new[1]) #repeat the 2nd point to create a 'closed loop' needed for considering 3 points consecutively
n = len(coord)
print(n)

convexity = []        
for i in range (0,n-1):

        
    b = np.array([ [1, coord_new[i][0], coord_new[i][1] ], [1, coord_new[i+1][0], coord_new[i+1][1] ], [1, coord_new[i+2][0], coord_new[i+2][1] ] ]) 
    print(b)
    
    detr_val = np.linalg.det(b)
    print(detr_val)
    
#    detr = np.append(detr, detr_val)
    
    if detr_val>0:  # We are considering polygon points anti-clockwise
        print("mid-vertex point is convex", [coord_new[i+1][0], coord_new[i+1][1] ] )
        convexity = np.append(convexity,'True')
    if detr_val<0:
        print("mid-vertex point is concave", [coord_new[i+1][0], coord_new[i+1][1] ] )        
        convexity = np.append(convexity,'False')
 

#Test point coordiate input
#point = [0.6,1.8]
#point = [0.6,2.0]
#point = [0.6, 2.0]
#point = [1.8,1.8]
#point = [3.0,-9.0]
#point = [0.6, 1.0]
#point = [2.0, 3.0]

#Defining points again to loop over each side of polygon and plot the test point        
coord_new = [[1,1], [2,1], [2,2], [1,2], [0.5,1.5]]
coord_new.append(coord_new[0]) #repeat the first point to create a 'closed loop' needed for considering 3 points consecutively
n = len(coord)
print(n) 

#Test point coordiate input
xp = 1.4
yp = 1.6
point = [xp, yp];

plt.figure()
plt.plot(xs,ys) 
plt.scatter(xp, yp, c = 'r', alpha=0.5, s = 10) 
plt.show() 

m2 = []

norm_dist = []

norm_vertex = []

area_triangle = []

area_val = []

for i in range (0,n):
    area_val = np.append(area_val,0.0)

tol = 10**(-3)

# Looping over each side

for i in range (0,n-1):
    
    if ( coord_new[i][0]-coord_new[i+1][0] == 0):
        
        diff = coord_new[i][0]- coord_new[i+1][0] 
        diff = tol
        m2 = np.append( m2, (coord_new[i][1]-coord_new[i+1][1]) / (diff) ) # Calculating slope of each side with adjuting the denomiator not to zero
    
    else:    
    
        m2 = np.append( m2, (coord_new[i][1]-coord_new[i+1][1]) / (coord_new[i][0]-coord_new[i+1][0]) )
    
    yi = ( (coord_new[i+1][1] - coord_new[i][1]) * (point[0] + m2[i] * point[1]) - (coord_new[i][0]*coord_new[i+1][1] - coord_new[i+1][0]*coord_new[i][1] )      )/ ( (coord_new[i+1][0] - coord_new[i][0]) + m2[i] * (coord_new[i+1][1] - coord_new[i][1])  )
    
    xi = point[0] + m2[i]*point[1] - m2[i]*yi
    
    side_intersect = [xi, yi]
    
    norm_dist = np.append( norm_dist, distance.euclidean(point,side_intersect) )
    
    norm_vertex = np.append (norm_vertex, distance.euclidean(point,coord_new[i]) )
    
    
    b = np.array([ [coord_new[i][0] - point[0] , coord_new[i+1][0] - point[0] ], [coord_new[i][1] - point[1], coord_new[i+1][1] - point[1]] ]) 
    print(b)
    area = np.linalg.det(b) # Don't use any 1/2 factor here, won't work and area will show as 0
    print(area)
#    detr_val = 1/2 * ( np.linalg.det(b) )
#    detr_val = np.append(detr_val, area )
    area_val[i] = area/2
    
# To evaluate index of nearest side and nearest vertex

min_vertex_point =  np.min(norm_vertex) 
min_dist_point = np.min(norm_dist) 
print("min point to vertex",min_vertex_point)
print("min point to side",min_dist_point)

#index_min_dist_point = -1

for i in range(0,n-1):
    
    if (norm_vertex [i] == min_vertex_point ):
        index_min_vertex_point = i
        break
       
for i in range(0,n-1):
    
    if (norm_dist [i] == min_dist_point ):
        index_min_dist_point = i
        break
        
        
# Finding out the x's for which the y's are same as yp i.e. yp is at the same height (y-coordiate) as vertex points => SAME THING NEEDS FOR same x-coordinate case also
x_check = []     
y_check = []   
for i in range (0,n-1):
    
    if ( coord_new[i][1] - point[1] == 0): # Finding out the x's for which the y's are same as yp
        x_check = np.append(x_check, coord_new[i][0])
        
    if ( coord_new[i][0] - point[0] == 0): # Finding out the y's for which the x's are same as xp
        y_check = np.append(y_check, coord_new[i][1])
        
   
for i in range (0,n-1):

    # To check point inside polygon for convex polygons
    if ( min(norm_dist) < min(norm_vertex)  and  area_val[index_min_dist_point] > 0): 
        
        print("point is inside polygon", point)
        break
     
    # To check point inside polygon for concave polygons    
    if ( min(norm_dist) >  min(norm_vertex)  and  convexity[index_min_vertex_point] == 'False'):
         print("point is inside polygon", point)
         break
         
    # To check point on horizontal polygon side      
    if (  min(norm_dist) == 0  and  area_val[index_min_dist_point] == 0 and len(x_check)!=0): 
        
        if(( point[0] <= x_check[0] and point[0] >= x_check[1] ) or (point[0] >= x_check[0] and point[0] <= x_check[1] )):
            print("point is on the polygon side", point)
            break
        else:
            print("point is outside polygon", point)
            break
     
    # To check point on vertical polygon side    
    if (  min(norm_dist) == 0  and  area_val[index_min_dist_point] == 0 and len(y_check)!=0): 
        
        if(( point[1] <= y_check[0] and point[1] >= y_check[1] ) or (point[1] >= y_check[0] and point[1] <= y_check[1] )):
            print("point is on the polygon side", point)   
            break             
        else:
            print("point is outside polygon", point)
            break
        
    # To check point outside of polygon      
    if ( min(norm_dist) < min(norm_vertex)  and  area_val[index_min_dist_point] < 0): 
        print("point is outside polygon", point)
        break
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------        
        
    
    
    
    
    
    



































      