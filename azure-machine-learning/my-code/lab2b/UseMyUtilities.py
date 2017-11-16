#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:22:31 2017

@author: toran
"""

def azureml_main(frame1):
    import MyUtilities as mu
    
    numCols = ["Cottagecheese.Prod", "Icecream.Prod", "Milk.Prod", "Total.Prod"] 
# call round2() from myutilities module    
    frame1[numCols] = frame1[numCols].apply(mu.round2) 
    return frame1