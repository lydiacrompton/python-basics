#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:31:53 2023

@author: lydiacrompton
"""

#EXERCISE 4: NEURON WITH INPUT SPIKES


#In a file called “neuron1.py”: Remake previous exercise with a method to compute the new membrane potential value taking in argument a single spike value and returning the new membrane potential value.
#Copy/paste the content of file “neuron1.py” to another file “neuron2.py“
#Use command line to run: py neuron1.py 1.0| py neuron2.py
#“neuron2.py” should be able to read the output of “neuron1.py” and use it as input to update the membrane potential. What is the error?


## Define a function to update neuron membrane potential by 1 millivolt
def updateMembranePotential(V_mem, inputSpike):
    V_mem = V_mem + inputSpike
    return(V_mem)

def main():
    ## Initialize neuron membrane potential in units milliVolts
    V_membrane = -75
    ## Use input function to take inputs from user
    spike=input("Provide the input spike value in milliVolts")
    ## Convert the input to float
    spike=int(spike)
    ## Call the function updateMembranePotential to update neuron membrane potential 
    V_mem = updateMembranePotential(V_membrane, spike)
    print(V_mem)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
