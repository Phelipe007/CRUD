from db_connection import db_connection
conexao = db_connection()

def create(nome, valor):
    cursor = conexao.cursor()

    nome = str(nome)
    valor = int(valor)
    parametros = [nome, valor]

    comando = 'INSERT INTO vendas (nome_produto, valor) VALUES ($s, $s)'

    cursor.execute(comando, parametros)
    conexao.commit()
    
    if cursor.rowcount > 0:
        cursor_status = True
    else:
        cursor_status = False

    cursor.close()
    return cursor_status

def read(id=None, nome=None, valor=None, valor_min=None, valor_max=None):
    cursor = conexao.cursor()
    parametros = []

    comando = 'SELECT idvendas, nome_produto, valor FROM vendas WHERE '

    if id is not None:
        comando += 'idvendas = %s'
        parametros.append(id)

    if nome is not None:
        comando += 'nome_produto LIKE %s'
        parametros.append(nome)

    if valor is not None:
        comando += 'valor = %s'
        parametros.append(valor)

    if valor_min is not None and valor_max is not None:
        comando += 'valor BETWEEN %s AND %s'
        parametros.append(valor_min)
        parametros.append(valor_max)

    comando += " ORDER BY idvendas ASC"

    cursor.execute(comando, parametros)
    resultado = cursor.fetchall()#ler, pegar todos os resultados da consulta


    cursor.close()
    
    return resultado

def update(nome=None, valor=None):
    cursor = conexao.cursor()
    nome = str(nome)
    valor = int(valor)
    parametros = []

    comando = "UPDATE vendas SET"

    if nome is not None:
        comando += " nome_produto = %s"
        parametros.append(nome)
    if valor is not None:
        comando += " valor = %s"
        parametros.append(valor)

    
    cursor.execute(comando, parametros)
    conexao.commit()
    
    if cursor.rowcount > 0:
        cursor_status = True
    else:
        cursor_status = False
    
    cursor.close()
    return cursor_status

    
def delete(id):
    cursor = conexao.cursor()
    id = int(id)

    comando = f"DELETE FROM vendas WHERE = $s"
    
    cursor.execute(comando, (id,))
    conexao.commit()
    
    if cursor.rowcount > 0:
        cursor_status = True
    else:
        cursor_status = False

    cursor.close()
    return cursor_status
    