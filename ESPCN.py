# Model weights downloaded from: https://github.com/fannymonori/TF-ESPCN
# Author: Fanny Monori
# TensorFlow ESPCN implementation for super-resolution
import cv2
from cv2 import dnn_superres
from PIL import Image
import numpy as np

sr=dnn_superres.DnnSuperResImpl_create()
# Ensure the ESPCN model file ('ESPCN_x4.pb') is downloaded and placed in the 'weights' directory
path= 'espcn_weights//ESPCN_x4.pb'
sr.readModel(path)
sr.setModel('espcn',4)


def correct(img):
    original_width, original_height = img.size
    new_width = original_width // 4
    new_height = original_height // 4
    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
    resized_image = cv2.cvtColor(np.array(resized_img), cv2.COLOR_RGB2BGR)
    upscaled_image = sr.upsample(resized_image)
    upscaled_image_pil = Image.fromarray(cv2.cvtColor(upscaled_image, cv2.COLOR_BGR2RGB))
    return upscaled_image_pil
