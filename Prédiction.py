import streamlit as st
import numpy as np
import joblib

def run():
    st.title("💰 Estimation de Prix Immobilier en Algérie")
    
    if "model" not in st.session_state:
        st.warning("Veuillez d'abord entraîner le modèle depuis la page 'Entraînement du Modèle'")
        return
    
    model = st.session_state.model
    scaler = st.session_state.scaler
    
    st.header("Saisie des Caractéristiques du Bien")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ville = st.selectbox("Ville", options=["Alger", "Oran", "Constantine", "Annaba", "Autre"])
        type_bien = st.selectbox("Type de bien", options=["Appartement", "Villa", "Maison", "Fermat"])
        etat_bien = st.selectbox("État du bien", options=["Neuf", "Bon état", "À rénover", "Vétuste"])
    
    with col2:
        surface = st.number_input("Surface (m²)", min_value=30, max_value=1000, value=80)
        nb_pieces = st.number_input("Nombre de pièces", min_value=1, max_value=20, value=3)
        nb_chambres = st.number_input("Nombre de chambres", min_value=1, max_value=10, value=2)
        nb_salles_bain = st.number_input("Nombre de salles de bain", min_value=1, max_value=5, value=1)
    
    # Encodage des caractéristiques
    villes_algerie = {"Alger": 1, "Oran": 2, "Constantine": 3, "Annaba": 4, "Autre": 10}
    types_bien = {"Appartement": 1, "Villa": 2, "Maison": 3, "Fermat": 4}
    etats_bien = {"Neuf": 1, "Bon état": 2, "À rénover": 3, "Vétuste": 4}
    
    features = np.array([[
        surface,
        nb_pieces,
        nb_chambres,
        nb_salles_bain,
        villes_algerie.get(ville, 10),
        types_bien.get(type_bien, 1),
        etats_bien.get(etat_bien, 2)
    ]])
    
    # Normalisation
    features_scaled = scaler.transform(features)
    
    if st.button("Estimer le Prix"):
        prix_estime = model.predict(features_scaled)[0]
        st.success(f"Prix estimé: {prix_estime:,.0f} DZD")
        
        # Affichage d'une fourchette de prix
        fourchette_basse = prix_estime * 0.9
        fourchette_haute = prix_estime * 1.1
        st.info(f"Fourchette de prix estimée: {fourchette_basse:,.0f} - {fourchette_haute:,.0f} DZD")