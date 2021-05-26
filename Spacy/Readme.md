# IMDb Movie Review
We have used movie reviews dataset by IMDb. What we have done is we created a classification model that looks at the review text and predicts whether a review is positive or negative.
Since this data set already includes whether a review is positive or negative in the feedback column, we can use those answers to train and test our model. 
Our goal here is to produce an accurate model that we could then use to process new user reviews and quickly determine whether they were positive or negative.


Dataset : https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

## Repository contains :
* **Python Notebook** : download it and run it in your code
  * Remember to install the following module <br><br>
  ``` 
  !conda install -c conda-forge spacy
  !python -m spacy download en
  ```

* **Pickle file** : it's a pre-trained model of your above notebook so , you can just download and load anywhere

``` 
import pickle
model = pickle.load(modelname)
print(model.predict(["Worst movie ever"])) 
```
