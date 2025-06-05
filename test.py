import streamlit as st
import pandas as pd
import numpy as np
import requests
from config import API_KEY


def main():
    # ----- Step 1: Basic Setup and Title -----
    st.title("My Fitness App")
    st.subheader("Powered by Health API")
    st.info("Enter a city and select options to view its current weather data.")

    home , bmi , bmr , dcr = st.tabs(["Home" , "BMI Calculator" , "BMR Calculator" , "Bulk/Cut Calculator"])

    with home:
        st.header("Home")

    with bmi:
        st.header("BMI Calculator")
        st.write("The Body-Mass Index (BMI) is a tool that measures the ratio of your height and weight to estimate the amount of body fat you have. Although not the perfect tool, it is often used in conjunction with other tools to assess one's overall health status and risks of illnesses. Below you can calculate your own BMI.")

        unit = st.selectbox("Enter preferred units" , options=("Metric (kg, cm)" , "Imperial (lb, in)") , key=5)
        if unit == "Imperial (lb, in)":
            height = st.text_input("Enter your height (in): " , key=6)
            weight = st.text_input("Enter your weight (lbs): " , key=7)
        else:
            height = st.text_input("Enter your height (cm): " , key=8)
            weight = st.text_input("Enter your weight (kg): " , key=9)

        height = float(height) ; weight = float(weight)
        
        submitted = st.button("Submit" , key=20)
        
        if submitted:

            if unit == "Imperial (lb, in)":
                url = "https://health-calculator-api.p.rapidapi.com/bmi/imperial"
                querystring = {"height":height , "weight":weight}
                headers = {"x-rapidapi-host": "health-calculator-api.p.rapidapi.com"}
                response = requests.get(url , headers=headers , params=querystring)
            else:
                url = "https://health-calculator-api.p.rapidapi.com/bmi"
                querystring = {"height":height , "weight":weight , "units":"metric"}
                headers = {
                    "x-rapidapi-key": API_KEY,
                    "x-rapidapi-host": "health-calculator-api.p.rapidapi.com"
                }
                response = requests.get(url , headers=headers , params=querystring)
                
            if response.status_code == 200:
                data = response.json()
    
    with bmr:
        st.header("BMR Calculator")

        unit = st.selectbox("Enter preferred units" , options=("Metric (kg, cm)" , "Imperial (lb, in)") , key=4)

        sex = st.selectbox("Enter your sex: " , ("Male" , "Female") , key=21)
        age = st.number_input("Enter your age: " , min_value=1 , max_value=100 , value=25 , key=22)
        if unit == "Imperial (lb, in)":
            height = st.text_input("Enter your height (in): " , key=10)
            weight = st.text_input("Enter your weight (lbs): " , key=11)
        else:
            height = st.text_input("Enter your height (cm): " , key=12)
            weight = st.text_input("Enter your weight (kg): " , key=13)

        height = float(height) ; weight = float(weight)

        submitted = st.button("Submit" , key=19)

        if submitted:

            url = "https://health-calculator-api.p.rapidapi.com/bmr"
            querystring = {"age":age , "weight":weight , "height":height , "gender":sex , "equation":"mifflin"}
            headers = {
                "x-rapidapi-key": API_KEY,
                "x-rapidapi-host": "health-calculator-api.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)

            if response.status_code == 200:
                data = response.json()

    with dcr:
        st.header("Bulk/Cut Calculator")

        unit = st.selectbox("Enter preferred units: " , options=("Metric (kg, cm)" , "Imperial (lb, in)") , key=3)

        sex = st.selectbox("Enter your sex: " , ("Male" , "Female") , key=1)
        age = st.number_input("Enter your age: " , min_value=1 , max_value=100)
        if unit == "Imperial (lb, in)":
            height = st.text_input("Enter your height (in): " , key=14)
            weight = st.text_input("Enter your weight (lbs): " , key=15)
        else:
            height = st.text_input("Enter your height (cm): " , key=16)
            weight = st.text_input("Enter your weight (kg): " , key=17)
        level = st.select_slider("Enter your activity level: " , (
            "Sedentary" , "Lightly Active" , "Moderately Active" , "Very Active" , "Extremely Active"
        ) , value="Moderately Active")
        goal = st.selectbox("Enter your goal: " , ("Cut" , "Maintain" , "Bulk") , index=1, key=2)

        height = float(height) ; weight = float(weight)
        if unit == "Imperial (lb, in)":
            height *= 2.54
            weight *= 0.4536

        level_map = {
            "Sedentary": "sedentary",
            "Lightly Active": "lightly_active",
            "Moderately Active": "moderately_active",
            "Very Active": "very_active",
            "Extremely Active": "extra_active"
        }
        level = level_map.get(level)

        goal_map = {
            "Cut": "weight_loss",
            "Maintain": "maintenance",
            "Bulk": "weight_gain"
        }
        goal = goal_map.get(goal)


        submitted = st.button("Submit" , key=18)

        if submitted:
            url = "https://health-calculator-api.p.rapidapi.com/dcn"
            querystring = {"age":age , "weight":weight , "height":height , "gender":sex , "activity_level":level , "goal":goal , "equation":"mifflin"}
            headers = {
                "x-rapidapi-key": API_KEY,
                "x-rapidapi-host": "health-calculator-api.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)

            if response.status_code == 200:
                data = response.json()


if __name__ == "__main__":
    main()