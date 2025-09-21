import pandas as pd
import plotly.express as px


def criar_grafico_area(df=None, x_col="Ano", y_cols=None, titulo="", 
                        opacidade=0.3, largura_linha=2):
    if df is None:
        df = pd.DataFrame({
            "Ano": [2008, 2018, 2020, 2021, 2022],
            "Vendas": [100, 120, 180, 150, 200],
            "Lucro": [30, 45, 60, 50, 70],
            "Custos": [70, 75, 120, 100, 130],
        })
        # variavéis para o gráfico
    if y_cols is None:
        y_cols = ["Vendas", "Lucro"]

    # Criando o gráfico de área
    fig = px.area(df, x=x_col, y=y_cols, title=titulo)
    
    # Estilizando o gráfico
    fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(size=14, color="white"),
    legend=dict(orientation="h", y=-0.2, x=0.5, xanchor="center",
                 title_text=""),
    title=dict(
        x=0.5,
        xanchor="center",
        font=dict(size=20, color="lightblue")
    ),
    margin=dict(l=20, r=20, t=60, b=40),
    
    # 🔹 Tooltip (hoverlabel)
    hoverlabel=dict(
        bgcolor="#2D4561", 
        font_size=14,
        font_color="#FFFFFF"
    )
)
    fig.update_yaxes(title_text="") # Removendo o título do eixo y
    
    # Ajustando opacidade e largura da linha
    fig.update_traces(opacity=opacidade, line=dict(width=largura_linha))
    return fig

# 🔹 Criando gráficos específicos
df1 = pd.DataFrame({
    "Ano": [2018, 2019, 2020, 2021, 2022],
    "Vendas": [100, 120, 180, 150, 200],
    "Lucro": [30, 45, 60, 50, 70],
    
})
df2 = pd.DataFrame({
    "Ano": [2010, 2011, 2012, 2013, 2014],
    "Vendas": [150, 160, 170, 180, 190],
    "Lucro": [40, 45, 50, 55, 60],
    "Custos": [110, 115, 120, 125, 130],
})
df3 = pd.DataFrame({
    "Ano": [2015, 2016, 2017, 2018, 2019],
    "Vendas": [200, 210, 220, 230, 240],
    "Lucro": [60, 65, 70, 75, 80],
    
})

grafico_1 = criar_grafico_area(df1, titulo="Vendas")
grafico_2 = criar_grafico_area(df2, titulo="Caixa")
grafico_3 = criar_grafico_area(df3, titulo="Custo")
