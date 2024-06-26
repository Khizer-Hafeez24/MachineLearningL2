# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yWLoeptf2rxtNkIQWjrCl4oTVMJ8VhNX
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Step 1: Load CSV file into a pandas DataFrame
data = pd.read_csv('/content/vehicle_data.csv')  # Assuming your CSV file has 10,000 records

# Step 2: Data Preprocessing
# Example: Convert categorical variables (like 'color') into numerical values using one-hot encoding
data = pd.get_dummies(data, columns=['color'])

# Step 4: Split data into features and target variable
X = data.drop('vehicle_type', axis=1)
y = data['vehicle_type']

# Step 5: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Model Selection and Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 7: Predicting and printing the vehicle type
def predict_vehicle(features):
    # Assuming 'features' is a dictionary containing values for weight, height, color, and number of wheels
    # Convert the dictionary to a DataFrame with a single row and the same columns as X_train
    features_df = pd.DataFrame([features])
    # Perform one-hot encoding for color if necessary
    if 'color' in features_df.columns:
        features_df = pd.get_dummies(features_df, columns=['color'])
        # Realign the columns to match the training data
        features_df = features_df.reindex(columns=X_train.columns, fill_value=0)
    prediction = model.predict(features_df)[0]
    if prediction == 'car':
        print("It's a car.")
    elif prediction == 'bike':
        print("It's a bike.")
    else:
        print("Unknown vehicle type.")

# Example usage:
features = {'weight': 1500, 'height': 140, 'color': 'red', 'no_of_wheels': 4}
predict_vehicle(features)
