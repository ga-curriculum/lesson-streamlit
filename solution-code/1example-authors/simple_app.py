import pickle
import streamlit as st

st.title('Which author do you write like?')

# Open your model!
with open('models/author_pipe.pkl', 'rb') as f:
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




#st.write(f'You write like {predicted_author.title()}.')