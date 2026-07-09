import streamlit as st


def render_header():
    """
    Renders application header.

    Returns
    -------
    tuple
        uploaded_file, identify_button
    """

    title_col, action_col = st.columns(
        [4, 1]
    )

    # ------------------------------------------------------
    # TITLE
    # ------------------------------------------------------

    with title_col:

        st.markdown(
            "# 🪑 PRL Furniture AI"
        )

        st.markdown(
            """
            <div style="
                margin-top:-14px;
                font-size:20px;
                color:#555;
            ">
                Identify Polish Mid-Century Furniture from a single photo
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ------------------------------------------------------
    # ACTIONS
    # ------------------------------------------------------

    with action_col:

        st.markdown(
            "<div style='height:10px'></div>",
            unsafe_allow_html=True,
        )

        uploaded_file = st.file_uploader(
            "Upload Photo",
            type=[
                "jpg",
                "jpeg",
                "png",
            ],
            label_visibility="collapsed",
        )

        identify_button = st.button(
            "🔍 Identify",
            type="primary",
            use_container_width=True,
            disabled=uploaded_file is None,
        )

    st.markdown(
        "<div style='margin-top:-8px'></div>",
        unsafe_allow_html=True,
    )

    st.divider()

    return (
        uploaded_file,
        identify_button,
    )