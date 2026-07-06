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

        # ---------------------------------------
        # Vision
        # ---------------------------------------

        st.subheader("Vision Features")

        st.json(result["features"])

        # ---------------------------------------
        # Final Result
        # ---------------------------------------

        st.subheader("🏆 Final Identification")

        winner = result["winner"]

        st.write(f"**Model:** {winner.model}")

        if result["verification"]:

            verification = result["verification"]

            st.write(
                f"**Verification confidence:** "
                f"{verification['confidence']:.2f}"
            )

            st.write(
                f"**Reason:** "
                f"{verification['reason']}"
            )

            st.write("### Matched features")

            for feature in verification["matched_features"]:

                st.write(f"✅ {feature}")

            st.write("### Different features")

            for feature in verification["different_features"]:

                st.write(f"❌ {feature}")

        else:

            st.warning(
                "No candidate passed verification. "
                "Showing the best Search result."
            )

        # ---------------------------------------
        # Search ranking
        # ---------------------------------------

        st.subheader("Search Ranking")

        for index, candidate in enumerate(
            result["candidates"],
            start=1,
        ):

            furniture = candidate["furniture"]

            st.write(
                f"{index}. "
                f"{furniture.model} "
                f"(Search score: {candidate['score']})"
            )

        # ---------------------------------------
        # Verification Results
        # ---------------------------------------

        st.subheader("Verification Results")

        for item in result["verification_results"]:

            verification = item["verification"]

            st.write("---")

            st.write(
                f"**{item['furniture'].model}**"
            )

            st.write(
                f"Search score: {item['search_score']}"
            )

            st.write(
                f"Match: {verification['match']}"
            )

            st.write(
                f"Confidence: {verification['confidence']:.2f}"
            )