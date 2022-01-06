
import numpy as np
import pandas as pd
from  matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slice = [30,30,20,20]
labels = ["Thirty","Thirty", "Twenty", "Twenty"]
explode = [0, 0, 0.2, 0]
colors = ['blue','red','green', 'yellow'] #Can place hex colors

plt.pie(slice, labels = labels, colors=colors, explode=explode, shadow = True, startangle=90, autopct='%1.1f%%',wedgeprops={'edgecolor':'black'})
plt.title("Pie Chart Representation")
plt.tight_layout()
plt.show()