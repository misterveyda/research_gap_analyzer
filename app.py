import streamlit as st
from src.pdf_extractor import extract_text_from_pdf
from src.text_preprocessing import preprocess_text
from src.topic_modeling import extract_topics
from src.gap_analysis import identify_gaps

st.title("Research Gap Analyzer")

uploaded_files = st.file_uploader(
    "Upload Research Papers (PDF)", 
    type=["pdf"], 
    accept_multiple_files=True
)

documents = []

if uploaded_files:
    for pdf in uploaded_files:
        raw_text = extract_text_from_pdf(pdf)
        clean_text = preprocess_text(raw_text)
        documents.append(clean_text)

    model, vectorizer = extract_topics(documents)
    gaps = identify_gaps(model, vectorizer.get_feature_names_out())

    st.subheader("Identified Research Themes")
    st.json(gaps)

