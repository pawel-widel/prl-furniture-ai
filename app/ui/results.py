import streamlit as st


def render_results(
    *,
    result,
    winner,
    user_image,
    reference_image,
):
    """
    Render identification results.
    """

    verification = result["verification"]

    confidence = 100

    if verification:

        confidence = int(
            verification["confidence"] * 100
        )

    # ======================================================
    # MAIN LAYOUT
    # ======================================================

    user_col, winner_col, top_col = st.columns(
        [1, 1.2, 1]
    )

    # ------------------------------------------------------
    # USER PHOTO
    # ------------------------------------------------------

    with user_col:

        st.subheader(
            "📷 Your Photo"
        )

        st.image(
            user_image,
            width=420,
        )

    # ------------------------------------------------------
    # BEST MATCH
    # ------------------------------------------------------

    with winner_col:

        st.subheader(
            f"🏆 Best Match: {winner.model}"
        )

        if reference_image:

            st.image(
                reference_image,
                width=420,
            )

        else:

            st.info(
                "No reference image available."
            )

    # ------------------------------------------------------
    # TOP 3 MATCHES
    # ------------------------------------------------------

    with top_col:

        st.subheader(
            "🏆 Top 3 Matches"
        )

        max_score = max(
            candidate["score"]
            for candidate in result["candidates"]
        )

        top_candidates = result["candidates"][:3]

        medals = [
            "🥇",
            "🥈",
            "🥉",
        ]

        for index, candidate in enumerate(
            top_candidates
        ):

            furniture = candidate["furniture"]

            if index == 0:

                percent = confidence

                st.markdown(
                    f"""
                    <div style="
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                        color:#1E7E34;
                        font-weight:700;
                        font-size:18px;
                        margin-bottom:6px;
                    ">
                        <span>{medals[index]} {furniture.model}</span>
                        <span>{percent}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.markdown(
                    f"""
                    <div style="
                        width:100%;
                        height:10px;
                        background:#E5E7EB;
                        border-radius:8px;
                        overflow:hidden;
                        margin-bottom:18px;
                    ">
                        <div style="
                            width:{percent}%;
                            height:10px;
                            background:#22C55E;
                        ">
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            else:

                percent = int(
                    (
                        candidate["score"]
                        / max_score
                    )
                    * confidence
                )

                st.markdown(
                    f"""
                    <div style="
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                        font-weight:600;
                        margin-bottom:6px;
                        margin-top:8px;
                    ">
                        <span>{medals[index]} {furniture.model}</span>
                        <span>{percent}%</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.progress(
                    percent / 100
                )

                st.write("")