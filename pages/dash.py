import pandas as pd
import streamlit as st


from components.cads.cards import  card_bruto, card_caixa, card_custo, card_investimento, card_liquido
from components.graficos_line.graficoline import grafico_1, grafico_2, grafico_3
from components.graficos_barras.graficobar import grafico_horizontal, grafico_vertical

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

 # layout e estilo
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
        
        [data-testid="stHorizontalBlock"] {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
            padding: 0; 
            
            }
            
            
        [data-testid="stMarkdownContainer"] {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 3rem;
       
        }
        [data-testid="stHeadingWithActionElements"] {
       
        margin-top: -5rem;
        
         
          }
        
        [data-testid="stHeader"] {
            background: transparent;   
            }
            
        
            
        [data-testid="stSidebar"] {
                background: linear-gradient(30deg, #141E30, #243B55, #141E30);
                color: white;}
        
        
          [data-testid="stElementContainer"] {
           
          
            }
          
        
        
        div[data-testid="stVerticalBlock"] {
             
            display: flex;
            justify-content: center;
            align-items: center;   
            
     
        }
    
    
     @keyframes gradient2 {
            0% { background-position: 50% 0%; }
            50% { background-position: 50% 100%; }
            100% { background-position: 50% 0%; }
        }
       
        </style>
     <h1 style="
            text-align: center;
            background: linear-gradient(30deg, #141E30, #62799c, #141E30);
            background-size: 200% 200%;  /* IMPORTANTE para a animação */
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradient2 8s ease-in-out infinite;
            font-size: 3rem;
            margin-top: 3rem;
        ">DASHBOARD DE ESTOQUE </h1>
    
            
""", unsafe_allow_html=True)

# varáveis que vão receber os dados 

lucro_bruto = "1000"
lucro_liquido = "800"
custo = "83000"
investidos = "83000"
caixa = "50000"



                
with st.container( gap="large"): 
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        card_bruto("Quantidade no Estoque", lucro_bruto,)
        
        
    with col2:
        card_liquido("Valor Bruto do Estoque", lucro_liquido) 
        
    with col3:
       card_caixa("Caixa", caixa)  

    with col4:
         card_investimento("Investidos", investidos)
    
    
    with col5:
         card_custo("Custo do Estoque", custo)   
         
        
        
# uma pequena divisão
st.markdown("""
<div style="display: flex;">
    <div style="backgrount: transparent; height: 1rem; width: 85vw;"></div>
</div>
""", unsafe_allow_html=True) 




with st.container():
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.plotly_chart(grafico_1, use_container_width=True, key="1",config={"displayModeBar": False}, )
    with col2:
        st.plotly_chart(grafico_2, use_container_width=True, key="2",config={"displayModeBar": False})
    with col3:
        st.plotly_chart(grafico_3, use_container_width=True, key="3", config={"displayModeBar": False})
        
    
with st.container():
    col1, col2, col3 = st.columns(3, gap="large")
            
    with col1:
        st.plotly_chart(grafico_vertical, use_container_width=True, key="grafico_vertical",config={"displayModeBar": False},)   

    with col2:
        st.plotly_chart(grafico_horizontal, use_container_width=True, key="grafico_horizontal",config={"displayModeBar": False},)
