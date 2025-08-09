#  Car Price Prediction App


##  Overview
This project is a **Car Price Prediction Web App** built with **Streamlit** and **Machine Learning** models.
The app predicts the most suitable car price for a user based on several features such as:
- Brand
- Model
- Engine Type
- Horsepower
- Torque
- Performance
- And more...

The dataset was cleaned and processed to ensure accurate predictions, and the final model was trained using **DecisionTreeRegressor** and **RandomForestRegressor** after feature engineering and scaling.

---

##  Features
- **Interactive Web App** powered by Streamlit
- Accepts user inputs for multiple car features
- Preprocessing pipeline with:
  - Missing value handling
  - Feature encoding
  - Scaling (StandardScaler)
- Trained on cleaned dataset (2010–2025)
- Real-time prediction

---

##  Dataset
- **Source**: Custom cleaned dataset based on `cars_datasets_2025`
- **Main features**:
  - Company Names
  - Car Names
  - Engine Type
  - HorsePower
  - Cleaned Capacity (CC/Battery)
  - Torque
  - Seats
  - Total Speed
  - Performance (0–100 KM/H)
  - Fuel Type
- Target: **Cars Prices ($)**

---

##  Tech Stack
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- **Streamlit** (Frontend Web App)
- **Pickle** (Model & Scaler serialization)
- **Machine Learning Models**:
  - DecisionTreeRegressor
  - RandomForestRegressor
  - GradientBoostingRegressor
  - LinearRegression
  - KNeighborsRegressor

---

##  How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/car-price-predictor.git
cd car-price-predictor

 Model Training
The training script:

Loads and cleans the dataset

Applies One-Hot Encoding for categorical variables

Scales numerical features using StandardScaler

Trains multiple regression models and evaluates them with R² score

Saves:

Trained model (car prices.sav)

Scaler (scaler.sav)

Model columns (model_columns.pkl)

 Screenshots
Main Page

Prediction Example

 Example Prediction
Company Names	Car Name	Engine	HP	Capacity	Torque	Speed	Perf	Fuel	Seats	Predicted Price
BMW	M5	V8	600	4395	750	305	3.4	Petrol	5	$102,500

 Future Improvements
Add more data for hybrid & electric vehicles

Deploy on Streamlit Cloud / Hugging Face Spaces

Implement advanced models like XGBoost & CatBoost

Add feature importance visualization

 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss your ideas
