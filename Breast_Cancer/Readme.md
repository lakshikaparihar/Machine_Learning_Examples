* Algorithm Used : Logistic Regression
* Library Used : Scikit-learn
* Dataset Used from UCI Machine Learning Repository

---
## Dataset details

No. of instances : 699<br>
Total Attribute : 10 <br>
Independent Variable : 9 <br>
Dependent Variable : 1 <br>
Missing Value : NO

**Note**:  2 for Benign, 4 for Malignan

---

## Model Save and export

```
 import pickle
 pickle.save(open("model.pkl","wb"),classifier)
```

You will get a file model.pkl after that and you can use it anywhere you wanted

---

## Model Load

```
model = pickle.load(open("model.pkl","rb"))
```
  