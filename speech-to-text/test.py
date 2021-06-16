from Model import Model
#x = 'nish.wav'
x = 'nish.m4a'
#x = 'nish.mp3'
print(Model().predict(x,["feature_name"]))
