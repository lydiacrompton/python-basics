#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:37:48 2023

@author: lydiacrompton
"""

#EXERCISE 1: Seperate model and simulator
   
# Write on the notebook the algorithm of the neuron implemented in exercise 6 of Lecture 1 using Main and Functions as described in previous slides
# Add a parameter to previous algo/code
#  For next exercises, write the algorithm and after the code



#1. Code a new method Simulate() taking in argument the method of exercise 4 and returning the new membrane potential value
#2. Code a new method computing a new membrane potential value, differ- ently from the one in exercise 4
#3. Make Simulate() method call the first method
#4. Make Simulate() method call the second method



# Initialise variables:
Vrest =-70
Vmembrane=Vrest 
int spike=0

def UpdateMemPotential1 (Vmembrane):#method 1
    global spike
   spike=float(input("enter input1: "))
    Vmembrane += spike
    return Vmembrane


def UpdateMemPotential2(Vmembrane,Input): #method 2
   Vmembrane<-Input
    return Vmembrane


def Simulate (method, Input): #function simulate based on the selected method
    global Vmembrane
    if method==1 then:
        Vmembrane=UpdateMemPotential1(Vmembrane)
        else:
            Vmembrane=UpdateMemPotential2(Vmembrane,Input)
            return Vmembrane
        
# Main function
def main():
    method=int(input("Enter method (1 or 2:) "))
    input1=float(input("Enter input 1:"))
    Vmembrane=Simulate(method,input1)
    print("Vmembrane:", Vmembrane)
    
if __name__="__main__":
    main()
    
    
