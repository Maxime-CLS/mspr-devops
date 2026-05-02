import streamlit as st
from src.auth.auth_manager import authenticate, add_user, get_user_by_username

def show_login_page():
    """Affiche la page de login/inscription."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "username" not in st.session_state:
        st.session_state.username = None

    if not st.session_state.authenticated:
        tab1, tab2 = st.tabs(["Connexion", "Inscription"])

        with tab1:
            st.header("Connexion")
            username = st.text_input("Nom d'utilisateur", key="login_username")
            password = st.text_input("Mot de passe", type="password", key="login_password")
            if st.button("Se connecter"):
                if authenticate(username, password):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Nom d'utilisateur ou mot de passe incorrect")

        with tab2:
            st.header("Inscription")
            new_username = st.text_input("Nouveau nom d'utilisateur", key="signup_username")
            new_name = st.text_input("Nom complet", key="signup_name")
            new_email = st.text_input("Email", key="signup_email")
            new_password = st.text_input("Nouveau mot de passe", type="password", key="signup_password")
            if st.button("S'inscrire"):
                if get_user_by_username(new_username):
                    st.error("Ce nom d'utilisateur est déjà pris")
                else:
                    if add_user(new_username, new_name, new_password, new_email):
                        st.success("Compte créé avec succès ! Vous pouvez maintenant vous connecter.")
                    else:
                        st.error("Erreur lors de la création du compte")
    else:
        st.success(f"Connecté en tant que {st.session_state.username}")
        if st.button("Se déconnecter"):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.rerun()