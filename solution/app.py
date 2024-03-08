import pickle
import streamlit as st

st.title("Which author do you write like? :book:")
st.subheader("Jane Austen or Edgar Allen Poe?")

with open('../models/austen-poe-detector.pkl', 'rb') as f:
    model = pickle.load(f)

text = st.text_area("Enter text here.")

pred = model.predict([text])[0]

if st.button("Submit"):
    st.write(f"You write most like: {pred}!")
    st.balloons()
