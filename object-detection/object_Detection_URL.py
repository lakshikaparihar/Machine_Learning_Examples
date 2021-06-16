from imageai.Detection import ObjectDetection
import os
import json
from skimage import io
from numpy import asarray
from PIL import Image
import requests

class object_Detection_URL(object):
    def __init__(self):
        print("Initializing class .......")
        self.execution_path = os.getcwd()
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath( os.path.join(self.execution_path , "resnet50_coco_best_v2.1.0.h5"))
        self.detector.loadModel()
        print("Loading model..........")

    def predict(self,X,feature_name):
        print("Entering.....................................")
        self.im = Image.open(requests.get(X, stream=True).raw)
        self.im.save("image.png")
        self.im_f = "image.png"
        #if X[-3:]=="png":
        self.image_numpy = io.imread(self.im_f)
        self.image_numpy = self.image_numpy[:,:,:3]
        print("PNG is ready to detect..................")
        #else:
        #    self.image_numpy = io.imread( X )
        #    print("Ready to detect")
        print("Detecting........................................")
        self.detections = self.detector.detectObjectsFromImage(input_type="array", input_image=self.image_numpy , output_image_path=os.path.join(self.execution_path , "image.png"))
        self.identity = dict()
        count = 1
        for eachObject in self.detections:
            self.identity[count]=[eachObject["name"],eachObject["percentage_probability"],eachObject["box_points"]]
            count += 1
        json_object = json.dumps(self.identity)
        return json_object
