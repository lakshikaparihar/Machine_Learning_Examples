from Movie import Movie
from tensorflow.keras.preprocessing import image
img = image.load_img('golmal.jpeg',target_size=(350,350,3))
print(Movie().predict(img,["feature_name"]))
