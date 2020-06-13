import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.axes as axes

import pandas as pd
import datetime
import matplotlib.font_manager as fm

_data=pd.read_csv('data_waga.in', delimiter=';', 
        usecols=['Date','Weight'],
        parse_dates=['Date'],infer_datetime_format=True)
        
_datesNum = mdates.date2num(_data.iloc[:, 0].values.reshape(-1, 1))
_dataWeight = _data.iloc[:, 1].values.reshape(-1, 1)

_6month = datetime.datetime.fromisoformat('2020-07-07') 
_6month_num = mdates.date2num(_6month)
print("_6month: ", _6month)
print("_6month_num: ", _6month_num)

today = datetime.datetime.now()
MAX_RANGE = 7
DAYS_FRAME = 7
_dayLast = []
_dayFirst = []
_dataFirstToLast = []
_daysFirstToLastNum = []
_daysFirstToLastWeight = []
_daysFirstToLastNum1dim = []
_daysFirstToLastWeight1dim = []
_linearRegressionFirstToLast = []
_linearRegressionFirstToLastPolynomial =[]
_linearRegressionFirstToLastLinearSpace = []
_linearRegressionFirstToLastLinearSpaceDatesDateformat = []
_dateLabels = []
cmap='RdPu'
colors = plt.cm.RdPu_r(np.linspace(0, 0.5, MAX_RANGE))
for i in range(MAX_RANGE):
    _dayLast.append(datetime.datetime.now() - datetime.timedelta(days = i))
    _dayFirst.append(_dayLast[i] - datetime.timedelta(days = DAYS_FRAME))
    # _dayFirstNum = mdates.date2num(_dayFirst)
    # _dayLastNum = mdates.date2num(_dayLast)
    _dataFirstToLast.append((_data['Date'] > _dayFirst[i]) & (_data['Date'] < _dayLast[i]))
    _daysFirstToLastNum.append(mdates.date2num(_data[_dataFirstToLast[i]].iloc[:, 0].values.reshape(-1, 1)))
    _labelString = ""
    print(_dayFirst[i].strftime("%Y-%m-%d"))
    print(_dayLast[i].strftime("%Y-%m-%d"))
    _labels = ("Estymacja od " , _dayFirst[i].strftime("%Y-%m-%d"), ' do ', _dayLast[i].strftime("%Y-%m-%d"))
    _dateLabels.append(_labelString.join(_labels))
    _daysFirstToLastWeight.append(_data[_dataFirstToLast[i]].iloc[:, 1].values.reshape(-1, 1))
    _daysFirstToLastNum1dim.append(_daysFirstToLastNum[i][:,0])
    _daysFirstToLastWeight1dim.append(_daysFirstToLastWeight[i][:,0])
    _linearRegressionFirstToLast.append(np.polyfit(_daysFirstToLastNum1dim[i], _daysFirstToLastWeight1dim[i], 1))
    _linearRegressionFirstToLastPolynomial.append(np.poly1d(_linearRegressionFirstToLast[i]))
    _linearRegressionFirstToLastLinearSpace.append(np.linspace(_daysFirstToLastNum1dim[i].min(), _6month_num, 100))
    _linearRegressionFirstToLastLinearSpaceDatesDateformat.append(mdates.num2date(_linearRegressionFirstToLastLinearSpace[i]))
    plt.plot_date(_linearRegressionFirstToLastLinearSpaceDatesDateformat[i],
        _linearRegressionFirstToLastPolynomial[i](_linearRegressionFirstToLastLinearSpace[i]),
        '-', linewidth=1, label=_dateLabels[i], color=colors[i])
    print("i= ", i, ", _dateLabels[i] = ", _dateLabels[i])

birth_weight = _dataWeight[0][0]
target_weight = 2*birth_weight

_datesNum1d = _datesNum[:,0]
_dataWeight1d = _dataWeight[:,0]
_dataFit = np.polyfit(_datesNum1d, _dataWeight1d, 2)
print("_dataFit: ", _dataFit)
_dataFitPoly = np.poly1d(_dataFit)
print("_dataFitPoly: ", _dataFitPoly)
_datesNumLinSpace = np.linspace(_datesNum1d.min(), _6month_num, 100)
_datesNum2Dates = mdates.num2date(_datesNumLinSpace)

plt.plot_date(_datesNum2Dates, _dataFitPoly(_datesNumLinSpace), '-', color='orange', label='Estymacja kwadratowa po całości danych')
plt.scatter(_datesNum1d,_dataWeight1d, color='steelblue', label = 'Dane')

plt.axhline(y=target_weight, xmin=0.0, xmax=1.0, color='r', label = 'Podwojona waga urodzeniowa')

heading_font = fm.FontProperties(fname='gfx/PlayfairDisplay-Italic.ttf', size=22)
legend_font = fm.FontProperties()
legend_font.set_name('Helvetica')

plt.grid()
plt.legend(prop=legend_font,loc='best')
plt.suptitle("Waga Miłosza w kolejnych dniach", fontsize=16, fontproperties=heading_font)

plt.show()

quit()


