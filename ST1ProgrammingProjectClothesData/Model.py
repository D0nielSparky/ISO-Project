# Importing all libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Importing dataframe from file
clothes_data = pd.read_csv("clothesData.csv")

# Use numpy to convert to arrays
# Labels are the values we want to predict
labels = np.array(clothes_data['Price'])

# Remove the labels from the clothesData
# axis 1 refers to the columns
clothesData = clothes_data.drop('Price', axis=1)
# Saving feature names for later use
clothes_list = list(clothesData.columns)
# Convert to numpy array
clothesData = np.array(clothesData)

# Using Skicit-learn to split data into training and testing sets
# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(clothesData, labels, test_size=None,
                                                                            random_state=42)

print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)

# The baseline predictions are the historical averages
baseline_preds = test_features[:, clothes_list.index('Brand')]
# Baseline errors, and display average baseline error
baseline_errors = abs(baseline_preds - test_labels)
print('Average baseline error: ', round(np.mean(baseline_errors), 2))

# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators=1000, random_state=42)
# Train the model on training data
rf.fit(train_features, train_labels)

# Use the forest's predict method on the test data
predictions = rf.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
