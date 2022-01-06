import csv
import numpy as np
import pandas as pd
from  matplotlib import pyplot as plt

#ages_x  = [20, 21, 22, 23, 24, 25, 26, 27, 28]

#dev_y = [30000, 20387, 25345, 29345, 41345, 27233, 26423, 34523, 37234]
 
#plt.plot(ages_x, dev_y)

#pl_dev_y = [40000, 30387, 35345, 39345, 51345, 37233, 36423, 44523, 47234]

#plt.plot(ages_x, pl_dev_y)
#plt.xlabel('Ages')
#plt.ylabel('Median Salary(USD)')
#plt.title('Median Salary (USD) by Age')
#plt.legend(['All Legends', 'Python'])
#plt.show()
with open('Voter_Registration_Data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    row = next(csv_reader)
    print(row)
#data = pd.read_csv('Voter_Registration_Data.csv')
#plt
#print(data)