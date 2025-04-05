import streamlit as st
import pandas as pd



import streamlit as st
import pandas as pd

def show_sheets_page():
    st.title("Lecture de Google Sheets dans Streamlit")

    # Remplace cet ID par celui de ta feuille Google Sheets
    sheet_id = "14GC4RUwAcezwnWs2gjDtPMpSoxzFHH9Us3fts9-cdFU"
    sheet_name = "str1"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    try:
        df = pd.read_csv(url)
        st.success("Données chargées avec succès depuis Google Sheets !")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
