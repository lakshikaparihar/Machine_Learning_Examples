# Decision Tree Regression

# Importing the libraries
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeRegressor

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Training the Decision Tree Regression model on the whole dataset
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

# Predicting a new result
print(regressor.predict([[6.5]]))

# Saving the model
pickle.dump(regressor,open("Sklearn-Decision-Tree-Regression","wb"))