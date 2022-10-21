import pandas as pd
import matplotlib.pyplot as plt


# reading the database
data = pd.read_csv("Rainfall.csv")

# histogram of Annual Rainfall
plt.hist(data['ANNUAL'])

plt.title("Histogram")

# Adding the legends
plt.show()
