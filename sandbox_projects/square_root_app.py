"""
A simple Streamlit web app for calculating the square root of a number.
The app features a modern UI, input validation, and displays the result in real time.
"""

import streamlit as st  # Import Streamlit for building the web app
import math             # Import math for square root calculation

def square_root(number):
    """Return the square root of a given number."""
    return math.sqrt(number)

# Set up the page configuration (title, icon, layout)
st.set_page_config(
    page_title="Square Root Calculator",
    page_icon="🔢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS styles for a modern look
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d3748 100%);
    }
    .main-header {
        text-align: center;
        color: #ffffff;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 20px rgba(99, 102, 241, 0.5);
    }
    .sub-header {
        text-align: center;
        color: #a0aec0;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .result-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    .result-text {
        color: #ffffff;
        font-size: 2rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .result-value {
        color: #63f;
        font-size: 3rem;
        font-weight: 700;
        text-shadow: 0 0 15px rgba(99, 102, 241, 0.8);
    }
    .input-label {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .stNumberInput > div > div > input {
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(99, 102, 241, 0.3);
        border-radius: 10px;
        color: #ffffff;
        font-size: 1.2rem;
        padding: 0.75rem;
        transition: all 0.3s ease;
    }
    .stNumberInput > div > div > input:focus {
        border-color: #63f;
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.5);
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Main header and sub-header
st.markdown('<h1 class="main-header">√ Square Root Calculator</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Enter a number to calculate its square root</p>', unsafe_allow_html=True)

# Create three columns for centering the input box
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Label for the input field
    st.markdown('<p class="input-label">Enter a number:</p>', unsafe_allow_html=True)
    # Number input widget (only allows non-negative numbers)
    number = st.number_input(
        label="",
        min_value=0.0,
        value=100.0,
        step=1.0,
        format="%.2f",
        key="number_input"
    )
    # Calculate the square root
    result = square_root(number)
    # Display the result in a styled container
    st.markdown(f"""
    <div class="result-container">
        <div class="result-text">Square root of {number}</div>
        <div class="result-value">{result:.6f}</div>
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
# python -m streamlit run square_root_app.py