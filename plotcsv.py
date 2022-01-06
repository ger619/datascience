
from numpy import where
import pandas as pd
from  matplotlib import pyplot as plt

data = pd.read_csv('Dev_data.csv')
Age = data['Age']
All_Devs = data['All_Devs']
pythons_sal = data['Python']

overall_median = 57287 
#All_Republicans = data['Republican']
#All_Pacific_Green = data['Pacific Green']
#All_Independent_Party = data['Independent Party']

plt.plot(Age, All_Devs, color ="#444444", linestyle = '--', label = 'All_Developers')

plt.plot(Age, pythons_sal, label= 'Python')

plt.fill_between(Age, pythons_sal, overall_median, where = (pythons_sal > overall_median), interpolate= True, color="Magenta",alpha=0.25, label ="Äbove average" )

plt.fill_between(Age, pythons_sal, overall_median, where = (pythons_sal <= overall_median), interpolate= True, alpha=0.25, label ="Below Average")


plt.legend()
plt.title("Pie Chart Representation")
plt.tight_layout()
plt.show()