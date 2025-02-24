#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("Error: The 'streamlit' module is not installed. Please install it using 'pip install streamlit'.")
    exit()

# Initialize session state for storing responses
if "responses" not in st.session_state:
    st.session_state.responses = []

# Survey Title
st.title("University Journey Survey")

# Define Gender Question
st.subheader("Select Your Gender:")
gender = st.radio("What is your gender?", ["FLINTA*", "Male", "Prefer not to assign"])

# Define First Question
st.subheader("Question 1: Biggest Challenge in Attaining a University Degree")
biggest_challenge = st.radio("What factor has been your biggest challenge?", [
    "Financial situation", "Parental education", "School support", "Cultural/family expectations", "None"
])

# Define Second Question
st.subheader("Question 2: Biggest Help in Your Academic Journey")
biggest_help = st.radio("What factor has helped you the most so far?", [
    "Financial situation", "Parental education", "School support", "Cultural/family expectations", "None"
])

# Submit Button
if st.button("Submit Response"):
    st.session_state.responses.append({
        "Gender": gender,
        "Biggest Challenge": biggest_challenge,
        "Biggest Help": biggest_help
    })
    st.success("Your response has been recorded!")

# Convert responses to a DataFrame
if len(st.session_state.responses) > 0:
    df = pd.DataFrame(st.session_state.responses)

    # Plot stacked bar chart for Biggest Challenge
    st.subheader("Survey Results: Biggest Challenges in University Attainment")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x="Biggest Challenge", hue="Gender", ax=ax)
    ax.set_xlabel("Challenges")
    ax.set_ylabel("Count")
    ax.set_title("Challenges in University Attainment by Gender")
    ax.legend(title="Gender")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Plot stacked bar chart for Biggest Help
    st.subheader("Survey Results: Factors that Helped in Academic Journey")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df, x="Biggest Help", hue="Gender", ax=ax)
    ax.set_xlabel("Helping Factors")
    ax.set_ylabel("Count")
    ax.set_title("Factors Supporting Academic Journey by Gender")
    ax.legend(title="Gender")
    plt.xticks(rotation=45)
    st.pyplot(fig)

