# Random Forest Regression

# Importing the libraries
import pandas as pd
import pickle

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Training the Random Forest Regression model on the whole dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X, y)

# Predicting a new result
regressor.predict([[6.5]])

#saving the model
pickle.dump(regressor,open("sklearn_Random_Forest_Regression_salary_prediction.pkl","wb"))