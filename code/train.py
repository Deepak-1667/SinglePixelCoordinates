import pandas as pd
import numpy as np
import os
from PIL import Image
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense  
from keras.optimizers import Adam

# Load Images from the files
def load_image(filename):
    img = Image.open(filename)
    img_arr = np.asarray(img)  
    return img_arr

# Load dataset from CSV  
df = pd.read_csv('datasets/train.csv')

# Separate into features and labels
X = df['image_path']  
y = df[['x_coordinate', 'y_coordinate']]
y = y.to_numpy()

# Load and preprocess images
images = []
dir_path = "datasets/annotated_images/train"
for filename in X:
    img = load_image(os.path.join(dir_path, filename))
    images.append(img)
X = np.array(images)

# Model building and compiling
model = Sequential()
model.add(Conv2D(32, kernel_size=3, 
                 activation='relu', input_shape=(256,256,3)))
model.add(MaxPooling2D(pool_size=2))
model.add(Conv2D(64, kernel_size=3, activation='relu')) 
model.add(MaxPooling2D(pool_size=2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(2))
model.compile(optimizer=Adam(), 
              loss='mean_squared_error',
              metrics=['accuracy'])

# Fitting datasets to the model
model.fit(X, y, epochs=50)  

# Save the model
model.save('models/single_pixel_model.h5')