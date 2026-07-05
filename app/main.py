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

        with st.spinner("Analyzing image..."):

            result = identify(uploaded_file)

        st.subheader("Vision Features")

        st.json(result["features"])

        st.subheader("Top Candidates")

        for index, candidate in enumerate(result["candidates"], start=1):

            furniture = candidate["furniture"]

            st.write(
                f"**{index}. {furniture.model}** "
                f"(score: {candidate['score']})"
            )