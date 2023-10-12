#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:39:31 2023

@author: lydiacrompton
"""

#EXERCISE 2: Neuron as a DTSS

#Write the algorithm of the neuron of lecture 1 as a DTSS model (with two functions for state transitions and outputs)
#Add a While loop to the simulator part of a DTSS model.


#1. Write the algorithm of the neuron of lecture 1 as a DTSS model (with two functions for state transitions and outputs)
#2. Add a While loop to the simulator part of a DTSS model.
#Simulate a neuron from t=0 to t=0.35 using a for loop. Take inputs during this interval and determine if neuron has spiked.

V_threshold = -65
V_membrane = 65
import sys

def update_V_membrane(spike_value, V_membrane):
    V_membrane += spike_value
    return V_membrane

def check_threshold(V_membrane):
    
    if V_membrane >= V_threshold:
        return 5
    else:
        return 0 

def simulator(spikeList, t_end, c):
    t = 0 
    #index of the input spike list is called n 
    n = 0 
    global V_membrane
    
    while(t < t_end):
        output_neuron = check_threshold(V_membrane)
        
        V_membrane = update_V_membrane(spikeList[n], V_membrane)
        
        print("t=", t, V_membrane, output_neuron)
        
        #Fraction the time with the given gap constant
        n = n +1
        t = n * c


def main():
    inputSpikeList = [0,5,5,0,0,0,5]
    t_end = 3.5
    c = 0.5
    v_mem = update_V_membrane(5, -10)
    simulator(inputSpikeList, t_end, c)
    
if _name_ ==  "__main__":   
    
    main()
    
    
    
    
    