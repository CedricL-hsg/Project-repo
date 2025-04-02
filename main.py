from data.data_fetcher import get_price_data
from data.indicators import calculate_max_drawdown
import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Dein persönlicher Anlageassistent")

startkapital = st.text_input("Startkapital in CHF", "10000")

einkommen = st.slider("Monatliches Einkommen (CHF)", 
                      0,
                      20000,
                      5000,
                      step=500
                      )

risikoprofil = st.selectbox("Risikoprofil", ["konservativ", "ausgewogen", "wachstum"])


st.subheader("Deine Angaben:")
st.write(f"💰 Startkapital: CHF {startkapital}")
st.write(f"📥 Monatliches Einkommen: CHF {einkommen}")
st.write(f"⚖️ Risikoprofil: {risikoprofil}")

# Auswahl je nach Risikoprofil
if risikoprofil == "konservativ":
    ticker = "BND"  # Anleihen-ETF
elif risikoprofil == "ausgewogen":
    ticker = "SPY"  # S&P 500
else:
    ticker = "QQQ"  # Tech-ETF

# Hole historische Daten
data = get_price_data(ticker)

# Zeichne den Chart
st.subheader("📈 Historische Performance")
fig, ax = plt.subplots()
ax.plot(data.index, data['Close'], label=ticker)
ax.set_title(f"Entwicklung von {ticker}")
ax.set_xlabel("Datum")
ax.set_ylabel("Preis in $")
ax.legend()
st.pyplot(fig)


# Berechne Drawdown
max_dd = calculate_max_drawdown(data['Close'])

# Zeige Drawdown an
st.markdown(f"📉 **Maximaler Drawdown (letzte 5 Jahre):** {max_dd:.2%}")

