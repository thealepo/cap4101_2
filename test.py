import streamlit as st
import pandas as pd
import numpy as np
import requests


def main():
    # ----- Step 1: Basic Setup and Title -----
    st.title("My Fitness App")
    st.subheader("Powered by Fitness Calculator API")
    st.info("Enter a city and select options to view its current weather data.")

    # ----- Step 2: User Inputs (Widgets) -----

    # 1) Text input to get city name
    city_name = st.text_input("Enter the name of a city:", "Miami")

    # 2) Checkbox to confirm if user wants to see additional info
    show_extra_info = st.checkbox("Show additional weather information", value=False)

    # 3) A slider for the number of forecast days (hypothetically if you have an endpoint that allows multiple days)
    forecast_days = st.slider("Select the number of days for the forecast:", 1, 7, 3)

    # 4) A radio button to select units (imperial or metric)
    unit = st.radio("Select temperature units:", ("Imperial (°F)", "Metric (°C)"))

    # 5) Button to submit request
    if st.button("Get Weather"):
        st.write(f"Fetching weather data for {city_name} ...")
        # We'll handle the API call in the next step

    # ----- Step 3: Make the API Call -----
    if st.button("Get Weather"):
        # 1) Prepare the request
        api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your key
        units = "imperial" if "Imperial" in unit else "metric"
        url = (
            f"http://api.openweathermap.org/data/2.5/weather"
            f"?q={city_name}&appid={api_key}&units={units}"
        )
        
        # 2) Fetch the data
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()

            # 3) Extract needed information
            weather_main = data["weather"][0]["main"]
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            lat = data["coord"]["lat"]
            lon = data["coord"]["lon"]

            # 4) Display the data in various forms
            st.success("Data fetched successfully!")

            # a) Display main weather info
            st.write(f"**Weather Condition:** {weather_main} - {weather_desc}")
            st.write(f"**Temperature:** {temp}°")
            st.write(f"**Humidity:** {humidity}%")

            # b) Show additional info if checkbox is selected
            if show_extra_info:
                feels_like = data["main"]["feels_like"]
                pressure = data["main"]["pressure"]
                st.write(f"**Feels Like:** {feels_like}°")
                st.write(f"**Pressure:** {pressure} hPa")

            # c) Create a small dataframe for demonstration
            weather_df = pd.DataFrame(
                {
                    "lat": [lat],
                    "lon": [lon],
                    "temperature": [temp],
                    "humidity": [humidity],
                }
            )
            st.dataframe(weather_df)  # Interactive table

            # d) Display a chart (example: bar chart for temperature vs humidity)
            chart_data = pd.DataFrame({
                "Measurement": ["Temperature", "Humidity"],
                "Value": [temp, humidity]
            })
            st.bar_chart(chart_data.set_index("Measurement"))

            # e) Display a map (Streamlit expects columns named "lat" and "lon")
            st.map(weather_df[["lat", "lon"]])

        else:
            st.error(f"Error: Could not retrieve data for {city_name}. Check the city name or API key.")



if __name__ == "__main__":
    main()