# function which displays the missing values in a dataset attribute wise
import pandas as pd
import numpy as np

dataset = pd.read_csv(".....csv")

def miss_val(data):
    if dataset.isnull().values.any():
       miss = (data.isnull().sum().sort_values(ascending=False))
       return miss
    else: print('There are no missing values in the Dataset')
    

#function show the number of unique values column wise
miss_val(dataset)

# num -> is the number of unique observations to be displayed

def unique(data,num):
    for c in list(data.columns):
        n = data[c].unique()
        if len(n)<= num:
           print(c)
           print(n)
        else:
           print(c + ': ' +str(len(n)) + ' unique values')

unique(dataset,5)


