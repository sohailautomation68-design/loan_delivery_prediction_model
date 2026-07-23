import streamlit as st
import pandas as pd
import joblib 
model=joblib.load("Loan approval.joblib")
sclar=joblib.load("sclar.joblib")
st.title("Loan Approval Prediction System")
st.write("This application predicts whether a loan application is likely to be approved based on the applicant's information.")
st.set_page_config(
    page_title="🏦 Loan Approval Prediction",
    page_icon="🏦",
    layout="wide"
)
from PIL import Image

from PIL import Image

image = Image.open("loan.jpg")
st.image(image, width=700)
st.markdown("---")
st.markdown("Developed by **Muhammad Sohail** 🚀")
Eduction=st.selectbox("eduction",["Graduate","Not Graduate"])

Self_Employee=st.selectbox("self_employe",["YES","NO"])

income_annum=st.number_input("Income Annum (PKR)",
                             min_value=0,
                             max_value=10000000,
                             value=500000)
loan_amount = st.number_input(
    "Loan Amount",
    min_value=1000000,
    max_value=10000000,
    value=1000000
)
resedintial_assests_value=st.slider("resedintial_assests_value",
                                    min_value=100000,
                                    max_value=10000000,
                                    value=500000)
commercial_value_assests=st.slider("commercial_value_assests",
                                   min_value=100000,
                                   max_value=5000000,
                                   value=100000)
bank_assest_value=st.slider("bank_assests_value",
                            min_value=500000,
                            max_value=5000000,
                            value=500000)
cibil_score = st.slider(
    "CIBIL Score",
    min_value=300,
    max_value=900,
    value=750
)
no_of_dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    max_value=10,
    value=0,
    step=1
)

loan_term = st.number_input(
    "Loan Term (Months)",
    min_value=1,
    max_value=600,
    value=360,
    step=1
)

luxury_Assests_value=st.slider("luxury_Assests_value",
                            min_value=500000,
                            max_value=5000000,
                            value=500000)
Eduction=1 if Eduction=="Graduate" else 0
self_employee = 1 if Self_Employee == "YES" else 0
st.sidebar.title("📋 About")

st.sidebar.info("""
**Loan Approval Prediction**

This application uses a Machine Learning model to predict loan approval based on applicant details.
""")

input_data = pd.DataFrame({
    "No_Of_Dependents": [no_of_dependents],
    "Education": [Eduction],
    "Self_Employed": [self_employee],
    "Income_Annum": [income_annum],
    "Loan_Amount": [loan_amount],
    "Loan_Term": [loan_term],
    "Cibil_Score": [cibil_score],
    "Residential_Assets_Value": [resedintial_assests_value],
    "Commercial_Assets_Value": [commercial_value_assests],
    "Luxury_Assets_Value": [luxury_Assests_value],
    "Bank_Asset_Value": [bank_assest_value]
})


if st.button("🔍 Predict Loan Status"):

    input_scaled = sclar.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("🎉 Congratulations! Your loan is likely to be Approved.")
        st.balloons()
    else:
        st.error("❌ Sorry! Your loan is likely to be Rejected.")
