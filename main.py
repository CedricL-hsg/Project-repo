import streamlit as st
import matplotlib.pyplot as plt
from data.data_fetcher import get_price_data
from data.indicators import calculate_max_drawdown
# Optional: from data.finnhub_api import get_pe_ratio

st.set_page_config(page_title="Anlageassistent", layout="centered")

# Titelbereich
st.title("💼 Intelligenter Anlageassistent")
st.markdown("Willkommen! Gib deine Präferenzen an und erhalte individuelle Investment-Insights.")

# Eingabe in Spalten aufteilen
with st.expander("🧮 Persönliche Angaben"):
    col1, col2 = st.columns(2)

    with col1:
        startkapital = st.number_input("💰 Startkapital in CHF", min_value=0, value=10000, step=1000)
        einkommen = st.slider("📥 Monatliches Einkommen (CHF)", 0, 20000, 5000, step=500)

    with col2:
        risikoprofil = st.selectbox("⚖️ Risikoprofil", ["konservativ", "ausgewogen", "wachstum"])
        # Optional: Erfahrung & Horizont
        erfahrung = st.radio("📚 Erfahrung", ["Anfänger", "Fortgeschritten", "Experte"])
        horizont = st.slider("📆 Anlagehorizont (Jahre)", 1, 30, 10)

# Ausgabe der Eingaben
st.markdown("---")
st.subheader("📝 Deine Angaben")
st.write(f"**Startkapital:** CHF {startkapital:,}")
st.write(f"**Monatliches Einkommen:** CHF {einkommen:,}")
st.write(f"**Risikoprofil:** {risikoprofil.capitalize()}")
st.write(f"**Erfahrung:** {erfahrung}")
st.write(f"**Horizont:** {horizont} Jahre")

# Auswahl ETF je nach Risikoprofil
if risikoprofil == "konservativ":
    ticker = "BND"
    beschreibung = "Fokus auf Sicherheit durch Anleihen (ETF: BND)"
elif risikoprofil == "ausgewogen":
    ticker = "SPY"
    beschreibung = "Ausgewogene Mischung durch S&P 500 (ETF: SPY)"
else:
    ticker = "QQQ"
    beschreibung = "Wachstumsorientiert durch Tech-Fokus (ETF: QQQ)"

# Daten & Visualisierung
st.markdown("---")
st.subheader("📈 Performance & Risikoanalyse")
st.markdown(f"**Ausgewählter ETF:** `{ticker}` – {beschreibung}")

# Kursdaten
data = get_price_data(ticker)
fig, ax = plt.subplots()
ax.plot(data.index, data['Close'], label=f"{ticker}")
ax.set_title(f"Entwicklung von {ticker}")
ax.set_xlabel("Datum")
ax.set_ylabel("Preis in $")
ax.legend()
st.pyplot(fig)

# Drawdown berechnen
max_dd = calculate_max_drawdown(data['Close'])
st.markdown(f"📉 **Maximaler Drawdown (5 Jahre):** {max_dd:.2%}")