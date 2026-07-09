import streamlit as st


def render_technical_details(result):
    """
    Render technical details section.
    """

    with st.expander(
        "⚙️ Technical Details",
        expanded=False,
    ):

        # ==================================================
        # PIPELINE
        # ==================================================

        st.markdown(
            """
### Pipeline

**1️⃣ Vision Analysis** ➜ **2️⃣ Candidate Search** ➜ **3️⃣ AI Verification** ➜ **4️⃣ Final Ranking**
"""
        )

        st.divider()

        # ==================================================
        # VISION FEATURES
        # ==================================================

        st.subheader(
            "👁️ Vision Features"
        )

        st.json(
            result["features"]
        )

        st.divider()

        # ==================================================
        # SEARCH RANKING
        # ==================================================

        st.subheader(
            "🔎 Candidate Search"
        )

        ranking = []

        for index, candidate in enumerate(
            result["candidates"],
            start=1,
        ):

            ranking.append(
                {
                    "Rank": index,
                    "Model": candidate[
                        "furniture"
                    ].model,
                    "Search score": candidate[
                        "score"
                    ],
                }
            )

        st.table(
            ranking
        )

        st.divider()

        # ==================================================
        # VERIFICATION
        # ==================================================

        st.subheader(
            "🤖 AI Verification"
        )

        for item in result[
            "verification_results"
        ]:

            verification = item[
                "verification"
            ]

            confidence = int(
                verification[
                    "confidence"
                ]
                * 100
            )

            with st.container():

                st.markdown(
                    f"### {item['furniture'].model}"
                )

                col1, col2, col3 = st.columns(
                    3
                )

                with col1:

                    st.metric(
                        "Search score",
                        item[
                            "search_score"
                        ],
                    )

                with col2:

                    st.metric(
                        "AI confidence",
                        f"{confidence}%",
                    )

                with col3:

                    st.metric(
                        "Match",
                        "✅ Yes"
                        if verification[
                            "match"
                        ]
                        else "❌ No",
                    )

                st.write(
                    verification[
                        "reason"
                    ]
                )

                if verification[
                    "matched_features"
                ]:

                    st.markdown(
                        "**Matched features**"
                    )

                    for feature in verification[
                        "matched_features"
                    ]:

                        st.write(
                            f"✅ {feature}"
                        )

                if verification[
                    "different_features"
                ]:

                    st.markdown(
                        "**Different features**"
                    )

                    for feature in verification[
                        "different_features"
                    ]:

                        st.write(
                            f"❌ {feature}"
                        )

                st.divider()