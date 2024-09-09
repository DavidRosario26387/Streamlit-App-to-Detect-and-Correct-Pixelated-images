# app.py
import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image  
from Detection_model import predict_image
from ESPCN import correct

st.set_page_config(layout="wide")
st.write("Hello... 👋🤗")
st.markdown("<h1 style='text-align: center;'>Detect Pixelated Images and Correct it</h1>", unsafe_allow_html=True)


row1 = st.columns(2)
col1 = row1[0].container()
col2 = row1[1].container()
col1.markdown("<h1 style='text-align: center; font-size: 40px;'>Detection</h1>", unsafe_allow_html=True)
col2.markdown("<h1 style='text-align: center; font-size: 40px;'>Correction</h1>", unsafe_allow_html=True)

def correct_image(image):
    upscaled_image = correct(image)
    if upscaled_image:
        st.success("Correction Complete")
        temp_name = 'corrected_image.png'
        upscaled_image.save(temp_name)
        with open(temp_name, 'rb') as file:
            st.download_button(label="Download image", data=file, file_name="Corrected.png", mime="image/png")
    else:
        st.error("Oops!..Error")

with col1:
    uploaded_file1 = st.file_uploader("Choose an image for Detection...", type=["jpg", "png", "jpeg"])
    detect_button = st.button("Detect Pixelation", disabled=uploaded_file1 is None)
    if uploaded_file1 is not None:
        image1 = Image.open(uploaded_file1)
        st.image(image1, caption="Uploaded Image for Detection", use_column_width=True)

    if detect_button and uploaded_file1 is not None:
        prediction = predict_image(image1) 
        if prediction > 0.5:
            st.error("The image is pixelated.")
        else:
            st.success("The image is not pixelated.")
with col2:
    uploaded_file2 = st.file_uploader("Choose an image for Correction...", type=["jpg", "png", "jpeg"])
    correct_button=st.button("Correct Pixelated Image", disabled=uploaded_file2 is None)
    if uploaded_file2 is not None:
        image2 = Image.open(uploaded_file2)
        st.image(image2, caption="Uploaded Image for Correction", use_column_width=True)
    if correct_button and uploaded_file1 is not None:
        correct_image(image2)
