#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:47:50 2023

@author: lydiacrompton
"""

#EXERCISE 5: Network of two interacting neurons as functions
    
    
#Consider a network of two interacting neurons as functions Apply the programming cycle method
#Step 1: write what is/are: the problem, sub-problems, solution, order of execution
#Step 2: implementation
#Step 3: Verification, did you find a bug, which one/s? Step 4: Is the program valid? If yes/no, say why?


#1. Consider a network of two interacting neurons as functions
#Simulate a neuron from t=0 to t=0.35 using a for loop. Take inputs during this interval and determine if neuron has spiked.


V_threshold = -65
V_membrane = -75
V_rest = -75
R_m = 5
tau_m = 0.5

def delta(input, V_mem, dt):#update membrane potential
    V_mem = V_mem + dt*(V_rest - V_mem+ (R_m*input))/tau_m
    return(V_mem)

def lambda_dtss(V_mem):#check threshold
    
    if(V_mem >= V_threshold):
        global V_membrane
        V_membrane = V_rest
        return(5)
    else:
        return(0)

## Define a function to simulate neuron behaviour
def simulate(inputSpikeList,t_end,c):
    t=0
    n=0
    global V_membrane
    for n in range(int(t_end/c)):
        output_neuron = lambda_dtss(V_membrane)
        V_membrane = delta(inputSpikeList[n],V_membrane,c)
        #print("V_membrane=",V_membrane)
        print("t=",t,V_membrane,output_neuron)
        n=n+1
        t=n*c
        #print("n=",n,"t=",t)
    return(V_membrane)    

def main():
    inputSpikeList = [0,5,5,0,0,0,0,5]
    t_end = 3.5
    c = 0.5
    simulate(inputSpikeList,t_end,c)
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
  
  
  
  