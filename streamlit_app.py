import streamlit as st
import time

# Function to simulate recommendation logic with more complex criteria
def recommend_product(age, risk, horizon, amount, currency, product_type):
    # Complex criteria for recommendation logic
    if currency == "USD":
        if amount >= 150:
            if risk == "High" and horizon == "Long-term":
                return "FX Growth Portfolio", "A high-risk, long-term USD-denominated portfolio focused on equities."
            elif risk == "Medium" and horizon in ["Medium-term", "Long-term"]:
                return "FX Bond Portfolio", "A medium-risk, medium to long-term USD-denominated portfolio focused on bonds."
            else:
                return "FX Income Accumulator Portfolio", "A low-risk USD-denominated portfolio focused on fixed income securities."
        else:
            return "Alternative Suggestion: Consider individual stocks or smaller investments such as Money Market Fund", "Your initial investment is lower than required for this portfolio."
    
    elif currency == "JMD":
        if amount >= 15000:
            if risk == "Low" and horizon in ["Short-term", "Medium-term"]:
                return "Money Market Fund", "A low-risk, short to medium-term JMD-denominated fund with a mix of securities."
            elif risk == "High" and horizon == "Long-term":
                return "Unit Trust Real Estate Portfolio", "A high-risk, long-term JMD-denominated portfolio focused on real estate."
            else:
                return "Capital Growth Fund", "A high-risk, long-term JMD-denominated fund with a mix of equities and fixed income."
        else:
            return "Alternative Suggestion: Consider individual stocks or lower threshold funds like Money Market Fund", "Your investment amount does not meet the minimum for the selected funds."
    
    return "No valid recommendation found", "Please adjust your inputs and try again."

# Streamlit app layout
st.title("Investment Product Recommendation")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
risk = st.selectbox("Risk Preference", ["Low", "Medium", "High"])
horizon = st.selectbox("Investment Horizon", ["Short-term", "Medium-term", "Long-term"])
amount = st.number_input("Investment Amount (in selected currency)", min_value=1000)
currency = st.selectbox("Investment Currency", ["JMD", "USD"])
product_type = st.selectbox("Preferred Product Type", ["Pooled Fund", "Equity", "Bond", "Real Estate"])

# Submit button for committing inputs
if st.button("Submit"):
    with st.spinner('Processing...'):
        time.sleep(3)  # Simulate model processing time
    
    # Get product recommendation
    product, explanation = recommend_product(age, risk, horizon, amount, currency, product_type)

    # Display the recommendation as an overlay
    st.write(f"""
    <style>
        .overlay {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 0, 0, 0.7);
            z-index: 9999;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .overlay-content {{
            background-color: black;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            max-width: 80%;
        }}
        .overlay h2 {{
            margin-bottom: 20px;
            font-size: 2rem;
        }}
        .overlay p {{
            font-size: 1.2rem;
        }}
    </style>
    <div class="overlay">
        <div class="overlay-content">
            <h2>Recommended Product</h2>
            <p><strong>{product}</strong></p>
            <p>{explanation}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
