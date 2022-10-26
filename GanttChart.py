import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load the dataset
df = pd.read_csv("Rainfall.csv")

fig, ax = plt.subplots(1, figsize=(16,6))
ax.barh(df.STATE_UT_NAME, df.ANNUAL, left=df.SEP)
plt.show()