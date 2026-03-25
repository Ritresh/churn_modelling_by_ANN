import streamlit as st
import numpy as np
import pickle
import os

from tensorflow.keras.models import load_model# type:ignore

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "..", "output", "churn_model.keras")
scaler_path = os.path.join(BASE_DIR, "..", "output", "scaler.pkl")

model = load_model(model_path)
with open(scaler_path, "rb") as f:
    sc = pickle.load(f)

st.title("Customer Churn Prediction")

CreditScore = st.number_input("CreditScore",100)
Age = st.number_input("Age", 18)
Tenure = st.number_input("Tenure", 1)
Balance = st.number_input("Balance", 0.0)

NumOfProducts = st.selectbox(
    "NumOfProducts",
    [1, 2, 3, 4]
)

HasCrCard_text = st.selectbox(
    "Has Credit Card",
    ["No", "Yes"]
)

HasCrCard = 1 if HasCrCard_text == "Yes" else 0

IsActiveMember_text = st.selectbox(
    "Is Active Member",
    ["No", "Yes"]
)

IsActiveMember = 1 if IsActiveMember_text == "Yes" else 0

EstimatedSalary = st.number_input(
    "Estimated Salary",
    0.0,
    200000.0,
    50000.0
)

Geography = st.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

Gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

# one hot encoding like training
Geography_Germany = 1 if Geography == "Germany" else 0
Geography_Spain = 1 if Geography == "Spain" else 0

Gender_Male = 1 if Gender == "Male" else 0

if st.button("Predict"):

    data = np.array([[
        CreditScore,
        Age,
        Tenure,
        Balance,
        NumOfProducts,
        HasCrCard,
        IsActiveMember,
        EstimatedSalary,
        Geography_Germany,
        Geography_Spain,
        Gender_Male
    ]])

    data = sc.transform(data)
    pred = model.predict(data)
    if pred[0][0] > 0.5:
        st.error("Customer will Exit")
    else:
        st.success("Customer will Stay")