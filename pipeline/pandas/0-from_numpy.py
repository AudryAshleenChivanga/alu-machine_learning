#!/usr/bin/env python3

"""
    Function that creates a pd.DataFrame from a np.ndarray
"""
import pandas as pd


def from_numpy(array):
    columns = [chr(65 + i) for i in range(array.shape[1])]
    df = pd.DataFrame(array, columns=columns)
    return df