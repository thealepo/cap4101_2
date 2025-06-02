import streamlit as st
import pandas as pd
import numpy as np
import requests


def main():
    # ----- Step 1: Basic Setup and Title -----
    st.title("My Fitness App")
    st.subheader("Powered by Fitness Calculator API")
    st.info("Enter a city and select options to view its current weather data.")

    home , bmi , bmr = st.tabs(["Home" , "BMI Calculator" , "BMR Calculator"])

    with home:
        st.header("Home")

    with bmi:
        st.header("BMI Calculator")

        unit = st.selectbox("Enter preferred units" , ("Metric (kg, m)" , "Imperial (lb, in)"))
        if unit == "Imperial (lb, in)":
            height = st.text_input("Enter your height (in): ")
            weight = st.text_input("Enter your weight (lbs): ")
        else:
            height = st.text_input("Enter your height (m): ")
            weight = st.text_input("Enter your weight (kg): ")
        
        submitted = st.button("Submit")
        
        if submitted:

            if unit == "Imperial (lb, in)":
                url = "https://health-calculator-api.p.rapidapi.com/bmi/imperial"
                querystring = {"height":height , "weight":weight}
                headers = {"x-rapidapi-host": "health-calculator-api.p.rapidapi.com"}
                response = requests.get(url , headers=headers , params=querystring)
            else:
                url = "https://health-calculator-api.p.rapidapi.com/bmi"
                querystring = {"height":height , "weight":weight , "units":"metric"}
                headers = {"x-rapidapi-host": "health-calculator-api.p.rapidapi.com"}
                response = requests.get(url , headers=headers , params=querystring)

            data = response.json()
            st.write(data)

if __name__ == "__main__":

    main()