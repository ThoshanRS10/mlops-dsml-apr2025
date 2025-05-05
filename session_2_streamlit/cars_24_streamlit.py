# intention is to create a UI where the user can enter features of a car and get a prediction of the price of the car.

import streamlit as st
import pickle

# Ensure joblib is installed by running `pip install joblib` in your terminal before executing this script.
import joblib

st.title("Car Price Prediction App")

# use same encode dictionary as in the training phase to encode our test data also

encode_dict = {
    "fuel_type": {"Diesel": 1, "Petrol": 2, "CNG": 3, "LPG": 4, "Electric": 5},
    "transmission_type": {"Manual": 1, "Automatic": 2},
    "seller_type": {"Dealer": 1, "Individual": 2, "Trustmark Dealer": 3},
}

# Load the model
model = joblib.load('session_2_streamlit\cars24-car-price-model.joblib')

# add widgets for features to get input from user

year = st.slider("Manufacturing Year", min_value = 1990, max_value = 2023, value = 2015, step=1)

seller_type = st.selectbox("Seller Type", ["Dealer", "Individual", "Trustmark Dealer"])

km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=1000000, value=50000, step=5000)

mileage = st.number_input("Mileage (kmpl)", min_value=0.0, max_value=18.0, value=15.0, step=0.5)

max_power = st.number_input("Max Power (bhp)", min_value=0.0, max_value=300.0, value=150.0, step=5.0)

col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Fuel Type", ["Diesel", "Petrol", "CNG", "LPG", "Electric"])	

engine = col2.number_input("Engine (cc)", min_value=500, max_value=5000, value=1500, step=100)

transmission_type = st.selectbox("Transmission Type", ["Manual", "Automatic"])

seats = st.number_input("Seats", min_value=2, max_value=10, value=5, step=1)

# by default, it should not ask for these many input information from the user.

scaler = joblib.load('session_2_streamlit\scaler.pkl') # Load the scaler object for scaling the input data

def model_pred(
    year, seller_type, km_driven, fuel_type, 
    transmission_type, mileage, engine, max_power, seats
): # all these are input features from user
	
		# Convert categorical features/inputs  using the encode dictionary
	seller_type_enc = encode_dict["seller_type"][seller_type] # if someone selects "Dealer" from the dropdown, it will be converted to 1 using the encode dictionary
	fuel_type_enc = encode_dict["fuel_type"][fuel_type]
	transmission_type_enc = encode_dict["transmission_type"][transmission_type]

    # convert all the features/ inputs from user into numerical format is passed into a list .
	data = [[
		float(year),
		seller_type_enc,
		float(km_driven),
		fuel_type_enc,
		transmission_type_enc,
		float(mileage),
		float(engine),
		float(max_power),
		float(seats)
	]]

		# Scale the data, pass it through the scaler object to scale it, from which we have loaded above (scaler.pkl) for std the numerical dataset.
        # The scaler object is used to scale the input data in the same way as the training data was scaled.
	data = scaler.transform(data)

		# Predict
          ## Pass the scaled data to the model to get the prediction.
	prediction = model.predict(data)
	return round(prediction[0], 2)

    

# when the user clicks the button "Predict", the function model_pred is called with the input features from the user.
if st.button("Predict"):
    price = model_pred(
        year, seller_type, km_driven, 
        fuel_type, transmission_type, 
        mileage, engine, max_power, seats
    )
    st.write(f"**Predicted Car Price**: {price} Lakhs (approx.)")
else:
    st.write("Click the **Predict** button once you've entered all the details.")