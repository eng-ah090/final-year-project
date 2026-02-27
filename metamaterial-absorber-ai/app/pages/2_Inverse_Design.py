import streamlit as st

from app.utils.inference import infer_geometry_from_target

st.header("Inverse Design")

target_absorption = st.slider("Target absorption", 0.50, 0.99, 0.90)
target_frequency = st.number_input("Target resonance frequency (GHz)", value=10.0, min_value=1.0)

if st.button("Suggest geometry"):
    suggestion = infer_geometry_from_target(
        {"absorption": target_absorption, "frequency": target_frequency}
    )
    st.json(suggestion)
