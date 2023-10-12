#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:32:30 2023

@author: lydiacrompton
"""

#EXERCISE 6: Separate neuron model and simulator
    
#1 Code a new method Simulate() taking in argument the method of exercise 4 and returning the new membrane potential value
#2 Code a new method computing a new membrane potential value, differently from the one in exercise 4
#3 Make Simulate() method call the first method
#4 Make Simulate() method call the second method. Add a comment explaining what you are doing in terms of models and simulator.


## Define a function to update neuron membrane potential by 1 millivolt
def updateMembranePotential1(V_mem, inputSpike):
    print("Inside updateMembranePotential1")
    V_mem = V_mem + inputSpike
    return(V_mem)

## Define a function to update neuron membrane potential by input weights
def updateMembranePotential2(V_mem, weight):
    print("Inside updateMembranePotential2")
    inputSpike = 5 ##mV
    V_mem = V_mem + weight*inputSpike
    return(V_mem)

## Define a function to simulate neuron behaviour
def simulate(V_mem, model,weight=0, inputSpike=0):
    if(model == 1):
        V_mem=updateMembranePotential1(V_mem, inputSpike)
    else:
        V_mem=updateMembranePotential2(V_mem, weight)
    return(V_mem)    

def main():
    ## Initialize neuron membrane potential in units milliVolts
    V_membrane = -75
    
    ## Use input function to take inputs from user
    spike=input("Provide the input spike value in milliVolts")
    
    ## Convert the input to float
    spike=int(spike)
    ## Call simulate to execute model1 of neuron update
    V_mem=simulate(V_membrane,model=1, inputSpike=spike)
    print(V_mem)
    
    ## Use input function to take inputs from user
    weight=input("Provide the input weights for a spike of 5mV")
    ## Convert the input to float
    weight=int(weight)
    ## Call the function updateMembranePotential to update neuron membrane potential 
    V_mem=simulate(V_membrane, model=2, weight=weight)
    print(V_mem)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
  
  import sys
print (sys.path)
    