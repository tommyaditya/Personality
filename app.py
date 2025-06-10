import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Prediksi Kepribadian")

with st.form("form"):
    time_alone = st.slider("Waktu dihabiskan sendiri (0-10)", 0, 10, 5)
    event_attend = st.slider("Kehadiran di acara sosial (0-10)", 0, 10, 5)
    going_out = st.slider("Frekuensi keluar rumah (0-10)", 0, 10, 5)
    friend_circle = st.slider("Ukuran lingkaran pertemanan (0-10)", 0, 10, 5)
    post_freq = st.slider("Frekuensi posting di medsos (0-10)", 0, 10, 5)
    stage_fear = st.selectbox("Takut tampil di depan umum?", ["Yes", "No"])
    drained_social = st.selectbox("Lelah setelah bersosialisasi?", ["Yes", "No"])
    submit = st.form_submit_button("Prediksi")

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
    st.success(f"Prediksi kepribadianmu: **{prediction}**")
