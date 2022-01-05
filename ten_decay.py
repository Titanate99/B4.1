# -*- coding: utf-8 -*-
# ten_decay.py
"""
Created:  Tue Jul 31, 2018
Modified: Wed Aug 1, 2018

Description
-----------
Simulate radioactive decay and compare the simulation with the exponential 
decay law for 10 different trials. 
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand

def get_decay_data(N0, lam, Dt):
    """
    Simulate a series of radioactive decay measurements.
    
    Parameters
    ----------
    N0 : int
        initial number of particles
    lam : float
        decay probability
    Dt : float
        time interval for decay measurements
        
    Returns
    -------
    N_t : array_like
        number of particles left after time `times`
    times : array_like
        time since beginning of decay measurments   
    """
    P_decay = lam*Dt    # Probability of decay in each time interval
    
    # Array to hold the number of particles left at the end of each time 
    # interval. Initialize it to start with N0 particles.
    Nleft = N0
    N_t=np.array([Nleft]) 
    
    # Repeat until all the particles have decayed
    while Nleft != 0:
        # Set the number of particles to be the number at the end of the last
        # time interval.
        Npart = Nleft
        
        # Go through all the particles to see if each one decays. If a particle 
        # decays, reduce the number left by one.
        for N in range(Npart):
            r = rand()
            if (r < P_decay):
                Nleft = Nleft-1
                
        # Append the number of particles left after this time interval to the
        # array containing the number of partles left from the previous time 
        # intervals. 
        N_t = np.append(N_t,Nleft)
    
    # Create corresponding time array
    times = np.arange(len(N_t))*Dt 
    return (times,N_t)

#%% Initialize the needed parameters
N0 = 15     # Set the initial number of particles
lam = 0.01  # Define the decay probability
Dt = 0.01   # Define the time interval

N_life = 3 # Set the number of particle lifetimes to plot
time_max = N_life/lam # Compute total time to plot

N_points = N_life*round(1/(lam*Dt)) # Calculate the total number plotting points

N_ave = np.zeros(N_points) # Create an array to hold the simulations average

#%% Plot ten simulations in single figure window
plt.figure(1)
plt.clf()
for idx in range(10):
    plt.subplot(5,2,idx+1) # Use subplots to put all plots in the same figure
    plt.axis([0,time_max,0,N0]) # Set the axis ranges to plot   
    times,N_t = get_decay_data(N0,lam,Dt)

    # The code below is needed to pad the simulation arrays with 
    # zeros after all the particles have decayed so the array's values
    # can be averaged. If the N_t array is longer than the average then
    # we just slice the portion we need. 
    if (len(N_t)<len(N_ave)):
        N_pad = N_points-len(N_t)
        N_pad = np.pad(N_t,(0,N_pad),'constant',constant_values=(0,0))
        N_ave = N_ave + N_pad
    elif (len(N_t)>len(N_ave)):
        N_ave = N_ave + N_t[:len(N_ave)]
    else:
        N_ave = N_ave + N_t
        
    # Plot the number of particles as a function of time for the simulation
    plt.plot(times,N_t,'r-',label='Simulation')  

    # Compute and plot the exponential decay law
    model_times = np.linspace(0,time_max) # create new times array for plotting
    N_model = N0*np.exp(-lam*model_times)
    plt.plot(model_times,N_model,label='Exponential decay')
    # The following code removes the time tick labels except for the 
    # bottom plots. This makes the plots look neater.
    if (idx < 8 ):
        plt.xticks([])
        
plt.savefig('ten_plots.png',dpi=300)
plt.show() 

#%% Creat and plot the average of the ten simulations
N_ave = N_ave/10 # Compute the average

plt.figure(2)
plt.clf()
times_ave = np.linspace(0,time_max,len(N_ave)) # Create the plots time array
plt.plot(times_ave,N_ave,'r-',label='Average of Simulations')
plt.plot(model_times,N_model,label='Exponential decay')
plt.legend()
plt.xlabel('Time')
plt.ylabel('N')
plt.savefig('ave_plots.png',dpi=300)
plt.show()