#!/usr/bin/env python3
"""
 pyhton script that create a pd.DataFrame from a Dictionary
"""
import pandas as pd


data = {'First': [0.0, 0.5, 1.0, 1.5],
        'Second': ['one', 'two', 'three', 'four']}

row = ['A', 'B', 'C', 'D']

df = pd.DataFrame(data, index=row)