from db_connection import db_connection
conexao = db_connection()

def create(nome, valor):
    cursor = conexao.cursor()

    nome = str(nome)
    valor = int(valor)

    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome}", {valor})'

    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    
    if cursor.rowcount > 0:
        cursor_status = True
    else:
        cursor_status = False
    return cursor_status

def read(id=None, nome=None, valor=None):
    cursor = conexao.cursor()

    id = int(id)
    nome = str(nome)
    valor = str(valor)

    comando = f'SELECT {id, nome, valor} FROM vendas'

    cursor.execute(comando)
    resultado = cursor.fetchall()#ler, pegar todos os resultados da consulta

    conexao.commit()

    cursor.close()
    conexao.close()
    return resultado

def update(nome=None, valor=None):
    cursor = conexao.cursor()
    nome = str(nome)
    valor = int(valor)

    if valor == None and nome != None:
        comando = f"UPDATE vendas SET nome_produto = {nome}"
    elif nome == None and nome != None:
        comando = f"UPDATE vendas SET valor = {valor}"
    elif nome and valor != None:
        comando = f"UPDATE vendas SET nome_produto = {nome}, valor = {valor}"

    cursor.execute(comando)
    conexao.commit()
    
    conexao.close()
    cursor.close()

    if cursor.rowcount > 0:
        cursor_status = True
    else:
        cursor_status = False
    return cursor_status
    
 def delete(id=None, nome=None, valor=None):
    cursor = conexao.cursor()
    id = int(id)
    nome = str(nome)
    valor = int(valor)

    comando = f"DELETE VALUES {id} FROM vendas TABLE = idvendas"
    
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    return cursor_status