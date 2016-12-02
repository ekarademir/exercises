import pandas as pd, numpy as np, matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

# Load the train set
traindf = pd.read_csv("train.csv")
traindf.set_index(["PassengerId"])

print(traindf.head(2))
# print(traindf.describe())
print(traindf.mean())
print(traindf.columns)


traindf["Age"]
plt.show()
