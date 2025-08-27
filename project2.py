import pickle
import pandas as pd
import streamlit as st


model = pickle.load(open('car prices.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

st.title('The Most Suitable Car for You')
st.info('If you want to buy or sell a car, this program is suitable for you.')

st.sidebar.header("Feature Selection")


cars_by_company = {
    "FERRARI": ["SF90 STRADALE", "F8 TRIBUTO", "812 GTS", "PORTOFINO", "ROMA", "MONZA SP2", "F8 SPIDER", "PORTOFINO M", "ROMA SPIDER"],
    "ROLLS ROYCE": ["PHANTOM", "GHOST", "WRAITH", "DAWN", "CULLINAN", "PHANTOM EXTENDED", "GHOST EXTENDED"],
    "Ford": ["KA+"],
    "MERCEDES": ["GT 63 S", "BENZ S-CLASS S 580", "BENZ E-CLASS E 63 S", "BENZ CLA 45 AMG", "BENZ GLE 63 S"],
    "AUDI": ["AUDI R8 GT", "R8 V10 PLUS", "RS7 SPORTBACK", "RS6 AVANT", "Q7", "Q5", "A8"],
    "BMW": ["M5 CS", "M4 GTS", "M3 COMPETITION", "M2 CS", "X5 M COMPETITION", "X3 M COMPETITION", "I8 ROADSTER"],
    "ASTON MARTIN": ["VANTAGE F1", "VALKYRIE", "VALHALLA", "DBS SUPERLEGGERA", "DB11", "VANTAGE", "DBX"],
    "BENTLEY": ["CONTINENTAL GT AZURE"],
    "LAMBORGHINI": ["VENENO ROADSTER", "SIAN", "AVENTADOR SVJ", "HURACAN EVO", "URUS"],
    "TOYOTA": ["CAMRY", "COROLLA", "PRIUS", "RAV4", "LAND CRUISER", "HIGHLANDER", "SIENNA", "TUNDRA", "YARIS"],
    "NISSAN": ["GT-R", "370Z", "ALTIMA", "MAXIMA", "SENTRA", "ROGUE"],
    "VOLVO": ["XC90", "XC60", "S90"],
    "KIA": ["SPORTAGE LX", "SPORTAGE EX", "SPORTAGE GT-LINE", "SPORTAGE SX TURBO"],
    "HONDA": ["CIVIC TYPE R", "ACCORD", "CR-V", "PILOT", "CIVIC HATCHBACK", "CITY"],
    "HYUNDAI": ["I10", "I20", "ELANTRA", "SANTA FE", "TUCSON", "SONATA", "PALISADE"],
    "MAHINDRA": ["XUV500", "SCORPIO", "THAR"],
    "MARUTI SUZUKI": ["SWIFT", "DZIRE", "BREZZA"],
    "Volkswagen": ["GOLF", "PASSAT", "TIGUAN", "JETTA", "POLO", "ARTEON", "ID.4"],
    "Porsche": ["911", "CAYENNE", "TAYCAN", "PANAMERA"],
    "Tesla": ["Model S", "Model 3", "Model X", "Model Y"],

}

Company_Names = st.selectbox("Select Company Name", list(cars_by_company.keys()))


Cars_Names = st.selectbox("Select Car Name", cars_by_company.get(Company_Names, []))

Fuel_Types = st.selectbox("Select Fuel Types", [
    'plug in hyrbrid', 'Petrol', 'Diesel', 'Hybrid', 'Electric', 'Petrol/Diesel',
    'Plug-in Hybrid', 'Petrol/AWD', 'Petrol/Hybrid', 'Hydrogen', 'Diesel/Petrol',
    'Petrol/EV', 'Hybrid/Electric', 'Petrol, Hybrid', 'Petrol, Diesel',
    'Hybrid (Petrol)', 'CNG/Petrol', 'Hybrid/Petrol', 'Diesel Hybrid',
    'Petrol (Hybrid)', 'Hybrid (Gas + Electric)', 'Gas / Hybrid',
    'Hybrid / Plug-in'
])

Engines = st.text_input('Engines (V8 , V12, V...)')
HorsePower = st.text_input('HorsePower (e.g., 963 hp)')
Cleaned_Capacity = st.text_input('Cleaned Capacity (CC/Battery Capacity)')
Total_Speed = st.text_input('Total Speed (e.g., 250 km/h)')
Performance = st.text_input('Performance (0 - 100 KM/H) (e.g., 7.2 sec)')
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












