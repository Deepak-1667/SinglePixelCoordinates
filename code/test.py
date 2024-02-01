import tensorflow as tf 
import pandas as pd   
import numpy as np
import cv2
import os
from PIL import Image


# Image loading and preprocessing functions
def load_image(filename):
    img = Image.open(filename) 
    img_arr = np.asarray(img)
    return img_arr


# Load dataset from CSV 
df = pd.read_csv('datasets/test.csv')  

# Separate features and labels
X = df['image_path']  
y = df[['x_coordinate', 'y_coordinate']]
y = y.to_numpy()


# Load test images and preprocess
images = []
dir_path = "datasets/annotated_images/test" 

# Iterate through image paths
for filename in X:  
    img = load_image(os.path.join(dir_path, filename)) 
    images.append(img)

# Convert list of images to numpy array
X = np.array(images)   

# Load trained model and compile  
model = tf.keras.models.load_model('models/single_pixel_model3.h5')  
model.compile(loss='mse', metrics=['mse'])   

# Evaluate model on test data
loss, mse = model.evaluate(X, y)  

# Print metrics
print("Restored model loss:", loss)  
print("Restored model mse:", mse)

# Make predictions on test data   
coords_pred = model.predict(X)   

# Calculate prediction error
error = np.mean(np.sqrt(np.sum(np.square(coords_pred - y)))) 
print("Prediction Error: ", error)