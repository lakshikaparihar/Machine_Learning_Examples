# K-Nearest Neighbors (K-NN)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


# Feature Scaling and creating model
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline

classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
pipeline = Pipeline(steps=[('Scaling', StandardScaler()), ('model',classifier)])
pipeline.fit(X_train,y_train)


# Predicting a new result
print(classifier.predict([[30,87000]]))

# Predicting the Test set results
y_pred = pipeline.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

# Saving the model
import pickle
pickle.dump(pipeline,open('KNN.pkl',"wb"))
