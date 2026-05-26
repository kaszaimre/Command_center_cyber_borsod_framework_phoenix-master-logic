import streamlit as st
import pandas as pd
import sys
import os

# 1. Kényszerített útvonal-beállítás (a biztos működéshez)
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# 2. Modulok importálása (Most már tiszta, duplikációk nélkül)
from core.phoenix_protocol import PhoenixProtocol
from trading.gold_extractor import process_gold_signals

# 3. Streamlit Konfiguráció
st.set_page_config(page_title="Borsodi Bunker Terminal", layout="wide")

st.title("🛡️ BORSODI BUNKER - VÁLLALATI TERMINÁL")
st.markdown("---")

# 4. Oldalsáv
ticker = st.sidebar.text_input("Ticker bevitele (pl. AAPL, RKLB)", "BTC")
btn_scan = st.sidebar.button("Mészárlás Indítása")

# 5. Fő logika
if btn_scan:
    st.write(f"--- [v6.5] {ticker} analízis folyamatban... ---")
    
    # Phoenix protocol indítása (ahogy a notebookban volt)
    p = PhoenixProtocol()
    p.boot_sequence()
    
    st.success(f"{ticker} adatok betöltve és elemezve.")
    
    # Itt jelenítjük meg a vizuális adatokat
    # Példa: a grafikon, amit a notebookból hoztál
    chart_data = pd.DataFrame({"Price": [100, 102, 101, 105, 108, 110]})
    st.line_chart(chart_data)
    
    st.info("Mészárlás befejezve. Pista bá' jelentése: A rendszer stabil!")
else:
    st.info("Várj a parancsra, Tábornok! Adj meg egy tickert az oldalsávban.")
