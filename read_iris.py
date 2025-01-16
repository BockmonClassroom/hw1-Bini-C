# Author: Bini Chandra
# Date: 01/15/2025
# This python file reads in the Iris.csv data set and prints each line of the data set.


# Import the pandas library
import pandas as pd

# Define the relative path of the Iris.csv file
path = './data/Iris.csv'

# Read the csv file into a dataframe
df = pd.read_csv(path)

# Iterate through each row of the dataframe and print it
for row in df.values:
    print(' ,'.join(map(str, row)))