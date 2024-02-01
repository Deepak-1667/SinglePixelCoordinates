import cv2  
import os
import random
import csv

# Input and output folders  
input_folder = 'datasets/images/test'   
output_folder = 'datasets/annotated_images/test'  

# Create output folder if doesn't exist  
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# CSV folder path
csv_file_path = "datasets/test.csv"  

# Ensure output folders exist
os.makedirs(output_folder, exist_ok=True)  
os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

# Open CSV file for writing 
with open(csv_file_path, mode='w', newline='') as csv_file:
    fieldnames = ['image_path',
                  'x_coordinate', 
                  'y_coordinate', 
                  'image_width', 
                  'image_height']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
  
    for filename in os.listdir(input_folder):

        # Load and preprocess image
        image = cv2.imread(os.path.join(input_folder, filename))  
        image = cv2.resize(image, (256, 256))   
        height, width, _ = image.shape 
        
        # Pick random pixel 
        x = random.randint(0, width-1)  
        y = random.randint(0, height-1)

        # Annotate pixel
        if x >= 0 and x < image.shape[0] and y >= 0 and y < image.shape[1]:
            image[x, y] = (0, 0, 255) 
        cv2.circle(image, (x, y), 
                   radius=3,  
                   color=(0, 0, 255), 
                   thickness=-1)


        # Save annotated image    
        output_path = os.path.join(output_folder, filename) 
        cv2.imwrite(output_path, image)

        # Write row to the CSV file
        writer.writerow({
            'image_path': filename,
            'x_coordinate': x,
            'y_coordinate': y,
            'image_width': width,
            'image_height': height  
        })
        
print('Saved annotated images to folder: ', output_folder)