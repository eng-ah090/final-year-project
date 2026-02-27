import numpy as np
import streamlit as st

from app.utils.sensing import extract_basic_features

st.header("Sensing")

noise = st.slider("Noise level", 0.0, 1.0, 0.1)
signal = np.sin(np.linspace(0, 4 * np.pi, 200)) + np.random.normal(0, noise, 200)
features = extract_basic_features(signal)

st.line_chart(signal)
st.write(features)
