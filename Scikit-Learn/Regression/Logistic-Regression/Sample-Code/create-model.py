import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)

print ('\nData: ')
print (dataframe)


X = dataframe.iloc[:, 0:8].values
Y = dataframe.iloc[:, -1].values

print ('X')
print (X)

print ('Y')
print (Y)


test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)


# Fit the model on training set
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

filename = 'finalized_model.pkl'
pickle.dump(model, open(filename, 'wb'))
print ('Model File Created...')

