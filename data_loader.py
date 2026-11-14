from pathlib import Path

import pandas as pd
import streamlit as st


DATA_DIR = Path(__file__).resolve().parent / "file_csv"


@st.cache_data(show_spinner=False)
def load_csv(filename):
    """Load a CSV from the project's file_csv directory with Streamlit caching."""
    return pd.read_csv(DATA_DIR / filename)
