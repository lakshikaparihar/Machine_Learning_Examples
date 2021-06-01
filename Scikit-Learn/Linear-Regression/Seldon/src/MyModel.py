import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

class MyModel(object):
    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """

    def __init__(self):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        print("Initializing.......")

        # Reading the data. Make sure to upload the csv file into Google Collaboratory for this to work. 
        # dataset = pd.read_csv('Salary_Data.csv') 
        dataset = pd.read_csv ('https://guneet-public-data.s3.ap-south-1.amazonaws.com/Salary_Data.csv');
        x = dataset.iloc[:, :-1].values   
        y = dataset.iloc[:, -1].values

        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split (x, y, test_size = 0.2, random_state = 1)

        # Create an instance of Linear Regression Model
        from sklearn.linear_model import LinearRegression
        self.regressor = LinearRegression ()

        # connect the model with dataset
        self.regressor.fit (x_train, y_train)

        print("Initialized")
    def predict(self, X, features_names=None):
        """
        Return a prediction.

        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        print("Predict called - will run identity function")
        y_predicted = self.regressor.predict (X)
        return y_predicted
