import streamlit as st
import numpy as np
import pandas as pd
import requests
from config import API_KEY

def main():
    st.title("My Fitness App")
    st.subheader("Powered by Health API")
    st.info("...")  # ADD INFORMATION AND DESCRIPTION OF WHAT WEB APP DOES

    auto_powered = st.tabs(["..."])

    with auto_powered:
        st.header("Calorie Calculator")
        st.write("Temp description...")

        user = st.radio("." , options=("Basic" , "Advanced") , index=None , help="Select level of yadayadayada. Basic is more geared towards beginners who want a simple report while Advanced contains a lot more details" , key=0)
        unit = st.selectbox("Enter preferred units" , options=("Metric (kg, cm)" , "Imperial (lb, in)") , key=1)

        sex = st.selectbox("Enter your sex: " , ("Male" , "Female") , key=11)
        age = st.number_input("Enter your age: " , min_value=1 , max_value=100 , value=25 , key=12)
        if unit == "Imperial (lb, in)":
            height = st.number_input("Enter your height (in): " , key=2)
            weight = st.number_input("Enter your weight (lb): " , key=3)
        else:
            height = st.number_input("Enter your height (cm): " , key=4)
            weight = st.number_input("Enter your weight (kg): " , key=5)

        height = float(height) ; weight = float(weight)

        if user == "Advanced":
            if unit == "Imperial (lb, in)":
                waist = st.number_input("Enter your waist circumference (in): " , key=6)
                wrist = st.number_input("Enter your wrist circumference (in): " , key=7)
            else:
                waist = st.number_input("Enter your waist circumference (cm): " , key=8)
                wrist = st.number_input("Enter your wrist circumference (cm): " , key=9)
            
            waist = float(waist) , wrist = float(wrist)

            submitted = st.button("Submit" , key=10)