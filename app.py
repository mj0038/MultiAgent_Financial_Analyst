import streamlit as st
from crew.crew_manager import create_crew

st.title("Financial Analyst App")

# User Inputs
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, NVDA):")
model_option = st.selectbox(
    "Select Model:",
    ["OpenAI GPT-4o", "OpenAI GPT-4o Mini", "Llama 3 8B", "Llama 3.1 70B", "Llama 3.1 8B"]
)
analyze_button = st.button("Analyze Stock")

if analyze_button and stock_symbol:
    st.write("Running analysis... Please wait.")
    file_path = create_crew(stock_symbol, model_option)
    with open(file_path, "r") as file:
        st.text(file.read())
