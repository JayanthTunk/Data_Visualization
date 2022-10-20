import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Rainfall.csv")

# Bar chart with state against Annual Rainfall
plt.bar(data['STATE_UT_NAME'], data['ANNUAL'])

plt.title("Bar Chart")

# Setting the X and Y labels
plt.xlabel('Annual Rainfall')
plt.ylabel('State')

# Adding the legends
plt.show()
