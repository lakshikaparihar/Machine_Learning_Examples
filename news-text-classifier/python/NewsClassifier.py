import pickle

from main_working import main_working

class NewsClassifier(object):
    def __init__(self):
        self.predictions= main_working()
        print("Initialzing the class")
        self.loaded_model = pickle.load(open("model.pkl", 'rb'))
        self.loaded_transformer = pickle.load(open("transformer.pkl", 'rb'))
        print("Loading model")

    def predict(self, X , feature_names):
        print("In the prediction..")
        test_features = self.loaded_transformer.transform(X)
        s = self.loaded_model
        prediction = self.predictions.get_top_k_predictions(s,test_features,2)
        print("Predicting......")
        return prediction

