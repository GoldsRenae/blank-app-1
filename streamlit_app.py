import streamlit as st

# Function to simulate recommendation logic
def recommend_product(age, risk, horizon, amount, currency, product_type):
    if currency == "USD":
        if risk == "High":
            if horizon == "Long-term":
                return "FX Growth Portfolio", "A high-risk, long-term USD-denominated portfolio focused on equities."
            else:
                return "FX Bond Portfolio", "A medium-risk, medium to long-term USD-denominated portfolio focused on bonds."
        elif risk == "Low":
            return "FX Income Accumulator Portfolio", "A low-risk USD-denominated portfolio focused on fixed income securities."
    elif currency == "JMD":
        if risk == "Low" and horizon != "Long-term":
            return "Money Market Fund", "A low-risk, short to medium-term JMD-denominated fund with a mix of securities."
        elif risk == "High":
            return "Unit Trust Real Estate Portfolio", "A high-risk, long-term JMD-denominated portfolio focused on real estate."
    return "Capital Growth Fund", "A high-risk, long-term JMD-denominated fund with a mix of equities and fixed income."

# Streamlit app layout
st.title("Investment Product Recommendation")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
risk = st.selectbox("Risk Preference", ["Low", "Medium", "High"])
horizon = st.selectbox("Investment Horizon", ["Short-term", "Medium-term", "Long-term"])
amount = st.number_input("Investment Amount (in selected currency)", min_value=1000)
currency = st.selectbox("Investment Currency", ["JMD", "USD"])
product_type = st.selectbox("Preferred Product Type", ["Pooled Fund", "Equity", "Bond", "Real Estate"])

# Get product recommendation
product, explanation = recommend_product(age, risk, horizon, amount, currency, product_type)

# Display the recommendation
st.header("Recommended Product")
st.write(f"We recommend: **{product}**")
st.subheader("Why this product?")
st.write(explanation)

# Mimic model processing time
import time
with st.spinner('Processing...'):
    time.sleep(2)  # Simulates model processing time
st.success('Recommendation ready!')

