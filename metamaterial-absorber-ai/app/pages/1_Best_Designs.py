import pandas as pd
import streamlit as st

from app.utils.selection import top_n_designs

st.header("Best Designs")

sample = pd.DataFrame(
    {
        "design_id": ["D1", "D2", "D3", "D4"],
        "absorption": [0.92, 0.88, 0.95, 0.90],
        "bandwidth": [1.2, 1.4, 1.1, 1.3],
    }
)

n = st.slider("Top N", min_value=1, max_value=len(sample), value=3)
ranked = top_n_designs(sample, target_col="absorption", n=n)

st.dataframe(ranked, use_container_width=True)
