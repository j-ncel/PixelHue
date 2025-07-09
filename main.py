import streamlit as st
from PIL import Image
from palette_extractor import extract
from template import template

DEFAULT_IMG = "koala.png"

st.set_page_config(page_title="PixelHue", page_icon="🎨", layout="centered")

st.title(":rainbow[PixelHue Palette Generator] 🎨")

st.markdown(template.css, unsafe_allow_html=True)


file = st.file_uploader("Upload Image", type=[
    "jpg", "png", "jpeg", "bmp", "gif", "webp"], label_visibility="collapsed")
st.write("")
maincol = st.columns(2)

with maincol[0]:
    img = Image.open(file if file else DEFAULT_IMG)
    st.image(img, caption=file.name if file else DEFAULT_IMG, width=300)


with maincol[1]:
    cols = st.columns(3)
    numbers = st.number_input(
        "Number of Colors", step=1, min_value=1, value=9, key="numbers")
    for i, color in enumerate(extract(img, numbers)):
        with cols[i % 3]:
            html_code_for_swatch = template.color_swatch_template.substitute(
                color=color)

            st.components.v1.html(html_code_for_swatch, height=120)

            st.markdown(
                f'<p class="color-text">{color}</p>', unsafe_allow_html=True)


st.markdown("""
<a href="https://coff.ee/jncel" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" width="170">
</a>
""", unsafe_allow_html=True)
