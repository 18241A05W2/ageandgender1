import streamlit as st
import numpy as np
import cv2 as cv
from ageandgender import age_gender_detector
from PIL import Image
from design import *

def main():
    #Age and Gender Detection
    st.markdown(html_temp, unsafe_allow_html=True)
    image_file = st.file_uploader("Upload your image",type=['png','jpg','jpeg'])
    if image_file is not None:
        our_image = Image.open(image_file)
        open_cv_image = np.array(our_image)
        st.text("Original Image")
        st.image(open_cv_image)

    if st.button('Detect'):
        result_img = age_gender_detector(open_cv_image)
        st.image(result_img)

if __name__ == '__main__':
    main()
