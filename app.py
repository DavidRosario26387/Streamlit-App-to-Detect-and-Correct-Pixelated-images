import streamlit as st
from PIL import Image  
from Detection_model import predict_image
from ESPCN import correct

# Set up Streamlit app with a wide layout
st.set_page_config(layout="wide")
st.write("Hello... 👋🤗")
st.markdown("<h1 style='text-align: center;'>Detect and Restore Pixelated Images</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .spacer {
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'is_pixelated' not in st.session_state:
    st.session_state['is_pixelated'] = None

if 'image' not in st.session_state:
    st.session_state['image'] = None

# Setup two columns for detection and result display
row1 = st.columns(2)
col1 = row1[0].container()
col2 = row1[1].container()
col1.markdown("<h1 style='text-align: center; font-size: 40px;'>Detection</h1>", unsafe_allow_html=True)
col2.markdown("<h1 style='text-align: center; font-size: 40px;'>Result</h1>", unsafe_allow_html=True)

# Function to restore the pixelated image
def restore_image(image):
    upscaled_image = correct(image)
    if upscaled_image:
        st.success("Restoration Complete")
        # Display the restored image
        st.image(upscaled_image, caption="Restored Image", use_column_width=True)
        temp_name = 'restored_image.png'
        upscaled_image.save(temp_name)

        # Notify user to download the restored image
        st.success("Download the improved image to view.")
        with open(temp_name, 'rb') as file:
            st.download_button(label="Download Restored Image", data=file, file_name="Restored.png", mime="image/png")
    else:
        st.error("Oops!..Error during restoration")

# Column for Detection
with col1:
    uploaded_file = st.file_uploader("Choose an image for Detection...", type=["jpg", "png", "jpeg"])
    detect_button = st.button("Detect Pixelation", disabled=uploaded_file is None)

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image for Detection", use_column_width=True)
    else:
        # del st.session_state['is_pixelated']
        # del st.session_state['image']
        st.session_state['is_pixelated']=None
        st.session_state['image']=None

    if detect_button and uploaded_file is not None:
        prediction = predict_image(image)
        if prediction > 0.5:
            st.session_state['is_pixelated'] = True
            st.session_state['image'] = image
        else:
            st.session_state['is_pixelated'] = False
            st.success("The image is not pixelated.")

# Column for Result and Restoration
with col2:
    # Adding a spacer div to create uniform space
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    if 'is_pixelated' in st.session_state:
        if st.session_state['is_pixelated']:
            st.error("The image is pixelated.")
            restore_button = st.button("Restore Pixelated Image")
            if restore_button:
                restore_image(st.session_state['image'])
        elif st.session_state['is_pixelated']==False:
            st.success("The image is not pixelated.")