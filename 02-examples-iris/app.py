import streamlit as st
import plotly.express as px
import numpy as np
import pickle
from predict import predict_flower
import time


st.title("Some Extras to Show!")
st.header("1️⃣ Let's First Take a Look at Checkboxes")

df_iris = px.data.iris()

show_eda = st.checkbox("Do you want to see some EDA?")

if show_eda:  # evaluates to true if checked
    hist_sepal = px.histogram(df_iris, x='sepal_length')
    hist_sepal 

show_df = st.checkbox("Do you want to see the data?")

if show_df:  # evaluates to true if checked
    df_iris

st.header("2️⃣ Using User Input to Make Predictions")


s_l = st.number_input("Sepal Length in cm", 0, 100)
s_w = st.number_input("Sepal Width in cm", 0, 100)
p_l = st.number_input("Petal Length in cm", 0, 100)
p_w = st.number_input("Petal Width in cm", 0, 100)

user_input = np.array([s_l, s_w, p_l, p_w])

# load model
with open('models/saved-iris-model.pkl', 'rb') as f:
    classifier = pickle.load(f)

# make prediction

if st.button('Make prediction'):
    with st.spinner('Predicting...'):
        time.sleep(5)
        prediction = predict_flower(classifier, user_input)

    st.text(f"The model predicts: {prediction[0].title()}")

st.header("3️⃣ Adding Some Columns!")

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


st.header("4️⃣ Lastly, a Pretty Cool Choropleth")

df = px.data.gapminder()

fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="lifeExp",
    hover_name="country",
    animation_frame="year",  # animation
    range_color=[20, 80],
)
fig