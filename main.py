from datetime import datetime
# from sklearn import 
import sklearn
import streamlit as st
import pandas as pd
# import lib.metadata.Package
import pickle
with open('D:\Flight_fare prediciton model\Flight_fare\Project\Flight_fare.pkl',"rb") as fr:
    model =pickle.load(fr)
st.title("Flight Fare Predictor")

with st.form("flight_form"):
    # Date and Time of Journey
    dep_date = st.date_input("Departure Date")
    dep_time = st.time_input("Departure Time")

    arr_date = st.date_input("Arrival Date")
    arr_time = st.time_input("Arrival Time")


# Combine into datetime objects
    
    date_dep = datetime.combine(dep_date, dep_time)
    date_arr = datetime.combine(arr_date, arr_time)


    # Total Stops
    Total_Stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])

    # Airline
    airline = st.selectbox("Airline", ['Jet Airways', 'IndiGo', 'Air India', 'Multiple carriers', 'SpiceJet', 'Vistara', 'GoAir', 'Other'])

    # Source
    Source = st.selectbox("Source", ['Delhi', 'Kolkata', 'Mumbai', 'Chennai'])

    # Destination
    Destination = st.selectbox("Destination", ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata'])

    submitted = st.form_submit_button("Submit")

if submitted:
    # Extracting date and time parts
    journey_day = date_dep.day
    journey_month = date_dep.month
    dep_hour = date_dep.hour
    dep_min = date_dep.minute
    arrival_hour = date_arr.hour
    arrival_min = date_arr.minute

    # Duration calculation
    Duration_hour = abs(arrival_hour - dep_hour)
    Duration_mins = abs(arrival_min - dep_min)

    # Airline one-hot encoding
    Airline_AirIndia = int(airline == 'Air India')
    Airline_GoAir = int(airline == 'GoAir')
    Airline_IndiGo = int(airline == 'IndiGo')
    Airline_JetAirways = int(airline == 'Jet Airways')
    Airline_MultipleCarriers = int(airline == 'Multiple carriers')
    Airline_SpiceJet = int(airline == 'SpiceJet')
    Airline_Vistara = int(airline == 'Vistara')
    Airline_Other = int(airline not in ['Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Multiple carriers', 'SpiceJet', 'Vistara'])

    # Source one-hot encoding
    Source_Delhi = int(Source == 'Delhi')
    Source_Kolkata = int(Source == 'Kolkata')
    Source_Mumbai = int(Source == 'Mumbai')
    Source_Chennai = int(Source == 'Chennai')

    # Destination one-hot encoding
    Destination_Cochin = int(Destination == 'Cochin')
    Destination_Delhi = int(Destination == 'Delhi')
    Destination_Hyderabad = int(Destination == 'Hyderabad')
    Destination_Kolkata = int(Destination == 'Kolkata')



    # You can now pass these values into your ML model for fare prediction

    # inputs= [[Depart_time,Arrival_time,selected_Sources,selected_Dest,select_stops,select_Airline]]
    if Source == Destination :
        prediction = 0
        st.subheader("Destination and Source must be different")
    else: 
        prediction=model.predict([[
                Total_Stops,
                journey_day,
                dep_hour,
            dep_min,
            arrival_hour,
            arrival_min,
            Duration_hour,
            Duration_mins,
            Airline_AirIndia,
            Airline_GoAir,
            Airline_IndiGo,
            Airline_JetAirways,
            Airline_MultipleCarriers,
            Airline_Other,
            Airline_SpiceJet,
            Airline_Vistara,
            Source_Chennai,
            Source_Kolkata,
            Source_Mumbai,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
        ]])
        # final =prediction.flatten().astype(float)
        price = int(prediction)
        st.success(f"The predicted price will be INR {price}")

