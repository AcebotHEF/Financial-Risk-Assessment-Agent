import streamlit as st
from risk_agent import analyze_risk

st.title("📉 Financial Risk Assessment Agent")

if st.button("Run Risk Analysis"):
    df, result = analyze_risk()

    st.subheader("📊 Financial Profile")
    st.dataframe(df)

    st.subheader("🔎 AI Risk Assessment")
    st.write(result)