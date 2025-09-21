import streamlit as st


st.set_page_config(
                    page_title="dashboard",
                   layout="wide",
                   initial_sidebar_state="collapsed",
                   page_icon="C:/Users/macdounout/Desktop/dash_streamlilt/logo.png",
                
                   )


# Se não estiver logado → volta para login
if "login" not in st.session_state or not st.session_state.login:
    st.warning("⚠️ Você precisa fazer login primeiro.")
    st.switch_page("login.py")
    
    

st.markdown(""" 
    <style>
        .block-container {
            padding-top: 4rem;
            padding-right: 0rem;
            padding-left: 0rem;
            max-width: 100%;
        }
        
        html, body {
            height: 100%;
            width: 100%;
            margin: 0;
            padding: 0;
        }
        
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(30deg, #141E30, #243B55, #141E30);
            background-size: 100% 300%;
            animation: gradient 8s ease-in-out infinite;
            color: white;
        }

        @keyframes gradient {
            0% { background-position: 50% 0%; }
            50% { background-position: 50% 100%; }
            100% { background-position: 50% 0%; }
        }
        
        [data-testid="stHeader"] {
            background: transparent;   
            }
            
        
            
        [data-testid="stSidebar"] {
                background: linear-gradient(30deg, #141E30, #243B55, #141E30);
                color: white;}
        
    </style>
           
""", unsafe_allow_html=True)
   
    
st.title("📊 Dashboard")



