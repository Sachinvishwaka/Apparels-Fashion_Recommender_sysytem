
import streamlit as st

st.set_page_config(
    page_title="Multipage_app",
    page_icon="None",
    layout="wide"
)
st.title("Apparels-Fashion Recommender System")
# Display Images
 
# import Image from pillow to open images
# import Image from pillow to open images
from PIL import Image
img = Image.open("Fashion image.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, caption="Fashion Images")



## adding description about mnist digit recognizer


st.markdown("A recommendation system is a system that is programmed to predict future preferable items from a large set of collections. A recommendation system works either by using user preferences or by using the items most preferred by all users".)
st.markdown("The main challenge in building a fashion recommendation system is that it is a very dynamic industry. It changes very often when it comes to seasons, festivals, pandemic conditions like coronavirus and many more.")

