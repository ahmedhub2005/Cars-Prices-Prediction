import pickle
import pandas as pd
import streamlit as st


model = pickle.load(open('car prices.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

st.title('The Most Suitable Car for You')
st.info('if you want buy or sell car this program suitable for you.')

st.sidebar.header("Feature Selection")

Company_Names = st.selectbox("Select Company Name ", ['FERRARI' ,'ROLLS ROYCE', 'Ford', 'MERCEDES', 'AUDI', 'BMW' ,'ASTON MARTIN',
 'BENTLEY', 'LAMBORGHINI', 'TOYOTA', 'NISSAN', 'ROLLS ROYCE ' ,'VOLVO' ,'KIA',
 'HONDA', 'KIA  ' ,'HYUNDAI' ,'MAHINDRA', 'MARUTI SUZUKI' ,'Nissan',
 'Volkswagen' ,'Porsche' ,'Cadillac' ,'Tata Motors' ,'Tesla' ,'Jeep', 'Mazda',
 'Chevrolet', 'GMC' ,'Kia' ,'Peugeot', 'Bugatti' ,'Volvo', 'Jaguar Land Rover',
 'Acura', 'Mitsubishi', 'Toyota'])


Cars_Names = category = st.selectbox("Select Car Name ", [
    'SF90 STRADALE', 'PHANTOM', 'KA+', 'GT 63 S', 'AUDI R8 GT', 'MCLAREN 720S', 'VANTAGE F1', 
    'CONTINENTAL GT AZURE', 'VENENO ROADSTER', 'F8 TRIBUTO', '812 GTS', 'PORTOFINO', 'ROMA', 
    'MONZA SP2', 'F8 SPIDER', 'PORTOFINO M', 'ROMA SPIDER', 'GR SUPRA', 'TOYOTA 86', 'TOYOTA GR86', 
    'TOYOTA LAND CRUISER', 'TOYOTA SEQUOIA', 'GT-R', '370Z', 'Z PROTO', 'ALTIMA', 'MAXIMA', 'SENTRA', 
    'ROGUE', 'PATHFINDER', 'FRONTIER', 'TITAN', 'VALKYRIE', 'VALHALLA', 'DBS SUPERLEGGERA', 'DB11', 
    'VANTAGE', 'DBX', 'RAPIDE AMR', 'VANQUISH', 'LAGONDA TARAF', 'VICTOR', 'SIAN', 'AVENTADOR SVJ', 
    'HURACAN PERFORMANTE', 'HURACAN EVO', 'AVENTADOR SV', 'URUS', 'HURACAN SPYDER', 'AVENTADOR ROADSTER', 
    'HURACAN PERFORMANTE SPYDER', 'AVENTADOR S', 'HURACAN EVO SPYDER', 'URUS PERFORMANTE', 
    'AVENTADOR ULTIMAE', 'HURACAN EVO RWD', 'AVENTADOR SVJ ROADSTER', 'URUS S', 'HURACAN STO', 
    'AVENTADOR LP 780-4 ULTIMATE', 'HURACAN EVO RWD SPYDER', 'AVENTADOR SVJ XAGO', 'URUS GRAPHITE CAPSULE', 
    'HURACAN STO EVO', 'AVENTADOR LP 780-4 ULTIMATE ROADSTER', 'GHOST', 'WRAITH', 'DAWN', 'CULLINAN', 
    'PHANTOM EXTENDED', 'GHOST EXTENDED', 'WRAITH BLACK BADGE', 'DAWN BLACK BADGE', 'CULLINAN BLACK BADGE', 
    'PHANTOM COUPE', 'GHOST COUPE', 'WRAITH COUPE', 'DAWN CONVERTIBLE', 'CULLINAN SUV', 'BENZ S-CLASS S 580', 
    'BENZ E-CLASS E 63 S', 'BENZ CLA 45 AMG', 'BENZ GLE 63 S', 'BENZ S-CLASS S 500', 'BENZ E-CLASS E 450', 
    'BENZ CLS 450', 'BENZ GT 53', 'BENZ GLE 450', 'BENZ A-CLASS A 45 S', 'BENZ C-CLASS C 43', 
    'BENZ E-CLASS E 350', 'BENZ GLE 350', 'BENZ GLC 43', 'BENZ GLA 45', 'BENZ GLC 350', 'BENZ GLE 53', 
    'BENZ S-CLASS S 350', 'BENZ EQS 53', 'BENZ MAYBACH S 680', 'M5 CS', 'M4 GTS', 'M3 COMPETITION', 
    'M2 CS', 'X5 M COMPETITION', 'X3 M COMPETITION', 'M8 GRAN COUPE', 'M850I XDRIVE COUPE', 
    'DAWN BLACK BADGE VOLANTE', 'CULLINAN BLACK BADGE SUV', 'PHANTOM TRANQUILITY', 'GHOST ZENITH', 
    'WRAITH EAGLE VIII', 'PHANTOM ORCHID', 'GHOST AZURE', 'WRAITH KRYPTOS', 'DAWN SILVER BULLET', 
    'CULLINAN FUX ORANGE', 'PHANTOM CELESTIAL', 'GHOST MYSORE', 'WRAITH LUMINARY', 'DAWN BLACK BADGE ADAMAS', 
    'CULLINAN RED DIAMOND', 'R8 V10 PLUS', 'RS7 SPORTBACK', 'S8', 'RS6 AVANT', 'S7 SPORTBACK', 'A8', 
    'S5 COUPE', 'SQ5', 'S4 SEDAN', 'S3 SEDAN', 'Q7', 'Q5', 'A7', 'A6', 'A5 COUPE', 'A4', 'Q3', 'E-TRON', 
    'E-TRON SPORTBACK', 'TT COUPE', 'I8 ROADSTER', '330I', 'M340I XDRIVE', '430I COUPE', 'M4 COMPETITION', 
    '530I', 'M550I XDRIVE', '118I', '128TI', 'M135I XDRIVE', '116D', '120D XDRIVE', '116I', '118D', 
    '120I', '125I', '114D', '114I', '125D', '118I XDRIVE', '116D EFFICIENTDYNAMICS', '118I SPORTLINE', 
    '118I M SPORT', '120I M SPORT', '116I EFFICIENTDYNAMICS', '116D ADVANTAGE', '120D EFFICIENTDYNAMICS', 
    '118I SHADOW LINE', '118D SPORT LINE', '120I XDRIVE', '114D SPORT LINE', '118I URBAN LINE', 'XC90', 
    'XC60', 'S90', 'SPORTAGE LX', 'SPORTAGE EX', 'SPORTAGE GT-LINE', 'SPORTAGE SX TURBO', 
    'SPORTAGE NIGHTFALL EDITION', 'CIVIC TYPE R', 'SPORTAGE PHEV', 'SPORTAGE 2024(BASE MODEL)', 
    'SPORTAGE 2024(TOP TRIM)', 'SPORTAGE 2024(BASE AWD)', 'SPORTAGE X-LINE', 'SPORTAGE 2024(S TRIM)', 
    'ACCORD', 'SPORTAGE 2024(HYBRID AWD)', 'SPORTAGE 2024(PLUG-IN HYBRID AWD)', 'SPORTAGE 2024(X-PRO)', 
    'SPORTAGE 2024(X-PRO PRESTIGE)', 'SPORTAGE 2024(SX TURBO AWD)', 'SPORTAGE 2024(BASE FWD)', 'CR-V', 
    'PILOT', 'CIVIC HATCHBACK', 'CAMRY', 'COROLLA', 'PRIUS', 'RAV4', 'HIGHLANDER', '4RUNNER', 'TACOMA', 
    'TUNDRA', 'AVALON', 'MIRAI', 'SIENNA', 'VENZA', 'HIGHLANDER HYBRID', 'LAND CRUISER PRADO', 
    'TUNDRA HYBRID', 'YARIS', 'C-HR', 'BZ4X', 'CROWN', 'MR2', 'CELICA', 'CITY', 'CIVIC', 'I10', 'I20', 
    'ELANTRA', 'XUV500', 'SCORPIO', 'THAR', 'SWIFT', 'DZIRE', 'BREZZA', 'PRIUS PRIME', 'GR COROLLA', 
    'LAND CRUISER 300', 'TUNDRA I-FORCE MAX', 'COROLLA HATCHBACK XSE', 'HILUX GR SPORT', 
    'ALPHARD EXECUTIVE LOUNGE', 'FORTUNER GR SPORT', 'INNOVA HYCROSS', 'COASTER', 'URBAN CRUISER TAISOR', 
    'AYGO X', 'HILUX REVO ROCCO', 'PROACE VERSO ELECTRIC', 'CENTURY SUV', 'COROLLA SEDAN HYBRID', 
    'BZ3', 'GR YARIS', 'SANTA FE', 'IONIQ 5', 'SANTA CRUZ', 'KONA', 'URVAN', 'IONIQ 6', 'TUCSON', 
    'PALISADE', 'SONATA', 'ACCENT', 'VENUE', 'KONA ELECTRIC', 'VELOSTER', 'NEXO;NIO', 'GENESIS', 'AZERA', 
    'EQUUS', 'TIBURON', 'ELANTRA GT', 'GOLF', 'PASSAT', 'TIGUAN', 'JETTA', 'POLO', 'ARTEON', 'ID.4', 
    'UP!', 'TOUAREG', 'SCIROCCO', 'BEETLE', 'AMAROK', 'T-ROC', 'SHARAN', 'CADDY', 'NV1500', 'TAIGO', 
    'CALIFORNIA', 'ID.3', 'ID. BUZZ', 'GOLF GTI', 'GOLF R', 'PASSAT ALLTRACK', 'POLO GTI', 'UP! GTI', 
    'T-CROSS', 'ID.5', 'ID. BUZZ CARGO', 'TOUAREG R', 'MULTIVAN', 'POLO BLUEMOTION', 'GOLF SPORTSVAN', 
    'GOLF ALLTRACK', 'SCIROCCO R', 'TIGUAN ALLSPACE', 'ARTEON 4MOTION', 'ID.4 GTX', 'ID.3 PRO', 
    'GOLF VARIANT', 'CRAFTER', 'LUPO', 'CORRADO', 'PHAETON', 'GOLF CABRIOLET', 'SANTANA', 'POLO VIVO', 
    'KARMANN GHIA', 'FOX', 'VENTO', 'GOLF ELECTRIC', 'BORA', 'TERAMONT', 'TAOS', ])


Fuel_Types = category = st.selectbox("Select Fuel Types", ['plug in hyrbrid' ,'Petrol' ,'Diesel' ,'Hybrid', 'Electric' ,'Petrol/Diesel',
 'Plug-in Hybrid', 'Petrol/AWD' ,'Petrol/Hybrid', 'Hydrogen', 'Diesel/Petrol',
 'Petrol/EV', 'Hybrid/Electric', 'Petrol, Hybrid' ,'Petrol, Diesel',
 'Hybrid (Petrol)', 'CNG/Petrol' ,'Hybrid/Petrol', 'Diesel Hybrid',
 'Petrol (Hybrid)' ,'Hybrid (Gas + Electric)' ,'Gas / Hybrid',
 'Hybrid / Plug-in'])
Engines = st.text_input('Engines')
HorsePower = st.text_input('HorsePower (e.g., 963 hp)')
Cleaned_Capacity = st.text_input('Capacity(CC/Battery Capacity)')
Total_Speed = st.text_input('Total Speed (e.g., 250 km/h)')
Performance = st.text_input('Performance(0 - 100 )KM/H (e.g., 7.2 sec)')
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













