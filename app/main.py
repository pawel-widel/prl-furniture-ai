import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from services.identification_runner import run_identification
from services.photo_service import get_main_reference_image
from services.image_service import prepare_image

from ui.header import render_header
from ui.results import render_results
from ui.technical_details import render_technical_details


st.set_page_config(
    page_title="PRL Furniture AI",
    page_icon="🪑",
    layout="wide",
)

# ======================================================
# HEADER
# ======================================================

uploaded_file, identify_button = render_header()

# ======================================================
# IDENTIFICATION
# ======================================================

if uploaded_file is not None and identify_button:

    result = run_identification(
        uploaded_file
    )

    winner = result["winner"]

    # ======================================================
    # PREPARE IMAGES
    # ======================================================

    user_image = prepare_image(
        uploaded_file
    )

    reference_image = None

    reference_image_path = get_main_reference_image(
        winner.reference_id
    )

    if reference_image_path:

        reference_image = prepare_image(
            reference_image_path
        )

    # ======================================================
    # RESULTS
    # ======================================================

    render_results(
        result=result,
        winner=winner,
        user_image=user_image,
        reference_image=reference_image,
    )

    st.divider()

    # ======================================================
    # TECHNICAL DETAILS
    # ======================================================

    render_technical_details(
        result
    )