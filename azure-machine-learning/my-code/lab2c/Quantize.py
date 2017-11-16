#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 22:38:26 2017

@author: toran
"""

def azureml_main(frame1):
    """Quantize the wind column using 4 bins & make new column."""
    import pandas as pd
    bins = [0, 2.5, 5, 7.5, 10]
    frame1['wind_cat'] = pd.cut(frame1['wind'], bins)
    return frame1