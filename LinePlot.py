
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
 
 
# reading the database
data = pd.read_csv("Rainfall.csv")
 
sns.lineplot(x='STATE_UT_NAME', y='ANNUAL', data=data)

# Setting the X and Y labels
plt.ylabel('Annual Rainfall')
plt.xlabel('State')

plt.show()