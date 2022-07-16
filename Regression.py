import pandas as pd
import numpy as np

data = pd.read_csv('ww-ii-data.csv')

# preprocessing

data = data.fillna(data.mean())
data = data.dropna(axis=1)

X = data[['STA', 'WindGustSpd', 'YR', 'MO', 'DA', 'SPD', 'MAX', 'MIN', 'MEA', 'SND', 'PGT', 'MeanTemp', 'MinTemp']]
y = data['MaxTemp']

# model 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x_train, x_test, y_train, y_test = train_test_split(X, y)
linear_model = LinearRegression()
linear_model.fit(x_train, y_train)

prediction = linear_model.predict(x_test)

# evaluate

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

print(mean_absolute_error(y_test, prediction))
print(r2_score(y_test, prediction))