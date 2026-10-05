import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool", page_icon="🌐")
st.title("🌐 CodeAlpha - Language Translation Tool")

languages = {
    "English":"en","Hindi":"hi","Gujarati":"gu","Marathi":"mr",
    "Bengali":"bn","Tamil":"ta","Telugu":"te","Kannada":"kn",
    "Malayalam":"ml","Punjabi":"pa","French":"fr","German":"de",
    "Spanish":"es","Japanese":"ja","Chinese":"zh-CN"
}

c1, c2 = st.columns(2)
with c1:
    source = st.selectbox("From", list(languages))
with c2:
    target = st.selectbox("To", list(languages), index=1)

text = st.text_area("Enter text")

if st.button("Translate", type="primary"):
    if not text.strip():
        st.warning("Please enter some text.")
    elif source == target:
        st.text_area("Translated text", text)
    else:
        try:
            result = GoogleTranslator(
                source=languages[source], target=languages[target]
            ).translate(text)
            st.success("Translation completed!")
            st.text_area("Translated text", result)
            st.download_button(
                "Download translation", result,
                file_name="translated_text.txt", mime="text/plain"
            )
        except Exception:
            st.error("Translation failed. Please check your internet connection.")
