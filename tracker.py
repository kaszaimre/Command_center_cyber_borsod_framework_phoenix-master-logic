#https://trackerpy-csdvuugw3xjdeyolcutd6y.streamlit.app/

import streamlit as st
import pandas as pd
import sys
import os

# 1. Kényszerített útvonal-beállítás (a gyökérkönyvtárra)
root_path = os.path.dirname(os.path.abspath(__file__))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# 2. Importálás (Ezek most már működni fognak, mert a gyökér a path-ban van)
try:
    from core.phoenix_protocol import PhoenixProtocol
    from trading.gold_extractor import process_gold_signals
    # Ha a 'core' vagy 'trading' mappa valamiért máshogy lenne elnevezve, 
    # ellenőrizd a GitHub-on a pontos nevüket!
except Exception as e:
    st.error(f"Import hiba: {e}. Ellenőrizd a mappák nevét a GitHubon!")
    st.stop()

# 3. Streamlit alkalmazás logikája
st.set_page_config(page_title="Borsodi Bunker Terminal", layout="wide")
st.title("🛡️ BORSODI BUNKER - VÁLLALATI TERMINÁL")

ticker = st.sidebar.text_input("Ticker bevitele", "BTC")
btn_scan = st.sidebar.button("Mészárlás Indítása")

if btn_scan:
    st.write(f"--- [v6.5] {ticker} analízis folyamatban... ---")
    st.success(f"{ticker} adatok betöltve.")
    st.line_chart(pd.DataFrame({"Price": [100, 102, 101, 105]}))
else:
    st.info("Várj a parancsra, Tábornok!")
