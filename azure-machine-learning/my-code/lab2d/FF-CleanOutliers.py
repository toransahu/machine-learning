#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:54:30 2017

@author: toran
"""

# The script MUST contain a function named azureml_main
# which is the entry point for this module.
import pandas as pd

azure = False

# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1):
    
    
    dataframe1 = dataframe1[(dataframe1["FFMC"] > 40.0) & \
                            (dataframe1["ISI"] < 30.0) & \
                            (dataframe1["rain"] < 23.0)]

    # Return value must be of a sequence of pandas.DataFrame
    return dataframe1,

if (azure):
    pass
else:
    pass
# =============================================================================
#     
#     filename = 
#     dataframe = pd.read_csv()
# =============================================================================
