import time

import streamlit as st

from services.identification_service import identify


def run_identification(uploaded_file):
    """
    Runs the identification pipeline with
    a user-friendly progress screen.
    """

    status = st.status(
        "🪑 Analyzing furniture...",
        expanded=True,
    )

    # ------------------------------------------------------
    # STEP 1
    # ------------------------------------------------------

    status.write(
        "⏳ Vision Analysis"
    )

    time.sleep(0.25)

    # ------------------------------------------------------
    # STEP 2
    # ------------------------------------------------------

    status.write(
        "⏳ Candidate Search"
    )

    time.sleep(0.25)

    # ------------------------------------------------------
    # STEP 3
    # ------------------------------------------------------

    status.write(
        "⏳ AI Verification"
    )

    time.sleep(0.25)

    # ------------------------------------------------------
    # IDENTIFICATION
    # ------------------------------------------------------

    result = identify(
        uploaded_file
    )

    # ------------------------------------------------------
    # FINISH
    # ------------------------------------------------------

    status.update(
        label="✅ Identification completed",
        state="complete",
    )

    return result