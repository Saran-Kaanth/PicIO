import streamlit as st

from helpers.helper import Helper

helper = Helper()

st.set_page_config(layout="wide", page_title="PicIO💫")

st.title("PicIO💫")
st.markdown(
    "***AI tool that extracts images from the given files and provides descriptions for the corresponding images.***"
)
st.warning(
    "The models (LLMs) used in this application are preview versions. You might notice some hallucinations in the image descriptions."
)

st.sidebar.header("PicIO")
file_type = st.sidebar.selectbox(
    "Choose your file type", ["PDF", "Word", "Powerpoint", "Excel"]
)

try:
    if file_type == "PDF":
        uploaded_files = st.sidebar.file_uploader(
            "Upload PDF files", type="pdf", accept_multiple_files=True
        )
        if uploaded_files:
            helper.extract_images_from_uploaded_file(file_type, uploaded_files)

    elif file_type == "Word":
        uploaded_docs = st.sidebar.file_uploader(
            "Upload Word document files", type="docx", accept_multiple_files=True
        )
        if uploaded_docs:
            helper.extract_images_from_uploaded_file(file_type, uploaded_docs)

    elif file_type == "Excel":
        uploaded_files = st.sidebar.file_uploader(
            "Upload Excel files", type="xlsx", accept_multiple_files=True
        )
        if uploaded_files:
            helper.extract_images_from_uploaded_file(file_type, uploaded_files)

    else:
        uploaded_ppts = st.sidebar.file_uploader(
            "Upload PowerPoint files", type=["pptx"], accept_multiple_files=True
        )
        if uploaded_ppts:
            helper.extract_images_from_uploaded_file(file_type, uploaded_ppts)
except Exception:
    st.error("Unable to process the files. Please try again later.")