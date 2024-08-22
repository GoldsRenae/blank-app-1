import streamlit as st
import time

# Product details based on the provided product descriptors
products = {
    'FX Income Accumulator Portfolio': {
        'risk': 'low', 
        'min_investment': 150, 
        'currency': 'USD',
        'description': 'A pooled fund that enables investors to earn in USD with low risk.'
    },
    'Money Market Fund': {
        'risk': 'low', 
        'min_investment': 15000, 
        'currency': 'JMD',
        'description': 'A low-risk fund with investments in high-quality securities, tax-free under certain conditions.'
    },
    'Capital Growth Fund': {
        'risk': 'high', 
        'min_investment': 15000, 
        'currency': 'JMD',
        'description': 'A high-risk fund focused on capital growth with a mix of equities and fixed income investments.'
    },
    'Unit Trusts Income Portfolio': {
        'risk': 'low', 
        'min_investment': 100000, 
        'currency': 'JMD',
        'description': 'A fund that provides flexible monthly income and a guaranteed principal sum.'
    },
    'Unit Trust Real Estate Portfolio': {
        'risk': 'high', 
        'min_investment': 100, 
        'currency': 'JMD',
        'description': 'A fund focused on real estate investments, suitable for long-term investors.'
    },
    'FX Bond Portfolio': {
        'risk': 'medium', 
        'min_investment': 150, 
        'currency': 'USD',
        'description': 'A medium-risk USD-denominated bond portfolio.'
    },
    'FX Growth Portfolio': {
        'risk': 'high', 
        'min_investment': 150, 
        'currency': 'USD',
        'description': 'A high-risk USD-denominated equity portfolio with global investment opportunities.'
    },
    'Equity Trading Account': {
        'risk': 'high', 
        'min_investment': 15000, 
        'currency': 'USD',
        'description': 'An account for trading individual stocks, suitable for high-risk investors.'
    }
}

# Administrator panel for updating market sentiment
if 'market_sentiment' not in st.session_state:
    st.session_state['market_sentiment'] = 'neutral'

st.sidebar.header('Administrator Panel')
admin_input = st.sidebar.radio(
    'Select the current market sentiment:',
    options=['Positive (Bullish)', 'Negative (Bearish)', 'Neutral'],
)

if st.sidebar.button('Update Sentiment'):
    st.session_state['market_sentiment'] = admin_input.split(' ')[0].lower()
    st.sidebar.success(f"Market sentiment updated to {st.session_state['market_sentiment'].capitalize()}")

# User input section
st.header('Investment Product Recommendation')
st.subheader('Please provide your details')

age = st.number_input('Age', min_value=18, max_value=100, value=30)
investment_amount = st.number_input('Investment Amount', min_value=100, max_value=1000000, value=10000)
risk_preference = st.selectbox('Risk Preference', ['Low', 'Medium', 'High'])
currency_preference = st.selectbox('Preferred Currency', ['JMD', 'USD'])
market_sentiment_input = st.selectbox('What is your current outlook on the market?', ['Positive', 'Negative', 'Neutral'])

if st.button('Get Recommendation'):
    # Simulate processing time
    with st.spinner('Processing your inputs...'):
        time.sleep(3)

    # Overlay for results
    st.markdown(
        """
        <style>
        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.8);
            z-index: 9999;
        }
        .overlay-text {
            color: white;
            font-size: 24px;
            text-align: center;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
        </style>
        <div class="overlay">
            <div class="overlay-text">
                Calculating your recommendation...
            </div>
        </div>
        """, unsafe_allow_html=True
    )
    time.sleep(2)  # Additional delay to simulate model processing

    # Recommendation logic based on user inputs, currency preference, and sentiment
    suitable_products = []
    for product, details in products.items():
        if (details['risk'] == risk_preference.lower() and
            investment_amount >= details['min_investment'] and
            details['currency'] == currency_preference):
            suitable_products.append((product, details))

    if market_sentiment_input.lower() != st.session_state['market_sentiment']:
        st.warning(f"Your market outlook ({market_sentiment_input}) differs from the current market sentiment ({st.session_state['market_sentiment']}).")

    # Display results
    st.markdown(
        """
        <style>
        .overlay {
            display: none;
        }
        </style>
        """, unsafe_allow_html=True
    )
    if suitable_products:
        st.success('Based on your inputs, we recommend the following products:')
        for product, details in suitable_products:
            st.markdown(f"**{product}** - {details['description']} (Minimum Investment: {details['min_investment']}, Currency: {details['currency']}, Risk: {details['risk'].capitalize()})")
    else:
        st.error("Unfortunately, no products match your criteria. Consider adjusting your investment amount, currency, or risk preference.")
