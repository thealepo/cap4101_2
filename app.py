import streamlit as st
import numpy as np
import pandas as pd
import requests
from config import API_KEY

def main():
    st.title("My Fitness App")
    st.subheader("Powered by Health API")
    st.info("...")  # ADD INFO

    standard = st.tabs(['Standard'])

    with standard:
        st.header("Calorie Calculator")
        st.write("...")  # ADD INFO

        user = st.radio("." , options=("Basic" , "Advanced") , index=None , key=0)
        unit = st.selectbox("Enter preferred units" , options=("Metric (kg, cm)" , "Imperial (lb, in)") , key=1)

        sex = st.selectbox("Enter your sex: " , ("Male" , "Female") , key=2)
        age = st.number_input("Enter your age: " , min_value=1 , max_value=80 , value=25 , key=3)
        if unit == "Imperial (lb, in)":
            height = st.number_input("Enter your height (in): " , key=4)
            weight = st.number_input("Enter your weight (lb): " , key=5)
        else:
            height = st.number_input("Enter your height (cm): " , key=6)
            weight = st.number_input("Enter your weight (kg): " , key=7)
        level = st.select_slider("Activity Level: " , (
            "Sedentary" , "Lightly Active" , "Moderately Active" , "Very Active" , "Extremely Active"
        ) , value="Moderately Active" , key=8)
        goal = st.selectbox("Fitness Goal: " , ("Cut" , "Maintain" , "Bulk") , index=1 , key=9)
        diet = None ; climate = "Average"
        if user == "Advanced":
            diet = st.selectbox("Dietary Preference: " , (
                "Regular" , "Vegetarian" , "Vegan" , "Gluten-Free" , "Pescetarian"
            ) , key=10)
            climate = st.select_slider("Climate (for water intake): " , ("Cold" , "Average" , "Hot") , value="Average" , key=11)

        height = float(height) ; weight = float(weight)
        if unit == "Imperial (lb, in)":
            height *= 2.54
            weight *= 0.4536

        level_json , goal_json , diet_json , climate_json = maps(level , goal , diet , climate)

        submitted = st.button("Submit", key=12)
        if submitted:
            # === Daily Calorie Needs ===
            url = "https://health-calculator-api.p.rapidapi.com/dcn"
            querystring = {
                "age": age,
                "weight": weight,
                "height": height,
                "gender": sex,
                "activity_level": level_json,
                "goal": goal_json,
                "equation": "mifflin"
            }
            headers = {
                "x-rapidapi-key": API_KEY,
                "x-rapidapi-host": "health-calculator-api.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)

            if response.status_code == 200:
                data = response.json()
                st.success("Daily Calorie Needs")
                st.write(f"**Goal:** {data['goal']}")
                st.write(f"**Calories:** {data['calories']} kcal/day")
            else:
                st.error("Failed to fetch calorie data.")

            if user == "Advanced":
                # === Daily Water Intake ===
                url_dwi = "https://health-calculator-api.p.rapidapi.com/dwi"
                querystring_dwi = {
                    "weight": weight,
                    "activity_level": level_json,
                    "climate": climate_json,
                    "unit": "liters"
                }
                response_dwi = requests.get(url_dwi, headers=headers, params=querystring_dwi)

                if response_dwi.status_code == 200:
                    data_dwi = response_dwi.json()
                    st.success("Daily Water Intake")
                    st.write(f"**Water Intake Recommendation:** {data_dwi['water_intake']} liters/day")
                else:
                    st.error("Failed to fetch water intake data.")

                # === Macronutrient Distribution ===
                url_macro = "https://health-calculator-api.p.rapidapi.com/mnd"
                querystring_macro = {
                    "activity_level": level_json,
                    "body_composition_goal": goal_json,
                    "dietary_preferences": diet_json
                }
                response_macro = requests.get(url_macro, headers=headers, params=querystring_macro)
                
                if response_macro.status_code == 200:
                    data_macro = response_macro.json()
                    st.success("Macronutrient Distribution")
                    st.write(f"**Carbohydrates:** {data_macro['carbohydrates']} g")
                    st.write(f"**Proteins:** {data_macro['proteins']} g")
                    st.write(f"**Fats:** {data_macro['fats']} g")
                else:
                    st.error("Failed to fetch macronutrient data.")



def maps(levels , goals , diets=None , climates="Average"):
        
        level_map = {
            "Sedentary": "sedentary",
            "Lightly Active": "lightly_active",
            "Moderately Active": "moderately_active",
            "Very Active": "very_active",
            "Extremely Active": "extra_active"
        }
        goal_map = {
            "Cut": "weight_loss",
            "Maintain": "maintenance",
            "Bulk": "weight_gain"
        }
        diet_map = {
             "Regular": None,
             "Vegetarian": "vegetarian",
             "Vegan": "vegan",
             "Gluten-Free": "gluten-free",
             "Pescatarian": "pescatarian"
        }
        climate_map = {
             "Cold": "cold",
             "Average": "average",
             "Hot": "hot"
        }

        return level_map.get(levels) , goal_map.get(goals) , diet_map.get(diets) , climate_map.get(climates)
    

if __name__ == "__main__":
    main()
