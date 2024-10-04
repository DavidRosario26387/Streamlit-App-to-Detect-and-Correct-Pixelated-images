# Pixelated Image Detection and Correction

This project provides a solution for detecting and correcting pixelated images using machine learning and super-resolution techniques. The user interface is built with Streamlit, enabling easy interaction with the model for both detecting pixelation in images and correcting pixelated images.

## Features
- **Pixelated Image Detection**: A convolutional neural network (CNN) model is used to predict whether an image is pixelated.
- **Pixelated Image Correction**: Uses the ESPCN (Efficient Sub-Pixel Convolutional Neural Network) model to restore pixelated images.
- **Streamlit UI**: A user-friendly interface for uploading images, detecting pixelation, and downloading corrected images.

## Demo
You can interact with the web application by running the following command:

``` bash
streamlit run app.py
```
<hr>
<img src="https://github.com/user-attachments/assets/a4d58b1c-a3d6-46d4-acfe-d82b514bd268" alt='Image' width="100%" height=720"/>
<hr>
<img src="https://github.com/user-attachments/assets/325d0eb1-213a-445a-a05f-e566a4326f5a" alt='Image' width="100%" height="400"/>
<hr>
<img src="https://github.com/user-attachments/assets/06e7f3e5-c44d-4cb3-b313-3f0c640ede00" alt='Image' width="100%" height="400"/>
<hr>

### The app provides two primary features:

- **Detection**: Upload an image to check if it's pixelated.
- **Correction**: Upload a pixelated image, and the app will apply super-resolution to correct it.

## Project Structure
``` bash
.
├── app.py                   # Main Streamlit app for UI
├── Detection_model.py        # Code for the pixelation detection model
├── ESPCN.py                  # Code for the ESPCN-based correction model
├── requirements.txt          # Python dependencies
├── saved_model/
│   └── pixel_detection_model.h5  # Pre-trained model for detection
├── espcn_weights/
│   └── ESPCN_x4.pb           # Pre-trained ESPCN model for correction
└── README.md                 # Project documentation
```

## Prerequisites
- Python 3.x
- TensorFlow, OpenCV, Streamlit, and other dependencies listed in requirements.txt.
  
## Installation
## Clone the repository:
``` bash
git clone https://github.com/DavidRosario26387/Streamlit-App-to-Detect-and-Correct-Pixelated-images.git
cd Streamlit-App-to-Detect-and-Correct-Pixelated-images
```
## Install the required dependencies:
``` bash
pip install -r requirements.txt
```

Ensure the model weights are placed in the correct directory:

-Detection model: `saved_model/pixel_detection_model.h5`

-ESPCN model weights: `espcn_weights/ESPCN_x4.pb`

## Running the Application
To launch the app locally, run:
``` bash
streamlit run app.py
```
The application will be accessible via a local web browser, where you can upload images to detect and correct pixelation.

## Credits
+ The ESPCN model is based on the implementation by Fanny Monori.
+ Detection model is a pre-trained CNN model fine-tuned for pixelation detection.

For more details on the model, please visit my repository: [Pixelated Image Detection and Correction](https://github.com/DavidRosario26387/Pixelated-Image-Detection-Correction).
