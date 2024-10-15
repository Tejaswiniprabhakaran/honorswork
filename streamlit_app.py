import streamlit as st
import requests

# Apply custom CSS for a more professional look with muted colors
st.markdown(
    """
    <style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(135deg, #a8c0ff, #3f4c6b);
        color: white;
    }

    /* Set font styles */
    body, p, div, input, select, button {
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        font-weight: bold;
    }

    /* Title styling */
    .title {
        color: #ffffff;
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        background-color: rgba(0, 0, 0, 0.5);
        padding: 15px;
        border-radius: 10px;
    }

    /* Input box styling */
    .stNumberInput input, .stSelectbox select {
        background-color: #ffffff;
        color: #333333;
        border: 2px solid #4a90e2;
        border-radius: 5px;
        font-size: 18px;
        padding: 8px;
        margin-bottom: 20px;
    }

    /* Button styling */
    .stButton>button {
        background-color: #007bb5;
        color: white;
        padding: 10px 20px;
        font-size: 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 15px;
    }

    /* Button hover effect */
    .stButton>button:hover {
        background-color: #005b8a;
    }

    /* Result box styling */
    .result-box {
        margin-top: 20px;
        font-size: 28px;
        text-align: center;
        background-color: #2c3e50;
        color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app title
st.markdown("<div class='title'>CalcMaster</div>", unsafe_allow_html=True)

# Input fields for numbers and operation
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Button to trigger the calculation
if st.button("Calculate"):
    # Send data to Flask API
    response = requests.post(
        "http://127.0.0.1:5001/calculate",  # Make sure Flask app is running on this port
        json={"num1": num1, "num2": num2, "operation": operation}
    )
    
    if response.status_code == 200:
        # Parse result from Flask API
        result = response.json().get("result")
        st.markdown(f"<div class='result-box'>Result: {result}</div>", unsafe_allow_html=True)
    else:
        st.error("An error occurred. Please check your input.")
