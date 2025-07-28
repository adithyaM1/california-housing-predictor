# Step-by-step ML Assignment: California Housing Prediction

# File 1: app.py (Main Streamlit App)

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load dataset
@st.cache_data
def load_data():
    data = fetch_california_housing()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = data.target
    return df

df = load_data()

# Sidebar - Feature inputs
st.sidebar.header("Input Features")
input_data = {}
for col in df.columns[:-1]:
    input_data[col] = st.sidebar.slider(col, float(df[col].min()), float(df[col].max()), float(df[col].mean()))

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Train-test split
X = df.drop('Target', axis=1)
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction
prediction = model.predict(input_df)[0]
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Display Results
st.title("California Housing Price Predictor")
st.write("Predicted Median House Value: $", round(prediction * 100000, 2))

st.subheader("Model Performance Metrics")
st.write(f"**MAE**: {mae:.2f}")
st.write(f"**MSE**: {mse:.2f}")
st.write(f"**R² Score**: {r2:.2f}")

# Save model (optional for deployment)
joblib.dump(model, "housing_model.pkl")
