# Support Vector Regression (SVR)

# Importing the libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.compose import TransformedTargetRegressor


# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
y = y.reshape(len(y),1)

# Feature Scaling
regressor = SVR(kernel = 'rbf')
pipeline = Pipeline(steps=[('Scaling', StandardScaler()), ('model',regressor)])
model = TransformedTargetRegressor(regressor=pipeline, transformer=StandardScaler())


# Training the SVR model on the whole dataset
model.fit(X,y)

# Predicting the result
print(model.predict([[6.5]]))

# Saving the model
import pickle
pickle.dump(model,open('SVR.pkl',"wb"))
