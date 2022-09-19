import sqlite3
from sqlite3 import Error

def conexao():
    caminho = "banco.db"
    try:
        con = None
        con = sqlite3.connect(caminho)
        return con
    except Error as error:
        print(error)

sql_inserir = 'INSERT INTO cliente VALUES(NULL,"Teste2","00000000000");'
sql_tabela = '''CREATE TABLE cliente(
                id INTEGER PRIMARY KEY,
                nome VARCHAR(60) NOT NULL,
                cpf VARCHAR(11) NOT NULL);'''

sql_remover = 'DELETE FROM cliente WHERE id=4;'

sql_atualizar = 'UPDATE cliente SET nome="Bill" WHERE id=1;'

sql_consultar = 'SELECT * FROM cliente;'

def consultar(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        con.close()
        return resultado
    except Error as er:
        print(er)

def atualizar(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        print("Registro atualizado com sucesso!")
    except Error as er:
        print(er)

def remover(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        print('Registro removido com sucesso!')
    except Error as er:
        print(er)

def inserir(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        con.close()
        print('Registro inserido com sucesso!')
    except Error as er:
        print(er)

def tabela(sql):
    try:
        con = conexao()
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print("Tabela criada!")
        con.close()
    except Error as er:
        print(er)

#tabela(sql_tabela)
#inserir(sql_inserir)
#remover(sql_remover)
#atualizar(sql_atualizar)
#for i in consultar(sql_consultar):
#    print(i)

