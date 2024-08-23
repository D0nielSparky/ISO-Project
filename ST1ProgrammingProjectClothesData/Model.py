# Importing all libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeRegressor

# Importing dataframe from file
clothes_data = pd.read_csv("clothesData.csv")

# Use numpy to convert to arrays
# Labels are the values we want to predict
clothesDataNumeric = pd.get_dummies(clothes_data, columns=['Brand', 'Category', 'Color', 'Size', 'Material'])

CategoricalPredictorList = clothesDataNumeric.columns.tolist()
CategoricalPredictorList.remove('Price')

TargetVariable = 'Price'

X = clothesDataNumeric[CategoricalPredictorList].values
y = clothesDataNumeric[TargetVariable].values

# Standardization of data
PredictorScaler = MinMaxScaler()
# Storing the fit object for later reference
PredictorScalerFit = PredictorScaler.fit(X)
# Generating the standardized values of X
X = PredictorScalerFit.transform(X)

dtree = DecisionTreeRegressor()
dtree.fit(X, y)

