import tensorflow as tf 
import numpy as np
from PIL import Image

# Image path
filename = "datasets/annotated_images/test/Image_19.jpg" 

# open and preprocess image
img = Image.open(filename) 
img=img.resize((256, 256)) 
img_arr = np.asarray(img)
img_arr = np.expand_dims(img_arr, axis=0)

# Model Loading and Compiling
model = tf.keras.models.load_model('models/single_pixel_model3.h5')  
model.compile(loss='mse', metrics=['mse'])   


# Make predictions on given Image   
coords_pred = model.predict(img_arr)   

print(f"X co-ordinate :{coords_pred[0][0]} , y co-ordinate :{coords_pred[0][1]}")