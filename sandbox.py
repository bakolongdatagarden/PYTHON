"""
A simple Streamlit web app for calculating the square root of a number.
The app features a modern UI, input validation, and displays the result in real time.
"""

import streamlit as st  # Import Streamlit for building the web app

def calculate_tax(earnings):
    if earnings < 12000:
        return earnings * 0.25
    else:
        return earnings * 0.30

# Set up the page configuration (title, icon, layout)
st.set_page_config(
    page_title="Personal Tax Calculator",
    page_icon="🔢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS styles for a brown background, golden orange highlights, and subtle green accents
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #4e342e 0%, #3e2723 100%);
    }
    .main-header {
        text-align: center;
        color: #ffb347;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 20px #ffb34788, 0 0 10px #3e2723;
        letter-spacing: 2px;
    }
    .sub-header {
        text-align: center;
        color: #ffd580;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        text-shadow: 0 0 10px #3e2723;
    }
    .result-container {
        background: linear-gradient(120deg, rgba(255, 183, 71, 0.12), rgba(34, 139, 34, 0.10));
        backdrop-filter: blur(8px);
        border: 2px solid #ffb347;
        border-radius: 18px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 8px 32px rgba(34, 139, 34, 0.18), 0 2px 8px rgba(255, 183, 71, 0.10);
    }
    .result-text {
        color: #ffb347;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 10px #3e2723;
    }
    .result-value {
        color: #ff914d;
        font-size: 3rem;
        font-weight: 700;
        text-shadow: 0 0 15px #ffb347, 0 0 10px #228b22;
    }
    .input-label {
        color: #ffd580;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 5px #3e2723;
    }
    .stNumberInput > div > div > input {
        background: rgba(255, 255, 255, 0.10);
        border: 2px solid #228b22;
        border-radius: 12px;
        color: #ff914d;
        font-size: 1.2rem;
        padding: 0.75rem;
        transition: all 0.3s ease;
        box-shadow: 0 0 8px #ffd58033;
    }
    .stNumberInput > div > div > input:focus {
        border-color: #ffb347;
        box-shadow: 0 0 15px #ffb347, 0 0 10px #228b22;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Main header and sub-header
st.markdown('<h1 class="main-header">Personal Tax Calculator</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Enter your earnings to reveal your magical tax amount</p>', unsafe_allow_html=True)

# Create three columns for centering the input box
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Label for the input field
    st.markdown('<p class="input-label">Enter your earnings:</p>', unsafe_allow_html=True)
    # Number input widget (only allows non-negative numbers)
    earnings = st.number_input(
        label="",
        min_value=0.0,
        value=100.0,
        step=1.0,
        format="%.2f",
        key="earnings_input"
    )
    # Calculate the tax owed
    tax_owed = calculate_tax(earnings)
    # Display the result in a styled container
    st.markdown(f"""
    <div class="result-container">
        <div class="result-text">Tax owed for ${earnings:,.2f}</div>
        <div class="result-value">${tax_owed:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #a0aec0; font-size: 0.9rem;">'
    'Built with Python & Streamlit 🚀<br>'
    'Project by Nyami Bakolong, with assistance from Claude AI and GitHub Copilot.'
    '</p>',
    unsafe_allow_html=True
)

# run code 
# python -m streamlit run sandbox.py