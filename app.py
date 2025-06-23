import streamlit as st
import pickle
import pandas as pd

# Load the model
with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📉", layout="centered")

with st.sidebar:
    st.title("About this App 🌐")
    st.markdown("""
    This application predicts if a customer will leave the service (churn) or stay.
    - **Model**: Logistic Regression
    - **Data**: Telecom customer dataset
    """)
    st.markdown("Built with ❤️ in Streamlit")

st.title("📉 Customer Churn Prediction")
st.markdown("#### Fill in the details below to see the prediction")

# Use columns for a more advanced UI
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender", ["Male", "Female"],
        help="Customer's gender"
    )
    partner = st.selectbox(
        "Partner", ["Yes", "No"],
        help="Does the customer have a partner?"
    )
    tenure = st.slider(
        "Tenure (months)", 0, 72, 12,
        help="Months as a customer"
    )
    contract = st.selectbox(
        "Contract", ["Month-to-month", "One year", "Two year"],
        help="Contract duration"
    )

with col2:
    senior_citizen = st.selectbox(
        "Senior Citizen", [0, 1],
        help="0 = under 65, 1 = 65 or older"
    )
    dependents = st.selectbox(
        "Dependents", ["Yes", "No"],
        help="Has dependents (children, etc.)"
    )
    monthly_charges = st.number_input(
        "Monthly Charges", 0.0, 500.0, 70.0,
        help="Average monthly bill in INR"
    )
    total_charges = st.number_input(
        "Total Charges", 0.0, 10000.0, 3000.0,
        help="Total billed amount in INR"
    )
    payment_method = st.selectbox(
        "Payment Method", [
            "Electronic check", "Mailed check",
            "Bank transfer (automatic)", "Credit card (automatic)"
        ],
        help="How the customer pays"
    )

# Prepare input for prediction
input_df = pd.DataFrame([{
    'gender': gender,
    'Partner': partner,
    'Dependents': dependents,
    'tenure': tenure,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'Contract': contract,
    'PaymentMethod': payment_method
}])

if st.button("Predict Churn 🚀"):
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]
    prob_pct = int(round(prob * 100))

    if pred == 1:
        st.error(f"⚠️ Likely to churn (Probability: {prob_pct}%)")
    else:
        st.success(f"✅ Likely to stay (Probability: {prob_pct}%)")

    with st.expander("What do these results mean?"):
        st.markdown("""
        - **Churn**: The customer is likely to leave the service soon.
        - **Stay**: The customer is likely to continue using the service.
        - **Probability**: The chance (0-100%) that the customer will churn.
        """)

# Footer
st.markdown(
    """
    <hr style="margin-top: 40px; margin-bottom: 10px;">
    <div style="text-align: center; color: gray;">
        &copy; 2025 Customer Churn Predictor
    </div>
    """,
    unsafe_allow_html=True
)


