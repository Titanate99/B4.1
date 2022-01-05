# -*- coding: utf-8 -*-
# radioactive.py
"""
Created:  Tue Jul 31, 2018
Modified: Wed Aug 1, 2018

Description
-----------
Simulate radioactive decay and compare the simulation with the exponential 
decay law. 
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand

# Get the initial number of particles
N0 = int(input("Enter the initial number of particles: "))
lam = 0.01          # Decay constant 
Dt = 0.01           # Time interval
P_decay = lam*Dt    # Probability of decay in each time interval

Nleft = N0

# Array to hold the number of particles left at the end of each time interval
N_t=np.array([Nleft]) 

# Repeat until all the particles have decayed
while Nleft != 0:
    # Set the number of particles to be the number at the end of the last time
    # interval.
    Npart = Nleft
    
    # Go through all the particles to see if they decay. If a particle decays,
    # reduce the number left by one.
    for N in range(Npart):  # Go through all the particles
        r = rand()
        if (r < P_decay):
            Nleft = Nleft-1
            
    # Append the number of particles left after this time interval to the array
    # containing the number of partles left from the previous time intervals. 
    N_t = np.append(N_t,Nleft)

# Create the time array
times = np.arange(len(N_t))*Dt 

# Plot the simulated number of particles as a function of time
plt.plot(times,N_t,'r-',label='Simulation')  

# Compute and plot the exponential decay law
N_ave = N0*np.exp(-lam*times)
plt.plot(times,N_ave,label='Exponential decay')

plt.xlabel('Time')
plt.ylabel('Number of particles')
plt.legend()
plt.show() 