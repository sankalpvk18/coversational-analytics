import streamlit as st

DB_NAME = "Superstore.db"
DB_PATH = "sqlite:///Superstore.db"
META_DATA_PATH = "superstore_meta_deta.csv"
API_KEY = st.secrets["API_KEY"]
FIREBASE_CERT_CONFIG = {
    "type": st.secrets["firebase"]["type"],
    "project_id": st.secrets["firebase"]["project_id"],
    "private_key_id": st.secrets["firebase"]["private_key_id"],
    "private_key": st.secrets["firebase"]["private_key"].replace("\\n", "\n"),
    "client_email": st.secrets["firebase"]["client_email"],
    "client_id": st.secrets["firebase"]["client_id"],
    "auth_uri": st.secrets["firebase"]["auth_uri"],
    "token_uri": st.secrets["firebase"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["firebase"][
        "auth_provider_x509_cert_url"
    ],
    "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"],
}
