import sys
from pathlib import Path

# Add the project root to Python's search path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import database.database as db
from services.prompt_builder import build_prompt

st.set_page_config(
    page_title="PRL Furniture AI",
    page_icon="🪑",
)

st.title("PRL Furniture Recognition")

st.write("Welcome to my hobby project!")

st.write("This application will help identify Polish PRL furniture using AI.")

uploaded_file = st.file_uploader(
    "Upload a furniture photo",
    type=["jpg", "jpeg", "png"]
)
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded photo", use_container_width=True
    )
    if st.button("🔍 Identify furniture"):

    

         furniture = db.get_all_furniture()
         prompt = build_prompt(furniture)

         st.success("Knowledge base loaded!")

         st.write(f"Furniture models: {len(furniture)}")

         st.write("First record:")

         first = furniture[0]

         st.subheader(first.model)

         st.write(f"**Common name:** {first.common_name}")
         st.write(f"**Designer:** {first.designer}")
         st.write(f"**Manufacturer:** {first.manufacturer}")
         st.write(f"**Category:** {first.category}")
         st.write(f"**Confidence:** {first.confidence:.0%}")

         st.divider()

         st.subheader("Generated prompt")

         st.text_area(
         "Prompt",
         prompt,
         height=500
)
    