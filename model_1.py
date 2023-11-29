# -*- coding: utf-8 -*-
"""
Senior Honours Project 2023/24
Abigail Charlton

Model 1

This code is used to simulate random and random biased walks by varying angle
and step size. It should run a walk until it reaches a target distance of user 
input over a number of simulations of user input. It should then return the 
values of how long, on average, it took for the particle to reach the target, 
and the minimum and maximum times it took over all the simulations. As a bonus,
it also has a progress bar for the number of simulations it has completed.
"""

#import necessary modules
import numpy as np
from tqdm import tqdm

#set target x value and number of simulations
target_x = 10
num_simulations = 100

#set empty list to store time data of each simulation
time_list = []

def walk_time():
    
    
    """
    This function carries out a random or biased random walk depending on the
    allowed angle the code can choose from. It then chooses a random step size
    based on Fenchel's values of run time 50-100 microns per second. Each step
    is 1 second. It returns the time, in seconds, of the random walk to reach
    the target x.
    
    """
    
    #set initial x position and number of steps to add to
    x0 = 0
    num_steps = 0
    
    #begin while loop to set the target and run until target reached
    while x0 < target_x:
        #choose random angle and step size
        angle = np.random.uniform(0, 2 * np.pi)
        step_size = np.random.uniform(0.05, 0.1)
        
        #change x position based on step size and angle and add a step count
        x0 += step_size * np.cos(angle)
        num_steps += 1
        
        #1 second per step, can be changed
        t_sec = num_steps * 1
        
    return t_sec

#progress bar
progress_bar = tqdm(total=num_simulations, desc="Simulations")

#begin loop over the range of simulations
for i in range(num_simulations):
    
    #carry out function
    t_sec = walk_time()

    #add how long it took to list 
    time_list.append(t_sec)
    
    progress_bar.update(1)
    
progress_bar.close()
    
#take average time
av_t = np.mean(time_list)

#create better units
t_days = av_t / (24*60*60)
max_time = max(time_list) / (24*60*60)
min_time = min(time_list) / (24*60*60)

print(f"Particle reached the target x-value of {target_x} mm:")
print(f"{int(av_t)} seconds")
print(f"{int(t_days)} days")
print(f"Max days: {max_time}")
print(f"Min days: {min_time}")