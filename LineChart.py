import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Rainfall.csv")

plt.plot(data['STATE_UT_NAME'])
plt.plot(data['Jun-Sep'])
 
# Adding Title to the Plot
plt.title("Scatter Plot")
 
# Setting the X and Y labels
plt.xlabel('State')
plt.ylabel('Jun-Sep Rainfall')
 
plt.show()