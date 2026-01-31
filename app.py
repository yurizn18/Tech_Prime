import mysql.connector
def conectar_database():
        try:
            conexao = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "20122006",
                database = "fila_digital"
            )
            return conexao
        except:
            return None

conexao_teste = conectar_database()
if conexao_teste is not None:
    print("Sucesso!")
    conexao_teste.close()
else: 
    print("Erro ao estabelecer a conexão")