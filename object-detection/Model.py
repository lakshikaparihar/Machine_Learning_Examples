from imageai.Detection import ObjectDetection
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import json

class Model(object):
    def __init__(self):
        print("Initializing class .......")
        self.execution_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath( os.path.join(self.execution_path , "resnet50_coco_best_v2.1.0.h5"))
        self.detector.loadModel()
        print("Loading model..........")

    def predict(self,X,feature_name):
        self.detections = self.detector.detectObjectsFromImage(input_image=os.path.join(self.execution_path , X),output_image_path=os.path.join(self.execution_path , "output-image.jpg"))
        self.identity = dict()
        for eachObject in self.detections:
            self.identity[eachObject["name"]]=eachObject["percentage_probability"]
        json_object = json.dumps(self.identity)
        return json_object
