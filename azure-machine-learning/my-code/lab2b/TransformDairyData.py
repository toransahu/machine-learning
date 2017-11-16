#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 20:23:58 2017

@author: toran
"""

def azureml_main(frame1):
    import pandas as pd
    import os.path
    
# set flag to change env
    azure = True
# pick file from local & create frame1    
    if(azure == False):
        repopath = "/mnt/ExternalHDD/E/workspace/machine-learning/azure-machine-learning"
        labfile = "/lab-scripts/Lab02B/cadairydata.csv"
        path = repopath + labfile
        frame1 = pd.read_csv(path)
        
# select subset of columns
    frame1 = frame1[["Year", "Month", "Cottagecheese.Prod", "Icecream.Prod", "Milk.Prod"]]
    
# filter data for month Aug
    frame1 = frame1[frame1['Month']=='Aug']

# add a column to show total of Aug
    frame1["Total.Prod"] = frame1["Cottagecheese.Prod"] + \
                            frame1["Icecream.Prod"] + \
                            frame1["Milk.Prod"]
    return frame1