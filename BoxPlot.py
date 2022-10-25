# import the required library 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
  
  
# load the dataset
df = pd.read_csv("Rainfall.csv")
  
df.boxplot(by ='STATE_UT_NAME', column =['ANNUAL'], grid = False)
plt.ylabel('Annual Rainfall')
plt.xlabel('State')
plt.show()