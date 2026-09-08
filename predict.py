import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'model224.h5'
model = load_model(filepath)
print("Model Loaded Successfully")

def process(in_path):
  test_image = load_img(in_path, target_size=(224, 224))
  print("Got Image for prediction")
  test_image = img_to_array(test_image)/255
  test_image = np.expand_dims(test_image, axis=0)
  result = model.predict(test_image)
  print('Raw result = ', result)
  pred = np.argmax(result, axis=1)[0]
  print("Prediction:", pred)
  return pred
#process("./Data/Normal/1-1-59_6128b3f32ba4b_jpg.rf.6cdba32abc38835bbf016648f3268b66.jpg")
#process("./Data/Vitamin B/109903_jpg.rf.56ce33a1367eb4d7ab1d40c982f49288.jpg")
#process("./Data/Vitamin D/1-7-e1679346473765_jpg.rf.1f174b1c529b95c2c55e5d3e62a39a3d.jpg")
#process("./Data/Vitamin E/2752__ProtectWyJQcm90ZWN0Il0_FocusFillWzI5NCwyMjIsIngiLDFd_jpg.rf.72d7c46ab0192e0c2c68e5ef9f13c3fd.jpg")