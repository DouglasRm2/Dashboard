import plotly.express as px
import pandas as pd
def criar_grafico_barra(df, x_col="Ano", y_cols=None, titulo="Gráfico de Barras", 
                        opacidade=0.8, cor_titulo="lightblue", horizontal=False):
    """
    Cria gráfico de barras estilizado no mesmo padrão do gráfico de área.
    """
    
    if y_cols is None:
        y_cols = [col for col in df.columns if col != x_col]

    # Se horizontal, inverter x e y
    if horizontal:
        fig = px.bar(df, y=x_col, x=y_cols, title=titulo, orientation="h", barmode="group")
    else:
        fig = px.bar(df, x=x_col, y=y_cols, title=titulo, barmode="group")

    # Layout estilizado
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(size=14, color="white"),
        legend=dict(
            orientation="h",
            y=-0.2,
            x=0.5,
            xanchor="center",
            title_text=""   # 🔹 Remove "variable" da legenda
        ),
        title=dict(
            x=0.5,
            xanchor="center",
            font=dict(size=20, color=cor_titulo)
        ),
        margin=dict(l=20, r=20, t=60, b=40),
        
        # Tooltip customizado
        hoverlabel=dict(
            bgcolor="#2D4561",
            font_size=14,
            font_color="#FFFFFF"
        )
    )

    # Remover labels dos eixos
    fig.update_xaxes(title_text="")
    fig.update_yaxes(title_text="")

    # Ajustar opacidade das barras
    fig.update_traces(opacity=opacidade)

    return fig


# 🔹 Exemplo
df1 = pd.DataFrame({
    "Ano": [2018, 2019, 2020, 2021, 2022],
    "Vendas": [100, 120, 180, 150, 200],
    "Lucro": [30, 45, 60, 50, 70],
})

grafico_vertical = criar_grafico_barra(df1, titulo="Vendas (Vertical)", horizontal=False)
grafico_horizontal = criar_grafico_barra(df1, titulo="Vendas (Horizontal)", horizontal=True)
