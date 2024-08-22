import streamlit as st
import pandas as pd
import numpy as np
# Global variable to hold the market sentiment
if 'market_sentiment' not in st.session_state:
    st.session_state['market_sentiment'] = 'neutral'

# Administrator panel to update market sentiment
st.sidebar.header('Administrator Panel')
st.sidebar.subheader('Update Market Sentiment')
admin_input = st.sidebar.radio(
    'Select the current market sentiment:',
    options=['Positive (Bullish)', 'Negative (Bearish)', 'Neutral'],
)

# Update the market sentiment globally
if st.sidebar.button('Update Sentiment'):
    st.session_state['market_sentiment'] = admin_input.split(' ')[0].lower()
    st.sidebar.success(f"Market sentiment updated to {st.session_state['market_sentiment'].capitalize()}")
# User input section
st.header('Investment Product Recommendation')
st.subheader('Please provide your details')

# Example user input fields
age = st.number_input('Age', min_value=18, max_value=100, step=1)
investment_amount = st.number_input('Investment Amount ($)', min_value=1000, step=500)

# User sentiment input
user_sentiment = st.selectbox(
    'What is your current outlook on the market?',
    options=['Positive (Bullish)', 'Negative (Bearish)', 'Neutral']
)

# Combine user sentiment with market sentiment
combined_sentiment = user_sentiment.lower() + '_' + st.session_state['market_sentiment']

# Example button to simulate the recommendation process
if st.button('Get Recommendation'):
    st.write("Processing your inputs...")

    # Simulate a short processing time
    with st.spinner('Analyzing your profile...'):
        import time
        time.sleep(3)

    # Example of how sentiment might affect the recommendation
    recommendation = "Conservative Portfolio" if combined_sentiment == "negative_bearish" else "Aggressive Portfolio"
    explanation = f"Based on your outlook ({user_sentiment}) and the current market sentiment ({st.session_state['market_sentiment']}), we recommend a {recommendation}."

    # Display the recommendation in an overlay style
    st.markdown(
        f"""
        <style>
        .overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(30, 61, 88, 0.85);
            color: white;
            z-index: 1000;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .blur {{
            filter: blur(5px);
        }}
        </style>
        <div class="overlay">
            <div style="background-color:#1e3d58;padding:20px;border-radius:10px;">
                <h3>Recommended Product</h3>
                <p>We recommend: <strong>{recommendation}</strong></p>
                <p><em>{explanation}</em></p>
            </div>
        </div>
        <script>
        document.querySelector('.overlay').addEventListener('click', function() {{
            this.style.display = 'none';
            document.querySelector('.blur').classList.remove('blur');
        }});
        </script>
        """,
        unsafe_allow_html=True
    )
