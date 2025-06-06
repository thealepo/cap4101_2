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
        if unit == "Imperial (lb, in)":
            height *= 2.54
            weight *= 0.4536

        if user == "Advanced":
            if unit == "Imperial (lb, in)":
                waist = st.number_input("Enter your waist circumference (in): " , key=6)
                wrist = st.number_input("Enter your wrist circumference (in): " , key=7)
            else:
                waist = st.number_input("Enter your waist circumference (cm): " , key=8)
                wrist = st.number_input("Enter your wrist circumference (cm): " , key=9)
            
            waist = float(waist) ; wrist = float(wrist)
            if unit == "Imperial (lb, in)":
                waist *= 2.54 ; wrist *= 2.54

            submitted = st.button("Submit" , key=10)

            if submitted:

                url_bfsi = "https://health-calculator-api.p.rapidapi.com/bfsi"
                querystring_bfsi = {"sex":sex,"height":height,"wrist":wrist}
                headers_ibw = {
                    "x-rapidapi-key": API_KEY,
                    "x-rapidapi-host": "health-calculator-api.p.rapidapi.com"
                }
                response_bfsi = requests.get(url_bfsi, headers=headers_ibw, params=querystring_bfsi)
                data_bfsi = response_bfsi.json()

                bfsi = data_bfsi['BFSI']
                frame = data_bfsi['Frame Size']

                url_ibw = "https://health-calculator-api.p.rapidapi.com/ibw"
                querystring_ibw = {"height":height,"body_frame":frame,"gender":sex,"formula":"hamwi"}
                headers_ibw = {
                    "x-rapidapi-key": API_KEY,
                    "x-rapidapi-host": "health-calculator-api.p.rapidapi.com"
                }
                response_ibw = requests.get(url_ibw, headers=headers_ibw, params=querystring_ibw)
                data_ibw = response_ibw.json()

                ideal_weight = data_ibw['ideal_weight']

                url_absi = "https://health-calculator-api.p.rapidapi.com/absi"
                querystring_absi = {"sex":sex,"age":age,"height":height,"weight":weight,"waist_circumference":waist,"unit":"metric"}
                headers_absi = {
                "x-rapidapi-key": API_KEY,
                "x-rapidapi-host": "health-calculator-api.p.rapidapi.com"
                }
                response_absi = requests.get(url_absi, headers=headers_absi, params=querystring_absi)
                data_absi = response_absi.json()

                absi = data_absi['ABSI']
                z_score = data_absi['ABSI z-score']
                mortality = data_absi['Mortality risk']





