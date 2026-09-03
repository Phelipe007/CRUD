from db_connection import db_connection
conexao = db_connection()

def create(nome_produto, valor):
    cursor = conexao.cursor()

    nome_produto = str(nome_produto)
    valor = int(valor)

    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    
    if cursor.rowcount > 0:
        cursor_status = True
    else:
        cursor_status = False
    return cursor_status

def read(id, nome, valor):
    cursor = conexao.cursor()

    id = id
    nome = nome
    valor = valor

    comando = f'SELECT {id, nome, valor} FROM vendas'

    cursor.execute(comando)
    resultado = cursor.fetchall()#ler, pegar todos os resultados da consulta

    conexao.commit()

    cursor.close()
    conexao.close()
    return resultado
 

 