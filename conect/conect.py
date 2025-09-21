import psycopg2
import os
import json

# Função para conectar ao banco de dados
def conectar_banco():
    try:
          # Carregar o arquivo JSON com as configurações
        with open("config.json", "r") as f:
            config = json.load(f)
        
        db_name = os.getenv("DBNAME")
        db_user = os.getenv("USER")
        db_password = os.getenv("PASSWORD")
        db_host = os.getenv("HOST", "localhost")  # Define 'localhost' como padrão, se não existir a variável
        db_port = os.getenv("PORT", "5432")
        
        # Estabelecendo a conexão
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        
        
        return conn  # Retorna apenas a conexão
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

# Função para obter o cursor a partir da conexão
def obter_cursor(conn):
    if conn:
        return conn.cursor()
    else:
        print("Conexão não estabelecida.")
        return None

# Função para executar uma consulta e obter resultados
def executar_consulta(cursor, query):
    try:
        cursor.execute(query)  # Executar a consulta
        return cursor.fetchall()  # Retornar todos os resultados
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return []

# Exemplo de uso
