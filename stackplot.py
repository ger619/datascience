import numpy as np
import pandas as pd
from  matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

Minutes = [1,2,3,4,5,6,7,8,9,10,]
David = [10,14,15,18,25,29,35,42,57,60]
Abol =  [13,16,19,25,25,29,36,40,59,62]
Ger =   [18,25,29,34,38,40,44,60,66,72]

label = ['David', 'Abol', 'Ger']

plt.stackplot(Minutes, David, Abol, Ger, labels = label)
plt.legend(loc="lower left")
plt.title("Stack Plot Representation")
plt.tight_layout()
plt.show()
