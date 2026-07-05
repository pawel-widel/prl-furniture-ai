import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from services.identification_service import identify

st.set_page_config(
    page_title="PRL Furniture AI",
    page_icon="🪑",
)

st.title("PRL Furniture Recognition")

st.write("Welcome to my hobby project!")

st.write("This application will help identify Polish PRL furniture using AI.")

uploaded_file = st.file_uploader(
    "Upload a furniture photo",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded photo",
        use_container_width=True,
    )

    if st.button("🔍 Identify furniture"):

        result = identify(uploaded_file)

        st.subheader("Identification result")

        st.write(result)