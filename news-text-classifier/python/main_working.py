import numpy as np

class main_working():

    def get_top_k_predictions(self,model,X_test,k):

        # get probabilities instead of predicted labels, since we want to collect top 3
        probs = model.predict_proba(X_test)

        # GET TOP K PREDICTIONS BY PROB - note these are just index
        best_n = np.argsort(probs, axis=1)[:,-k:]

        # GET CATEGORY OF PREDICTIONS
        preds=[[model.classes_[predicted_cat] for predicted_cat in prediction] for prediction in best_n]

        preds=[ item[::-1] for item in preds]

        return preds
   