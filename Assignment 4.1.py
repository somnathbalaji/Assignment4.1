
# coding: utf-8

# @author: Somnath Balaji
# # You survey households in your area to find the average rent they are paying. Find the standard deviation from the following data:
# # $1550, $1700, $900, $850, $1000, $950.

# In[5]:


# Importing the libraries required
import pandas as pd
import numpy as np
import statistics

# Creating a list from the given data
l=['$1550', '$1700', '$900', '$850','$1000','$950']

# Creating another list to replace dollar symbol and looping it with previous list
m=[int(s.replace('$','')) for s in l ]

# Printing the value by calculating the mean and standard deviation
print("Average Rent to be Paid:",statistics.mean(m))
print("Standard Deviation of the Data:",statistics.stdev(m))

