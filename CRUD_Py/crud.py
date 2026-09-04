from db_connection import db_connection
conexao = db_connection()

def create(nome, valor):
    cursor = conexao.cursor()

    nome = str(nome)
    valor = int(valor)

    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome}", {valor})'

    cursor.execute(comando)
    conexao.commit()
    
    if cursor.rowcount > 0:
        cursor_status = True
    else:
        cursor_status = False

    cursor.close()
    conexao.close()
    return cursor_status

def read(id=None, nome=None, valor=None, valor_min=None, valor_max=None):
    cursor = conexao.cursor()
    parametros = []

    comando = 'SELECT idvendas, nome_produto, valor FROM vendas WHERE '

    if id is not None:
        comando += f'idvendas = %s'
        parametros.append(f"{id}")

    elif nome is not None:
        comando += f'nome_produto LIKE %s'
        parametros.append(f"%{nome}%")

    elif valor is not None:
        comando += f'valor = %s'
        parametros.append(f"{valor}")

    elif valor_min and valor_max is not None:
        comando += f'valor BETWEEN $s AND %s'
        parametros.append(f"{valor_min}")
        parametros.append(f"{valor_max}")

    comando += " ORDER BY idvendas ASC"

    cursor.execute(comando (parametros, ))
    resultado = cursor.fetchall()#ler, pegar todos os resultados da consulta

    conexao.commit()

    cursor.close()
    conexao.close()
    return resultado

def update(nome=None, valor=None):
    cursor = conexao.cursor()
    nome = str(nome)
    valor = int(valor)

    omando = f"UPDATE vendas SET"

    if nome is not None:
        comando += f" nome_produto = {nome}"
    elif valor is not None:
        comando += f" valor = {valor}"

    if cursor.rowcount > 0:
        cursor_status = True
    else:
        cursor_status = False
    return cursor_status

    cursor.execute(comando)
    conexao.commit()
    
    conexao.close()
    cursor.close()

    
def delete(id, nome, valor):
    cursor = conexao.cursor()
    id = int(id)
    nome = str(nome)
    valor = int(valor)

    comando = f"DELETE VALUES {id} FROM vendas TABLE = idvendas"
    
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()