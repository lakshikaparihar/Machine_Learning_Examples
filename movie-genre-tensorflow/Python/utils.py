from tensorflow.keras.preprocessing import image

def cleansing(img):
  print("Entering cleansing........")
  img = image.img_to_array(img)
  img = img/255.0
  img = img.reshape(1,350,350,3)
  print("Cleansing is done.........")
  return img

