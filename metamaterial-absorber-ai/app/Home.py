import streamlit as st

st.set_page_config(page_title="Metamaterial Absorber AI", layout="wide")

st.title("Metamaterial Absorber AI")
st.write(
    "A lightweight Streamlit workspace for exploring best designs, inverse design, sensing workflows, and AI-assisted research."
)

st.markdown(
    """
### Modules
- **Best Designs**: Browse and filter candidate geometries.
- **Inverse Design**: Predict geometry settings from target responses.
- **Sensing**: Simple signal preprocessing and feature extraction.
- **AI Researcher**: Chat-style helper for notes and ideation.
"""
)
