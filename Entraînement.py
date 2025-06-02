import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd
import numpy as np
import joblib

def run():
    st.title("🧠 Entraînement du Modèle de Prédiction")
    
    if "df" not in st.session_state:
        st.warning("Veuillez d'abord charger les données depuis la page 'Chargement des Données'")
        return
    
    df = st.session_state.df
    
    st.header("Préparation des Données")
    
    # Encodage des variables catégorielles spécifiques à l'Algérie
    df_encoded = encode_algerian_features(df)
    
    # Sélection des features
    features = ['Surface', 'Nb_Pieces', 'Nb_Chambres', 'Nb_Salles_Bain', 
               'Ville_Encoded', 'Type_Encoded', 'Etat_Encoded']
    features = [f for f in features if f in df_encoded.columns]
    
    X = df_encoded[features]
    y = df_encoded['Prix']
    
    # Normalisation
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split des données
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    st.header("Entraînement du Modèle")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    with st.spinner("Entraînement en cours..."):
        model.fit(X_train, y_train)
    
    # Évaluation
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    
    st.success(f"Modèle entraîné avec succès! Erreur Moyenne Absolue: {mae:,.0f} DZD")
    
    # Sauvegarde
    st.session_state.model = model
    st.session_state.scaler = scaler
    joblib.dump(model, 'modele_immobilier_algerie.pkl')
    joblib.dump(scaler, 'scaler_immobilier_algerie.pkl')

def encode_algerian_features(df):
    """Encodage des caractéristiques spécifiques à l'Algérie"""
    df_encoded = df.copy()
    
    # Villes algériennes principales
    villes_algerie = {
        'Alger': 1, 'Oran': 2, 'Constantine': 3, 
        'Annaba': 4, 'Blida': 5, 'Batna': 6,
        'Sétif': 7, 'Tlemcen': 8, 'Mostaganem': 9
    }
    
    if 'Ville' in df_encoded.columns:
        df_encoded['Ville_Encoded'] = df_encoded['Ville'].map(villes_algerie).fillna(10)  # 10 pour autres villes
    
    # Types de biens
    types_bien = {
        'Appartement': 1, 'Villa': 2, 
        'Maison': 3, 'Fermat': 4
    }
    
    if 'Type' in df_encoded.columns:
        df_encoded['Type_Encoded'] = df_encoded['Type'].map(types_bien).fillna(1)
    
    # État du bien
    etats_bien = {
        'Neuf': 1, 'Bon état': 2,
        'À rénover': 3, 'Vétuste': 4
    }
    
    if 'Etat' in df_encoded.columns:
        df_encoded['Etat_Encoded'] = df_encoded['Etat'].map(etats_bien).fillna(2)
    
    return df_encoded