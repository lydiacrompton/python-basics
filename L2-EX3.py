#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:44:57 2023

@author: lydiacrompton
"""

#EXERCISE 3:Neuron as DTSS with For loop

    
#Replace simulator While loop by a For loop of a DTSS model.

# Simulate a neuron from t=0 to t=5 using a for loop. Take inputs during this interval and determine if neuron has spiked.

V_threshold = -65
V_membrane = -75
V_rest = -75

def delta(input, V_mem):#update v membrane
    V_mem = V_mem + input
    return(V_mem)

def lambda_dtss(V_mem): #check threshold
    
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
    for n in range(int(t_end/c)+1):
        output_neuron = lambda_dtss(V_membrane)
        V_membrane = delta(inputSpikeList[n],V_membrane)
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