import streamlit as st
# Ensure you have a file named 'risk_agent.py' in the same folder
from risk_agent import analyze_risk

# Optional: Set page configuration for a wider layout
st.set_page_config(page_title="Financial Risk Agent", layout="wide")

st.title("📉 Financial Risk Assessment Agent")

# Button to trigger analysis
if st.button("Run Risk Analysis", type="primary"):
    with st.spinner("Analyzing financial data..."):
        try:
            # call the function
            df, result = analyze_risk()

            # Create columns for a cleaner layout
            col1, col2 = st.columns([1, 1])

            with col1:
                st.subheader("📊 Financial Profile")
                st.dataframe(df, use_container_width=True)

            with col2:
                st.subheader("🔎 AI Risk Assessment")
                # Using .info box makes the text stand out more
                st.info(result)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")