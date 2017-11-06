#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:08:43 2017

@author: toran
"""

def round2(df):
    """Round upto 2 decimal."""
    import numpy as np
    return df.apply(lambda x: np.round(x,2))