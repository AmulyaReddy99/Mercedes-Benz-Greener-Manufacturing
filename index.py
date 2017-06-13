import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

style.use('ggplot')
sns.set(style = 'white')


# ##### Overview Analysis
data = pd.read_csv('./input/train.csv')
print data.head()

# ### For Finding Outlier
plt.figure(figsize = (8,6))
plt.scatter(data['ID'], data['y'])
plt.xlabel('ID')
plt.ylabel('Time for testing')
plt.show()


# ##### Combined Data
# def get_combined():

# 	train = pd.read_csv('./input/train.csv')
# 	test = pd.read_csv('./input/test.csv')

# 	y = train['y']
# 	train.drop('y', axis = 1, inplace = True)

# 	combined = train.append(test, ignore_index = True)

# 	return combined
# 	# print train.shape, test.shape
# 	# print train.head()
# 	# print test.head()


# combined = get_combined()
# # print combined.shape
# print combined.head()



