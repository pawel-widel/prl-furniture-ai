import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from services.identification_service import identify

st.set_page_config(
    page_title="PRL Furniture AI",
    page_icon="🪑",
    layout="wide",
)

# ======================================================
# HEADER
# ======================================================

st.markdown("# 🪑 PRL Furniture AI")

st.markdown(
    "### Identify Polish Mid-Century Furniture from a single photo"
)

st.divider()

# ======================================================
# UPLOAD
# ======================================================

uploaded_file = st.file_uploader(
    "Upload a furniture photo",
    type=["jpg", "jpeg", "png"],
)

if uploaded_file is not None:

    if st.button(
        "🔍 Identify furniture",
        type="primary",
        width="stretch",
    ):

        with st.spinner("Analyzing furniture..."):

            result = identify(uploaded_file)

        winner = result["winner"]

        # ======================================================
        # MAIN LAYOUT
        # ======================================================

        left_col, center_col, right_col = st.columns(
            [1, 1.4, 1]
        )

        # ------------------------------------------------------
        # USER PHOTO
        # ------------------------------------------------------

        with left_col:

            st.subheader("📷 Your Photo")

            st.image(
                uploaded_file,
                use_container_width=True,
            )

        # ------------------------------------------------------
        # WINNER
        # ------------------------------------------------------

        with center_col:

            st.subheader("🏆 Best Match")

            st.info(
                "Reference photo will appear here in the next iteration."
            )

            st.markdown(f"## {winner.model}")

            if result["verification"]:

                verification = result["verification"]

                confidence = int(
                    verification["confidence"] * 100
                )

                st.metric(
                    "Confidence",
                    f"{confidence}%",
                )

                st.markdown("### Why this match?")

                for feature in verification["matched_features"]:

                    st.write(f"✅ {feature}")

            else:

                st.warning(
                    "No candidate passed verification."
                )

        # ------------------------------------------------------
        # TOP 3
        # ------------------------------------------------------

        with right_col:

            st.subheader("📊 Similar Models")

            max_score = max(
                candidate["score"]
                for candidate in result["candidates"]
            )

            for candidate in result["candidates"][:3]:

                furniture = candidate["furniture"]

                score = candidate["score"]

                percent = int(
                    (score / max_score) * 100
                )

                st.write(f"**{furniture.model}**")

                st.progress(percent / 100)

                st.caption(f"{percent}% similarity")

                st.write("")

        st.divider()

        # ======================================================
        # TECHNICAL DETAILS
        # ======================================================

        with st.expander(
            "⚙️ Technical Details",
            expanded=False,
        ):

            st.subheader("Vision Features")

            st.json(result["features"])

            st.divider()

            st.subheader("Search Ranking")

            for index, candidate in enumerate(
                result["candidates"],
                start=1,
            ):

                st.write(
                    f"{index}. "
                    f"{candidate['furniture'].model} "
                    f"(Score: {candidate['score']})"
                )

            st.divider()

            st.subheader("Verification Results")

            for item in result["verification_results"]:

                verification = item["verification"]

                st.markdown("---")

                st.markdown(
                    f"### {item['furniture'].model}"
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

                st.write(
                    verification["reason"]
                )

                if verification["matched_features"]:

                    st.markdown("**Matched features**")

                    for feature in verification["matched_features"]:

                        st.write(f"✅ {feature}")

                if verification["different_features"]:

                    st.markdown("**Different features**")

                    for feature in verification["different_features"]:

                        st.write(f"❌ {feature}")