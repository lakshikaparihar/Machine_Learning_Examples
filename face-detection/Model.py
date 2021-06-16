import requests
import face_recognition
import urllib.request

class Model(object):
    def __init__(self):
        print("Initializing class .......")
        print("Loading model..........")

    def predict(self,X,feature_name):
        response = urllib.request.urlopen(X[0])
        image = face_recognition.load_image_file(response)
        face_locations = face_recognition.face_locations(image)
        return face_locations
