import streamlit as st
import pandas as pd



#  altura e largura padrão dos cards


def card_bruto(title, value):
    st.markdown(
        f"""
        <div style="
    background: linear-gradient(135deg, #19273C, #19273C, #19273C, #19273C, #5F7697);
    border-radius: 12px;
    padding: 20px;
    color: white;
    max-width: 400px;       /* limite de largura */
    width: 90%;            /* ocupa o espaço disponível */
    min-height: 120px;      /* altura mínima */
    display: flex;          /* flexbox para centralizar */
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: Arial, sans-serif;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    overflow: hidden;       /* evita estouro de conteúdo */
    word-wrap: break-word;  /* quebra palavras longas */
">
    <p style="margin: 0; font-size: clamp(25px, 2vw, 20px); opacity: 0.8;">
        {title}
    </p>
    <p style="margin: 0; font-size: clamp(30px, 3vw, 28px); font-weight: bold;">
        {value}
    </p>
</div>
        """,
        
        unsafe_allow_html=True
    )
    

def card_custo(title, value):
    st.markdown(
        f"""
       <div style="
    background: linear-gradient(135deg, #19273C, #19273C, #19273C, #19273C, #5F7697);
    border-radius: 12px;
    padding: 20px;
    color: white;
    max-width: 400px;       /* limite de largura */
    width: 90%;            /* ocupa o espaço disponível */
    min-height: 120px;      /* altura mínima */
    display: flex;          /* flexbox para centralizar */
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: Arial, sans-serif;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    overflow: hidden;       /* evita estouro de conteúdo */
    word-wrap: break-word;  /* quebra palavras longas */
">
    <p style="margin: 0; font-size: clamp(25px, 2vw, 20px); opacity: 0.8;">
        {title}
    </p>
    <p style="margin: 0; font-size: clamp(30px, 3vw, 28px); font-weight: bold;">
        {value}
    </p>
</div>
        """,
        unsafe_allow_html=True
    )



def card_liquido(title, value):
    st.markdown(
        f"""
        <div style="
    background: linear-gradient(135deg, #19273C, #19273C, #19273C, #19273C, #5F7697);
    border-radius: 12px;
    padding: 20px;
    color: white;
    max-width: 400px;       /* limite de largura */
    width: 90%;            /* ocupa o espaço disponível */
    min-height: 120px;      /* altura mínima */
    display: flex;          /* flexbox para centralizar */
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: Arial, sans-serif;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    overflow: hidden;       /* evita estouro de conteúdo */
    word-wrap: break-word;  /* quebra palavras longas */
">
    <p style="margin: 0; font-size: clamp(25px, 2vw, 20px); opacity: 0.8;">
        {title}
    </p>
    <p style="margin: 0; font-size: clamp(30px, 3vw, 28px); font-weight: bold;">
        {value}
    </p>
</div>
        """,
        unsafe_allow_html=True
    )




def card_investimento(title, value):
    st.markdown(
        f"""
       <div style="
    background: linear-gradient(135deg, #19273C, #19273C, #19273C, #19273C, #5F7697);
    border-radius: 12px;
    padding: 20px;
    color: white;
    max-width: 400px;      
    width: 90%;            
    min-height: 120px;      
    display: flex;        
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: Arial, sans-serif;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    overflow: hidden;     
    word-wrap: break-word;  
">
    <p style="margin: 0; font-size: clamp(25px, 2vw, 20px); opacity: 0.8;">
        {title}
    </p>
    <p style="margin: 0; font-size: clamp(30px, 3vw, 28px); font-weight: bold;">
        {value}
    </p>
</div>
        """,
        unsafe_allow_html=True
    )
    
    



def card_caixa(title, value):
    
    st.markdown(
        f"""
        <div style="
    background: linear-gradient(135deg, #19273C,  #19273C, #19273C, #19273C, #19273C, #5F7697);
    border-radius: 12px;
    padding: 20px;
    color: white;
    max-width: 400px;       /* limite de largura */
    width: 90%;            /* ocupa o espaço disponível */
    min-height: 120px;      /* altura mínima */
    display: flex;          /* flexbox para centralizar */
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    font-family: Arial, sans-serif;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    overflow: hidden;       /* evita estouro de conteúdo */
    word-wrap: break-word;  /* quebra palavras longas */
">
    <p style="margin: 0; font-size: clamp(25px, 2vw, 20px); opacity: 0.8;">
        {title}
    </p>
    <p style="margin: 0; font-size: clamp(30px, 3vw, 28px); font-weight: bold;">
        {value}
    </p>
</div>
        """,
       
        unsafe_allow_html=True
    )