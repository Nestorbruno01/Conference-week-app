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

# Load existing responses if available
CSV_FILE = "survey_responses.csv"
try:
    df_responses = pd.read_csv(CSV_FILE)
except FileNotFoundError:
    df_responses = pd.DataFrame(columns=["Gender", "Biggest Challenge", "Biggest Help"])

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
    new_response = pd.DataFrame([{ "Gender": gender, "Biggest Challenge": biggest_challenge, "Biggest Help": biggest_help }])
    df_responses = pd.concat([df_responses, new_response], ignore_index=True)
    df_responses.to_csv(CSV_FILE, index=False)
    st.success("Your response has been recorded!")

# Convert responses to a DataFrame and display results
if not df_responses.empty:
    # Plot stacked bar chart for Biggest Challenge
    st.subheader("Survey Results: Biggest Challenges in University Attainment")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df_responses, x="Biggest Challenge", hue="Gender", ax=ax)
    ax.set_xlabel("Challenges")
    ax.set_ylabel("Count")
    ax.set_title("Challenges in University Attainment by Gender")
    ax.legend(title="Gender")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Plot stacked bar chart for Biggest Help
    st.subheader("Survey Results: Factors that Helped in Academic Journey")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=df_responses, x="Biggest Help", hue="Gender", ax=ax)
    ax.set_xlabel("Helping Factors")
    ax.set_ylabel("Count")
    ax.set_title("Factors Supporting Academic Journey by Gender")
    ax.legend(title="Gender")
    plt.xticks(rotation=45)
    st.pyplot(fig)

