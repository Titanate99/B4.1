#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:30:23 2021

@author: nate_mac

Write a function that takes Ntotal as an input parameter and returns an estimate
for . Use this function to estimate  for . Use semilogx()1Links to an external 
site. to plot the estimated value of  as a function of Ntotal. Also plot the error 
using linear, semilog, or log-log scales and discuss the scaling.
"""


import random
import matplotlib.pyplot as plt
  


circle_points= 0
square_points= 0
 

 
# Total Random numbers generated= possible x
# values* possible y values

array= 10
arrays=[]
Pis=[]
truePi = 3.1415926535



for i in range(7): 
    
    for i in range(array):
      
        # Randomly generated x and y values from a
        # uniform distribution
        # Range of x and y values is -1 to 1
        rand_x= random.uniform(-1, 1)
        rand_y= random.uniform(-1, 1)
      
        # Distance between (x, y) from the origin
        origin_dist= rand_x**2 + rand_y**2
      
        # Checking if (x, y) lies inside the circle
        if origin_dist<= 1:
            circle_points+= 1
      
        square_points+= 1
      
        # Estimating value of pi,
        # pi= 4*(no. of points generated inside the 
        # circle)/ (no. of points generated inside the square)
        pi = 4* circle_points/ square_points
      
    ##    print(rand_x, rand_y, circle_points, square_points, "-", pi)
    ##    print("\n")
    print("When array is " + str(array) + " Pi is estimated at " + str(pi))
    arrays.append(array)
    Pis.append(abs(pi-truePi))
    array = array * 10

print(arrays)
print(Pis)

plt.semilogx(arrays,Pis)

plt.xlabel("Sample Range")
plt.ylabel("Estimation Error from Pi")
    
    
    
    

