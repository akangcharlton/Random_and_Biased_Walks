# -*- coding: utf-8 -*-
"""
Senior Honours Project 2023/24
Abigail Charlton

Model 2 - Adapted from Kumar's model

This code generates random and biased random walks by varying step size in
both dimensions (x,y). It takes the number of steps and the number of
simulations and outputs the distance the particle managed to travel in this 
time. (All docstrings and comments added are my own.)

"""

import numpy as np

#set number of simulations and empty list to add displacements to
no_of_sims = 1000
no_of_steps = 100
disp_list = []

def randomwalksimulate():
    
    """
    This function carries out the random walk by choosing a random step 
    distance for each axis and adds them to a list. It then creates a path by
    joining the origin array and the steps array and then cumulatively adds the
    steps to the previous one to generate the final position. It outputs this
    path. To implement the biased gradient, the ratio of backwards to forwards
    movement can be changed as this changes how far backwards the particle can
    move and also decreases the probability that the backwards movement will
    be randomly chosen.
    """
 
    #create empty step list to add to and define 2 dimensions of movement
    steplist = []
    dims = 2
    
    step_n = no_of_steps
    
    #define the step range
    steps = [*range(0, 101, 1)] 
    exclude = {range(-51, 50, 1)}
    step_set = [i for i in steps if i not in exclude]
    
    #set origin
    origin = np.zeros((1,dims))

    step_shape = (step_n,dims)
    
    #choose steps randomly and add to step list
    steps = np.random.choice(a=step_set, size=step_shape)
    steplist.append(steps)
    
    #create path and add cumulatively
    path = np.concatenate([origin, steps]).cumsum(0)
    
    return path


def data_extract():
    
    """
    This function carries out the random walk and extracts each position from 
    path and returns a tuple containing the elements of the path.
    
    """
    
    #carry out random walk
    path = randomwalksimulate()

    #begin loop over the path
    for pos in range(len(path)):
        
        #extract each position in the path and create an array of the elements
        sample = path[pos]
        yield np.array([ sample[0], sample[1] ])

#begin a for loop over the range of simulations        
for i in range(no_of_sims):
    
    #creates array of x y positions
    temp1 = np.array(list(data_extract())).T 

    point1 = temp1
    
    #accesses last elements of array, i.e., the last position
    last_x = point1[0, -1]
    last_y = point1[1, -1]

    #calculates the total displacement from origin and appends to the list
    disp = np.hypot(last_x, last_y)
    disp_list.append(disp)

#maximum, minimum and average displacement taken from list
max_disp = max(disp_list)
min_disp = min(disp_list)
av_disp = np.average(disp_list)

print(f"Over {no_of_sims} simulations, particle travels an average of {av_disp} microns in {no_of_steps} seconds")
print(f"Max = {max_disp}")
print(f"Min = {min_disp}")


