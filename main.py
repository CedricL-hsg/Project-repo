import streamlit as st

st.title("📊 Dein persönlicher Anlageassistent")

startkapital = st.text_input("Startkapital in CHF", "10000")

einkommen = st.slider("Monatliches Einkommen (CHF)", 
                      0,
                      15000,
                      5000,
                      step=500
                      )

risikoprofil = st.selectbox("Risikoprofil", ["konservativ", "ausgewogen", "dynamisch"])