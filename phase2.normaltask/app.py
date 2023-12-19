import streamlit as st
import pickle
import string

background_image_code = """
<style>
    body {
        background-image: url('A:\datascience\withMLmodel\Emailproj\Hacker-Wallpaper-03-4000x2158-1-scaled.jpg');
        background-size: cover;
    }
</style>
"""

st.markdown(background_image_code, unsafe_allow_html=True)

def transform_text(text):
    text = text.lower()
    text = text.split(" ")

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in string.punctuation:
            y.append(i)

    return " ".join(y)

c_vic= pickle.load(open(r".\vectorizerV5.pkl",'rb'))
model = pickle.load(open(r".\modelV5.pkl",'rb'))

st.title("Email Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Classify'):

    transformed_sms = transform_text(input_sms)
    vec = c_vic.transform([transformed_sms])
    result = model.predict(vec)[0]
    
    if result == 1:
        st.header("Spam")
    else:
        st.header("Ham")
