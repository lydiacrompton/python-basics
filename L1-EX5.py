#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:24:16 2023

@author: lydiacrompton
"""

#Exercise 5: Neuron with input weights

#Declare and add weight parameter to the code of file “neuron1.py” of exercise 4. 
#Receive this parameter value as an argument of the Main. Test different values 
#and add in a comment the membrane potential value for 2 different parameter values. 
#Add to the comment an explanation of what does it mean to change the parameter value
# of a neuron model.


## Define a function to update neuron membrane potential by input weights
def updateMembranePotential(V_mem, weight):
    inputSpike = 5 ##mV
    V_mem = V_mem + weight*inputSpike
    return(V_mem)

def main():
    ## Initialize neuron membrane potential in units milliVolts
    V_membrane = -75
    
    ## Use input function to take inputs from user
    weight=input("Provide the input weights for a spike of 5mV")
    
    ## Convert the input to float
    weight=int(weight)
    ## Call the function updateMembranePotential to update neuron membrane potential 
    V_mem=updateMembranePotential(V_membrane, weight)  
    print(V_mem)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()