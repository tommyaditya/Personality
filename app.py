import streamlit as st
import pandas as pd
import pickle

# Load model dan encoder
model = pickle.load(open("model.pkl", "rb"))
le = pickle.load(open("encoder.pkl", "rb"))

st.title("Personality Prediction")

with st.form("form"):
    time_alone = st.slider("Time spent alone (0-10)", 0, 15, 5)
    event_attend = st.slider("Attendance at social events (0-10)", 0, 15, 5)
    going_out = st.slider("Frequency of going out (0-10)", 0, 15, 5)
    friend_circle = st.slider("Size of social circle (0-10)", 0, 15, 5)
    post_freq = st.slider("Frequency of posting on social media (0-10)", 0, 15, 5)
    stage_fear = st.selectbox("Afraid of appearing in public?", ["Yes", "No"])
    drained_social = st.selectbox("Tired after socializing?", ["Yes", "No"])
    submit = st.form_submit_button("Prediction")

if submit:
    input_df = pd.DataFrame({
        "Time_spent_Alone": [time_alone],
        "Social_event_attendance": [event_attend],
        "Going_outside": [going_out],
        "Friends_circle_size": [friend_circle],
        "Post_frequency": [post_freq],
        "Stage_fear": [1 if stage_fear == "Yes" else 0],
        "Drained_after_socializing": [1 if drained_social == "Yes" else 0]
    })

    prediction = model.predict(input_df)[0]
    personality = le.inverse_transform([prediction])[0]

    st.success(f"You are probably a: **{personality}**")
