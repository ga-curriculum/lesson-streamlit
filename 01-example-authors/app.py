import matplotlib.pyplot as plt
import pandas as pd
import pickle
import streamlit as st

st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

st.title('Austen or Poe?')

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
    'Page',
    ('About', 'EDA', 'Make a prediction')
)

if page == 'About':
    st.subheader('About this project')
    st.write('''
This is a Streamlit app that hosts my Poe vs. Austen model.

The best model I found was....

You can get in touch with me on these websites....

etc.
    ''')
elif page == 'EDA':
    # header
    st.subheader('Exploratory Data Analysis')
    st.write('''The model is trained on paragraphs.
    
Below you can find....''')
    

elif page == 'Make a prediction':
    
    st.title('Which author do you write like?')

    # Open your model!
    with open('../models/austen-poe-detector.pkl', 'rb') as f:
        model = pickle.load(f)

    # Text input
    text = st.text_area('Please enter some text:', max_chars=500)

    # Save predicted author & probabilities
    predicted_author = model.predict([text])[0]
    probs = list(model.predict_proba([text])[0])

    # Create button
    if st.button('Submit'):
        if len(text) > 0:

            # Add some pictures?
        
            if predicted_author == 'Edgar Allan Poe':
                prob = probs[0]
                st.write(f'You write like Edgar Allan Poe with a {round(100 * prob, 2)}% probability!')
                st.image('https://cdn.pixabay.com/photo/2012/10/26/01/14/portrait-62996_960_720.jpg')
                st.balloons()

            if predicted_author == 'Jane Austen':
                prob = probs[1]
                st.write(f'You write like Jane Austen with a {round(100 * prob, 2)}% probability!')
                st.image('https://images.unsplash.com/photo-1573125716783-d05b57a86488?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80')
                st.snow()
        else:
            st.error('Please write some text to generate a prediction!')
