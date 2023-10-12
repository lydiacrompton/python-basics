#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:28:43 2023

@author: lydiacrompton
"""

#L3-EX1

#Add simulation time to the algo of 1 neuron.
#Add real time to the algo of 1 neuron.
#Add and print execution time to the code of one neuron.


V_threshold = -65
V_membrane = -75
V_rest = -75
C=0.5
t_end=3.5

import sys

def update_V_membrane(spike_value, V_membrane):#delta
    V_membrane += spike_value
    return V_membrane

def check_threshold(V_membrane):#lambda- basically the spike impact
    
    if V_membrane >= V_threshold:
        return 5
    else:
        return 0 

def simulator(spikeList, t_end, c):
    t = 0 
    #index of the input spike list is called n 
    n = 0 
    tstart=time.time() #real time???
    
    while(t < t_end):
        check_threshold(V_membrane)
        Vmembrane=update_V_membrane(inputSpikeList[n],Vmembrane)
        
        #Fraction the time with the given gap constant
        n = n +1
        t = n * c
        
        Tsimulation_time=n
        Treal_time=t
        Tcurrent=time.time()
        Texecution_time=Tcurrent-Tstart
        
        print(Tsimulation_time)
        
        print(Treal_time)
        
        print(Texecution_time)
        
        


def main():
    inputSpikeList = [0,5,5,0,0,0,5]
    t_end = 3.5
    c = 0.5
    v_mem = update_V_membrane(5, -10)
    simulator(inputSpikeList, t_end, c)
    
if _name_ ==  "__main__":   
    main()