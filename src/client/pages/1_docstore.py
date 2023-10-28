# app/pages/docstore.py

import streamlit as st

st.set_page_config(
    page_title="VectaLearn",
    page_icon="🧊",
)

uploaded_file = st.sidebar.file_uploader(
    label="Upload a doc",
    type=["pdf", "docx", "txt", "md"],
    accept_multiple_files=True,
)
