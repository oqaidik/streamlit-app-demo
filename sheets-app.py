import streamlit as st
import pandas as pd

st.title("Lecture de Google Sheets dans Streamlit")

# Remplace cet ID par celui de ta feuille Google Sheets
sheet_id = "14GC4RUwAcezwnWs2gjDtPMpSoxzFHH9Us3fts9-cdFU"
sheet_name = "str1"

# Créer l'URL de téléchargement en CSV
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

# Lire le contenu avec pandas
df = pd.read_csv(url)

# Afficher le tableau
st.subheader("Contenu du tableau Google Sheets")
st.dataframe(df)