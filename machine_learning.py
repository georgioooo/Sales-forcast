import pandas as pd
from correlation_code import history_itemA, history_itemB, bordeaux_weather
import sklearn
from sklearn import linear_model
import numpy as np

forecast_reduction = pd.read_csv('forecast_reduction.csv')


# dictionary contain features of forecast dataframe with sales of items A and B
dic = dict(MAX_TEMPERATURE_C=bordeaux_weather.MAX_TEMPERATURE_C,
           MIN_TEMPERATURE_C=bordeaux_weather.MIN_TEMPERATURE_C,
           PRECIP_TOTAL_DAY_MM=bordeaux_weather.PRECIP_TOTAL_DAY_MM,
           HUMIDITY_MAX_PERCENT=bordeaux_weather.HUMIDITY_MAX_PERCENT,
           CLOUDCOVER_AVG_PERCENT=bordeaux_weather.CLOUDCOVER_AVG_PERCENT,
           Sales_A_Bordeaux=history_itemA.SALES,
           Sales_B_Bordeaux=history_itemB.SALES
           )


# A dataframe contain features of forecast dataframe with sales of items A and B
df = pd.DataFrame(data=dic)


x = np.array(df.drop(['Sales_A_Bordeaux', 'Sales_B_Bordeaux'], axis=1))
A = np.array(df['Sales_A_Bordeaux'])
B = np.array(df['Sales_B_Bordeaux'])


x_train_A, x_test_A, Y_train_A, Y_test_A = sklearn.model_selection.train_test_split(x, A, test_size=0.1)
x_train_B, x_test_B, Y_train_B, y_test_B = sklearn.model_selection.train_test_split(x, B, test_size=0.1)
z = linear_model.LinearRegression()


# applying linear regression for item A
z_itemA = z.fit(x_train_A, Y_train_A)
accuracy_itemA = z.score(x_test_A, Y_test_A)
prediction_itemA = z_itemA.predict(forecast_reduction.drop(['DATE'], axis=1))
print('the accuracy prediction of the item A for the 7 days in june is:', accuracy_itemA)
print('the prediction sales for this 7 days in june is:', prediction_itemA)
print(sum(prediction_itemA))


# applying linear regression for item B
z_itemB = z.fit(x_train_B, Y_train_B)
accuracy_itemB = z.score(x_test_B, y_test_B)
prediction_itemB = z_itemB.predict(forecast_reduction.drop(['DATE'], axis=1))
print('the accuracy prediction of the item B for the 7 days in june is:', accuracy_itemB)
print('the prediction sales for this 7 days in june is:', prediction_itemB)
print(sum(prediction_itemB))
