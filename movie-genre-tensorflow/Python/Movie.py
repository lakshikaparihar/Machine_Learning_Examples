from tensorflow.keras.models import load_model
import utils
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import pandas as pd

class Movie(object):
  def __init__(self):
    self.model=load_model("./model.h5")
    print("Model initialized.............")

  def predict(self,X,feature_names):
    print("Entering prediction........")
    img = utils.cleansing(X)
    df = pd.read_csv('train.csv')
    classes = np.array(df.columns[2:])
    print("predicting..............")
    proba = self.model.predict(img)
    print("Got the top 3 genre.............")
    top3=np.argsort(proba[0])[:-4:-1]
    print("creating json...........")
    genre=dict()
    for i in range(3):
      genre[classes[top3[i]]] = proba[0][top3[i]]
    return genre
