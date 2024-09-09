# model.py
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the detection model
Detection_model = load_model('saved_model/pixel_detection_model.h5')

def load_and_crop_image(img):
    width, height = img.size
    left = (width - 224) // 2
    top = (height - 224) // 2
    right = left + 224
    bottom = top + 224
    img = img.crop((left, top, right, bottom))
    img = img.convert('RGB')  # Ensure the image is in RGB mode
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize pixel values
    return img  # Return the cropped image

def predict_image(img):
    cropped_img = load_and_crop_image(img)
    prediction = Detection_model.predict(cropped_img)
    return prediction[0]
