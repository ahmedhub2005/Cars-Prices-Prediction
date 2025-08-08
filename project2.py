import pickle
import pandas as pd
import streamlit as st


model = pickle.load(open('car prices.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

st.title('The Most Suitable Car for You')
st.info('if you want buy or sell car this program suitable for you.')

st.sidebar.header("Feature Selection")

Company_Names = st.text_input('Company Names (capital letters)')
Cars_Names = st.text_input('Cars Names (capital letters)')
Engines = st.text_input('Engines')
HorsePower = st.text_input('HorsePower (e.g., 963 hp)')
Cleaned_Capacity = st.text_input('Cleaned Capacity(CC/Battery Capacity)')
Total_Speed = st.text_input('Total Speed (e.g., 250 km/h)')
Performance = st.text_input('Performance(0 - 100 )KM/H (e.g., 7.2 sec)')
Fuel_Types = st.text_input('Fuel Types')
Seats = st.text_input('Seats')
Torque = st.text_input('Torque (e.g., 400 Nm)')

def extract_number(value):
    try:
        return float(''.join(c for c in value if c.isdigit() or c == '.'))
    except:
        return None

con = st.sidebar.button("Confirm")

if con:
    if '' in [Company_Names, Cars_Names, Engines, Cleaned_Capacity, HorsePower, Total_Speed, Performance, Fuel_Types, Seats, Torque]:
        st.sidebar.warning("Please fill in all the fields before confirming.")
    else:
        try:
            df = pd.DataFrame({
                'Company Names': [Company_Names],
                'Cars Names': [Cars_Names],
                'Engines': [Engines],
                'Fuel Types': [Fuel_Types],
                'Cleaned Capacity': [extract_number(Cleaned_Capacity)], 
                'HorsePower': [extract_number(HorsePower)],
                'Seats': [int(Seats)],
                'Torque': [extract_number(Torque)],
                'Total_Speed': [extract_number(Total_Speed)],
                'Performance': [extract_number(Performance)],
                })



            df_encoded = pd.get_dummies(df)
            for col in model_columns:
                if col not in df_encoded.columns:
                    df_encoded[col] = 0
            df_encoded = df_encoded[model_columns]

           
            df_scaled = scaler.transform(df_encoded)

          
            prediction = model.predict(df_scaled)[0]
            prediction = max(0, prediction)
            st.sidebar.success(f"Predicted Car Price: {prediction:,.2f}$")

        except Exception as e:
            st.sidebar.error(f"An error occurred during prediction:\n\n{e}")











