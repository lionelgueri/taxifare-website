import streamlit as st
import requests
from datetime import datetime
import pandas as pd

# TaxiFareModel front
st.title('Taxi Fare Prediction')

st.markdown('''
    Prévoir le prix d'une course de taxi à New York en fonction de la date et l'heure de la course, des coordonnées GPS du lieu de départ et d'arrivée, et du nombre de passagers.
''')

## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# Ask for user input
date_time = st.date_input('Date and Time', datetime.now())
pickup_longitude = st.number_input('Pickup Longitude', value=-74.00597)
pickup_latitude = st.number_input('Pickup Latitude', value=40.71427)
dropoff_longitude = st.number_input('Dropoff Longitude', value=-74.0080678)
dropoff_latitude = st.number_input('Dropoff Latitude', value=40.7052024)
passenger_count = st.number_input('Passenger Count', min_value=1, max_value=8, step=1, value=1)

## Once we have these, let's call our API in order to retrieve a prediction

if st.button('Get Fare'):
    url = 'https://taxifare.lewagon.ai/predict'

    # Build a dictionary containing the parameters for our API
    params = {
        'pickup_datetime': date_time.strftime("%Y-%m-%d %H:%M:%S"),
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    # Call our API using the `requests` package
    response = requests.get(url, params=params)

    # Retrieve the prediction from the **JSON** returned by the API
    prediction = response.json()['fare']

    # Finally, we can display the prediction to the user
    st.write(f'The predicted fare is: {prediction}')

    # Display the map with the pickup location
    st.map(pd.DataFrame({'lat': [pickup_latitude], 'lon': [pickup_longitude]}, columns=['lat', 'lon']))
