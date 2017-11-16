#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:31:41 2017

@author: toran
"""

# The script MUST contain a function named azureml_main
# which is the entry point for this module.


# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1):
    import matplotlib 
    matplotlib.use('agg')
    
    import pandas as pd
    import matplotlib.pyplot as plt
    from pandas.tools.plotting import scatter_matrix
    
    ## remove unwanted column
    ### cause they are string values
    ### axis=1 means we are droping columns not row
    ### inplace=true means we're not making copy of dataframe (Good Practice)
    dataframe1.drop(["X","Y", "month", "day"], axis=1, inplace=True)
    
    ## Create a scatter plot matrix
    fig1 = plt.figure(1, figsize =(12,9))
    ax = fig1.gca()
    scatter_matrix(dataframe1, alpha=0.2, figsize=(10,10), diagonal='kde', ax=ax)
    fig1.savefig('scatter2.png')
    
    return dataframe1,
