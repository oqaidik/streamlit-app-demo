
import streamlit as st

# Initialisation de l'état
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Fonction pour changer de page
def go_to_sheets():
    st.session_state.page = 'sheets'

# Navigation
if st.session_state.page == 'home':
    st.title("Bienvenue dans mon app !")
    st.write("Cliquez sur le bouton pour lire les données depuis Google Sheets.")
    if st.button("Voir Google Sheets"):
        go_to_sheets()

elif st.session_state.page == 'sheets':
    # On appelle ici le contenu de la deuxième page
    from sheets_app import show_sheets_page
    show_sheets_page()
    if st.button("🔙 Retour"):
        st.session_state.page = 'home'
