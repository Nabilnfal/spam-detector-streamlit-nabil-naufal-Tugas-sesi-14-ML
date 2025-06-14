
import streamlit as st
import joblib

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Aplikasi Deteksi Spam")
st.write("Masukkan pesan untuk mendeteksi apakah spam atau bukan.")

user_input = st.text_area("Masukkan pesan:")
if st.button("Deteksi"):
    if user_input.strip() != "":
        data = vectorizer.transform([user_input])
        result = model.predict(data)
        st.success("Hasil Deteksi: {}".format("Spam" if result[0] == 1 else "Bukan Spam"))
