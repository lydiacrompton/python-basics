#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:46:35 2023

@author: lydiacrompton
"""

#EXERICSE 4: Neuron using euler method

#Write the algorithm of a Euler method discretize the membrane potential differential equation.
#What is the DTSS model?
#What is the link with the simulator?


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