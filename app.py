import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Projet Immobilier Algérien",
    page_icon="🏠",
    layout="wide"
)

# Titre principal
st.markdown("<h1 style='text-align: center; color: #2E86AB;'>🏠 Estimation des Prix Immobiliers en Algérie</h1>", unsafe_allow_html=True)

# Navigation latérale
menu = st.sidebar.radio("Navigation", [
    "Accueil",
    "Chargement des Données",
    "Exploration des Données", 
    "Entraînement du Modèle",
    "Prédiction de Prix"
])

# Affichage du contenu selon la page choisie
if menu == "Accueil":
    st.markdown("""
    ### 🔍 Objectif du Projet :
    > Prédire le prix d'un bien immobilier en Algérie à partir de ses caractéristiques
    
    ### 🧩 Étapes de l'Application :
    1. **Chargement des données** 📂 - Importez votre fichier de données
    2. **Exploration des données** 🔍 - Visualisez et analysez les données
    3. **Entraînement du modèle** 🧠 - Entraînez un modèle de prédiction
    4. **Prédiction de prix** 💰 - Estimez le prix d'un bien immobilier
    
    ### 📌 Données Algériennes :
    - Villes principales : Alger, Oran, Constantine, Annaba, etc.
    - Types de biens : Appartement, Villa, Maison, Fermat
    - Caractéristiques : Surface, Nombre de pièces, État du bien, etc.
    """)

elif menu == "Chargement des Données":
    from Chargement import run
    run()

elif menu == "Exploration des Données":
    from Exploration_des_données import run
    run()

elif menu == "Entraînement du Modèle":
    from Entraînement import run
    run()

elif menu == "Prédiction de Prix":
    from Prédiction import run
    run()