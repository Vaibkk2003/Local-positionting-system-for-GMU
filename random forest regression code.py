--import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Importing the dataset
dataset = pd.read_csv('local_positioning_data.csv'
# Features matrix (X) and target vector (y)
X = dataset.iloc[:, :-1].values  # All columns except the last one ("position")
y = dataset.iloc[:, -1].values   # Last column as the target variable ("position")

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training the Random Forest Regression model on the training set
regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(X_train, y_train)

# Predicting results on the test set
y_pred = regressor.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared Score: {r2}")

# Predicting a new result (example data)
new_data = np.array([[55, 56, 57, 176, 177, 178, 1000, 1800, 830, 430]])  # Example values
new_prediction = regressor.predict(new_data)
print(f"Predicted Position for new data: {new_prediction[0]}")

# Visualizing the Random Forest Regression results
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], y, color='red', label='Actual Data')
plt.scatter(X_test[:, 0], y_pred, color='blue', label='Predicted Data')
plt.title('Random Forest Regression Results')
plt.xlabel('RSSI Value')
plt.ylabel('Position')
plt.legend()
plt.show()