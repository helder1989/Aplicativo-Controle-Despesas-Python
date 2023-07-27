# importando SQLite

import sqlite3 as lite

# criando conexão com o banco de dados

con = lite.connect("despesas2.db")

# Criando tabela de categoria
cur = con.cursor()
cur.execute("CREATE TABLE Categorias(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

# Criando tabela de receita, valor total
cur = con.cursor()
cur.execute("CREATE TABLE Receitas(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT adicionando_em DATE, valor DECIMAL)")

# Criando tabela de gastos
cur = con.cursor()
cur.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT retirado_em DATE, valor DECIMAL)")

# Fechando a conexão com o banco de dados após as operações
con.close()