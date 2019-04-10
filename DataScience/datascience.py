import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()
height = [1.73,1.63,1.71,1.89, 1.50]
np_height = np.array(height)
weight = [65.4, 59.2, 63, 88, 59]
np_weight = np.array(weight)
print(np_height)
print(np_weight)
meanheight = np.mean(np_height)
medheight = np.median(np_height)
bmi = np_weight/np_height ** 2
print(bmi>23)

np_2d = np.array([[1.73,1.63,1.71,1.89, 1.50],[65.4, 59.2, 63, 88, 59]])
print ('This shows us the shape of the string',  np_2d.shape)
print ('This show the first element on the second index',  np_2d[0,2],np_2d[0][2])
print ('This shows the first and second element',  np_2d[:,1:3])
print ('This shows weight of all family members',  np_2d[1:])
print ('This shows mean weight', meanheight)
print ('This shows median weight', medheight)


df_swing = pd.read_csv('Voter_Registration_Data.csv')
df_swing[['HD_CODE', 'HD_NAME', 'COUNT(V.ID)', 'PARTY']]
print ('This shows output', df_swing)

#This will display a histogram
_ = plt.hist(df_swing['PARTY'])
_ = plt.xlabel('asd')
_ = plt.ylabel('dfasd')
plt.show()

#This will display a line graph
x = np.sort(df_swing["COUNT(V.ID)"])
y = np.arange(1, len(x)+1) /len(x)
plt.plot(x,y, marker='.',linestyle='none')
_ = plt.xlabel('asd')
_ = plt.ylabel('dfasd')
plt.margins(0.02)
plt.show()

