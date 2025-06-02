import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def run():
    st.title("🔍 Exploration des Données Immobilières Algériennes")
    
    if "df" not in st.session_state:
        st.warning("Veuillez d'abord charger les données depuis la page 'Chargement des Données'")
        return
    
    df = st.session_state.df
    
    st.header("Visualisation des Données")
    
    # Histogramme des prix
    fig = px.histogram(df, x="Prix", nbins=50, title="Distribution des Prix Immobiliers (DZD)")
    st.plotly_chart(fig)
    
    # Prix par ville
    if 'Ville' in df.columns:
        fig = px.box(df, x="Ville", y="Prix", title="Prix par Ville")
        st.plotly_chart(fig)
    
    # Prix par type de bien
    if 'Type' in df.columns:
        fig = px.pie(df, names="Type", title="Répartition par Type de Bien")
        st.plotly_chart(fig)
    
    # Corrélation surface/prix
    if 'Surface' in df.columns and 'Prix' in df.columns:
        fig = px.scatter(df, x="Surface", y="Prix", color="Ville", 
                        title="Relation Surface/Prix")
        st.plotly_chart(fig)
    
    # Carte des prix (si données géographiques disponibles)
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", 
                              color="Prix", size="Surface",
                              mapbox_style="open-street-map",
                              title="Répartition Géographique des Prix")
        st.plotly_chart(fig)