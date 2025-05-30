import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("Music Generator App")

    home = st.tabs(['Home'])

    with home:
        st.header("Home")

        st.file_uploader(type=['jpg','jpeg','png'])