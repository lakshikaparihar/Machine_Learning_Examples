import face_recognition
import numpy as np
from PIL import Image, ImageDraw
import urllib.request
class main(object):
    def __init__(self):
        print("Initialzing the class")
        print("Loading model")

    def predict(self, X, feature_names):
        print("In the prediction..")
        known_face_encoding = []
        for i in range(1,len(X[0])):
            response = urllib.request.urlopen(X[0][i])
            find_image = face_recognition.load_image_file(response)
            face_encoding = face_recognition.face_encodings(find_image)[0]
            known_face_encoding.append(face_encoding)
        known_face_name=X[1]
        print('Learned encoding for', len(known_face_encoding), 'images.')
        res = urllib.request.urlopen(X[0][0])
        unknown_image = face_recognition.load_image_file(res)
        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        pil_image = Image.fromarray(unknown_image)
        draw = ImageDraw.Draw(pil_image)
        output = []
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_name[best_match_index]
                out = name + " found at " + str([(left, top), (right, bottom)])
                draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
                text_width, text_height = draw.textsize(name)
                draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
                draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
                output.append(out)
        del draw
        pil_image.save("final.jpg")
        print("Predicting......")
        return output
