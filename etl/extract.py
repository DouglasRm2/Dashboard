
# Conectar ao banco
from conect.conect import conectar_banco, executar_consulta, obter_cursor


conn = conectar_banco()

if conn:
    # Obter o cursor
    cursor = obter_cursor(conn)

    if cursor:
        
        consulta = 'SELECT * FROM minha_tabela'
        resultados = executar_consulta(cursor, consulta)

       
        for resultado in resultados:
            print(resultado)

        # Fechar o cursor e a conexão
        cursor.close()
        conn.close()
