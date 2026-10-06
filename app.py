import streamlit as st
import requests

st.title("Language Translation Tool")

# Enter text
text = st.text_area("Enter your text:")

# Select languages
source_language = st.selectbox(
    "Select source language",
    ["English", "Telugu", "Hindi", "Tamil", "Kannada"]
)

target_language = st.selectbox(
    "Select target language",
    ["English", "Telugu", "Hindi", "Tamil", "Kannada"]
)

# Language codes
language_codes = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn"
}

# Translate button
if st.button("Translate"):

    if text == "":
        st.warning("Please enter some text.")

    else:
        source = language_codes[source_language]
        target = language_codes[target_language]

        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": text,
            "langpair": source + "|" + target
        }

        response = requests.get(url, params=params)

        print(response.status_code)
        print(response.text)

        if response.status_code == 200:

            data = response.json()

            result = data["responseData"]["translatedText"]

            st.subheader("Translated Text:")
            st.success(result)

        else:
            st.error("Translation failed")
            st.write(response.text)