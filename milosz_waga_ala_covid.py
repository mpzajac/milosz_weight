import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.colors import ListedColormap
import pandas as pd
from datetime import datetime

_data=pd.read_csv('data_waga.in', delimiter=';', usecols=['Date','Weight'], ))
print(_data.head())
_data.plot(figsize=(7,7))
plt.plot(date2num(
plt.grid()
plt.show()

        #dtype="str", usecols=[0])
#_data = [datetime.strptime(d, '%Y-%m-%dT%H%M') for d in _dataRAW]
#_waga = np.loadtxt('data_waga.in', delimiter=';', dtype="float", usecols=[1])
#date = _waga[:,0]
#weight = _waga[:,1]
#nutrition_comment = _waga[:,2]
#defecation_comment = _waga[:,3]
#_comments_def = np.genfromtxt('data_comments_defecation.in', delimiter=';')
#_comments_nutrition = np.genfromtxt('data_comments_nutrition.in', delimiter=';')

#print(_waga)

#slope, intercept, r_value, p_value, std_err = stats.linregress(_data, _waga)
#plt.plot(_data, _waga, 'o', label='original data')
#plt.plot(_data, intercept + slope*_data, 'r', label='fitted line')
#plt.legend()
#plt.show()
