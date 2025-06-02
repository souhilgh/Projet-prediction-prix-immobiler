import streamlit as st
import pandas as pd

def run():
    st.title("📂 Chargement des Données Immobilières Algériennes")
    
    uploaded_file = st.file_uploader("Téléversez votre fichier de données immobilières (CSV)", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            # Nettoyage des données spécifiques à l'Algérie
            df = clean_algerian_data(df)
            
            st.session_state.df = df
            st.success("Données chargées avec succès!")
            
            st.subheader("Aperçu des Données")
            st.write(df.head())
            
            st.subheader("Statistiques Descriptives")
            st.write(df.describe())
            
            st.subheader("Valeurs Manquantes")
            st.write(df.isnull().sum())
            
        except Exception as e:
            st.error(f"Erreur lors du chargement des données: {e}")
    else:
        st.info("Veuillez téléverser un fichier CSV contenant des données immobilières algériennes.")

def clean_algerian_data(df):
    """Fonction pour nettoyer les données spécifiques à l'Algérie"""
    # Conversion des prix en DZD si nécessaire
    if 'Prix' in df.columns:
        df['Prix'] = df['Prix'].astype(float)
    
    # Nettoyage des villes algériennes
    if 'Ville' in df.columns:
        df['Ville'] = df['Ville'].str.title().str.strip()
    
    return df