import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Rainfall.csv")
 
# Scatter plot with STATE_UT_NAME against ANNUAL
plt.scatter(data['STATE_UT_NAME'], data['ANNUAL'])
 
# Adding Title to the Plot
plt.title("Scatter Plot")
 
# Setting the X and Y labels
plt.xlabel('STATE_UT_NAME')
plt.ylabel('ANNUAL')
 
plt.show()