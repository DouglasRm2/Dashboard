import streamlit as st
import time


st.set_page_config(
                    page_title="Bem-vindo",
                   layout="wide",
                   initial_sidebar_state="collapsed",
                   page_icon="C:/Users/macdounout/Desktop/dash_streamlilt/logo.png",
                
                   )

# Credenciais válidas
LOGIN_CORRETO = "admin"
SENHA_CORRETA = "1"
# __________________________

# css para ocupar toda a largura
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
            
        
        div [data-testid="stAlert"] {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 3rem;
        } 
        
        
        div[data-testid="stAlertContainer"] {
            padding: 4px 8px;      
            margin: 5px 0;         
            border-radius: 90px;     
            font-size: 0.9rem;    
            min-height: auto;     
            width: 250px;
            text-align: center;  
            background-color: #141E30; 
            text-color: white;
            
        }

        div[data-testid="stHorizontalBlock"] {
            margin-top: 6rem;
            display: flex;
            justify-content: center;
            align-items: center;    
            
     
        }
        div[data-testid="stVerticalBlock"] {
             
            display: flex;
            justify-content: center;
            align-items: center;   
            
     
        }
        
        
        button[kind="secondary"] {
            background-color: #1F3C68;
            color: white;        
            border: none;       
            border-radius: 8px;
            padding: 8px 16px;     
            font-weight: bold;
            cursor: pointer; 
            transition: 0.3s ease-in-out;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.3)
        }
        
        button[kind="secondary"]:hover {
            background-color: #57A2C7; 
            color: white !important;
        }
                
      
            
            
        [data-testid="stSidebar"] {
                
                background: linear-gradient(30deg, #141E30, #243B55, #141E30);
                color: white;
               
                }

        

          /* input */
          
        /* Controla largura máxima do input */
        div[data-testid="stTextInput"] {
            width: 300px !important;   /* ajuste a largura como preferir */
            margin: auto;              /* centraliza na tela */
        }

        /* Opcional: ajusta a caixa interna do input */
        div[data-baseweb="input"] {
            border-radius: 8px !important;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.3);
        }
        
        
         /* Centralizar e ajustar largura do botão */
         
         div.stButton {
            display: flex;
            justify-content: center; /* centraliza horizontalmente */
            margin-top: 15px; /* opcional: espaço acima */
            margin: auto;
            width: auto; /* ocupa toda a largura disponível */
           ;
        }
        div.stButton > button {
            display: flex;
            justify-content: center; /
            margin: 0 auto;      
            width: 150px;          
            border-radius: 8px !important;
            font-weight: bold;
                 
        }
        
        

    
    </style>
    
    <h1 style="text-align: center;
            top: 6rem;
            color: white;
            font-size: 3rem;
            margin-top: 3rem;
            ">Bem-vindo ao Painel de dados da shark </h1>
    
    <p style="text-align: center;
            color: white;
            font-size: 10px;
            margin-top: 1rem;
            </p>

            
            
            
""", unsafe_allow_html=True)



#  ----- estado de segurança -----

# Inicializa estado de login
if "login" not in st.session_state:
    st.session_state.login = False
# __________________________


if st.session_state.login:
    st.success("✅ Você está logado! 😊👍 ")
    if st.button("Sair"):
        st.session_state.login = False
        st.switch_page("login.py") 
else:
    st.warning("⚠️ Por favor, faça login :shark:")
# __________________________


    # Layout com colunas
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      #  st.markdown("# Faça seu login :shark:")

        # Campos de entrada
        usuario = st.text_input("Usuário", value="", key="usuario_input")
        senha = st.text_input("Senha", type="password", value="", key="senha_input")

        # Botão de login
        if st.button("Entrar", key="entrar"):
            if usuario == LOGIN_CORRETO and senha == SENHA_CORRETA:
                st.session_state.login = True

                # Mostra spinner de carregamento
                with st.spinner("🔄 Entrando no painel..."):
                    time.sleep(2)  # espera 2 segundos (pode ajustar para 3)

                st.success("✅ Login realizado com sucesso!")
                time.sleep(2)  # dá um tempinho para o usuário ver o sucesso
                st.switch_page("dash.py")  # Redireciona para o dashboard

            else:
                    st.session_state.login = False
                    st.error("Usuário ou senha incorretos.")
##  ----- fim estado de segurança -----

