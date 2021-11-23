import streamlit as st
import datetime as dt
import pandas as pd
import numpy as np
from PIL import Image

smart_living_icon = Image.open('2.1 Smart Living logo.png')
st.image(smart_living_icon, caption='HKT Smart Living')
st.image('https://aws1.discourse-cdn.com/business7/uploads/streamlit/original/2X/f/f0d0d26db1f2d99da8472951c60e5a1b782eb6fe.png')


st.title('My Trial Website by Alex Lee')
st.header('Welcome to HKT Smart Living Engineering')

now = dt.datetime.now()
your_name = "Your whatever name"

st.write(f"It is now {now}")

st.write(f"My name is {your_name}.")

input_text = st.text_input('Enter whatever:')
st.caption('This is a string that explains something above.')

st.markdown("**mark**down")

code = '''def hello():
          print("Hello, Streamlit!")'''

st.code(code, language='python')
st.text("This is some text.This is some text.This is some text.This is some text.This is some text.This is some text.\nThis is some text.This is some text.This is some text.This is some text.This is some text.This is some text.This is some text.This is some text.")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


image = Image.open('sunshine.jpg')
st.image(image, caption='Sunrise by the mountains')

video_file = open('HKT_SL x MtAnderson_Video_Output_20210521.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.caption('This video is from local network.')


st.video('https://www.youtube.com/watch?v=Klqn--Mu2pE')
st.caption('This video is from Youtube.')

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)




# Insert containers
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# Insert containers



# Insert form
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")
# Insert form
