# Single Pixel Coordinates

A  predictor to locate the single pixel coordinates in a image.

## Docker Image

```code
docker pull deepakdocker27/singlepixelcoordinate

docker run deepakdocker27/singlepixelcoordinate

```

## Table of Contents

- Prepare Data
- Installation
- Usage

## Preparing the Data <a name="preparingthedata"></a>
<!-- **Structure:**   -->
Please click the [data](https://www.kaggle.com/datasets/phucthaiv02/butterfly-image-classification/data) to download and prepare the images. In our code, the data should be organized as below:

Note : There are just images in this dataset. After that, it was processed through our code, annotated, and saved in the annotated_images directory.

```plaintext
datasets/
|--annotated_images/
|  |--test
|  |  |--image_01.jpg
|  |  |--image_02.jpg
|  |  |--image_03.jpg
|  |  |--image_04.jpg    
|  |--train
|  |  |--image_01.jpg
|  |  |--image_02.jpg
|  |  |--image_03.jpg
|  |  |--image_04.jpg    
|--images/
|  |--test
|  |  |--image_01.jpg
|  |  |--image_02.jpg
|  |  |--image_03.jpg
|  |  |--image_04.jpg    
|  |--train
|  |  |--image_01.jpg
|  |  |--image_02.jpg
|  |  |--image_03.jpg
|  |  |--image_04.jpg
|--test.csv
|--train.csv
```


## Installation

### Dependencies

#### --Python 3.10.9

#### --Tensorflow 2.14.0


### Python Environment
Please excuate the following commands.

```code
git clone https://github.com/Deepak-1667/Single_Pixel_Coordinate_Prediction.git Single_Pixel_Coordinate_Prediction
cd Single_Pixel_Coordinate_Prediction

python -m venv venv
```
### Activating Virtual Environment
-On Windows:
```code
.\venv\Scripts\activate
```

-On macOS and Linux:
```code
source venv/bin/activate
```

### Installing dependencies
```code
pip install tensorflow==2.14.0

pip install -r requirements.txt

```

## Usage

### To Annotate Image
Run the command :
```code
python code/annotate_images.py

```
### Train
Run the command :
```code
python code/train.py

```
### Test
Run the command :
```code
python code/test.py

```

### To Check Single Image
Run the command :
```code
python code/main.py

```

## Pre-Trained Model
click the [link](https://drive.google.com/drive/folders/109Vz8e2ACWvLP94fuPYSBAPHuF6k2yr0?usp=drive_link) to download the pretrained Model and organized as below

```plaintext
models/
|--model.h5/

```

