import pandas as pd
import numpy as np

def get_column_array(df, column):
    expected_length = len(df)
    current_array = df[column].dropna().values
    if len(current_array) < expected_length:
        current_array = np.append(current_array, [''] * (expected_length - len(current_array)))
    return current_array

def create_Unique_Dict(cat_X,cat_Y):
    newDF_X = cat_X.sort_values(cat_X.columns.tolist()).reset_index(drop=True).apply(lambda x: x.drop_duplicates())
    newDF_Y = cat_Y.sort_values(cat_Y.columns.tolist()).reset_index(drop=True).apply(lambda x: x.drop_duplicates())
    for column in newDF_X.columns:
        newDF_X[column] = get_column_array(newDF_X, column)
    for column in newDF_Y.columns:
        newDF_Y[column] = get_column_array(newDF_Y, column)
    return newDF_X , newDF_Y