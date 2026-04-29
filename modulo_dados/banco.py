import sqlite3

def conectar():
    return sqlite3.connect("database.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL,
            nome TEXT NOT NULL,
            data text NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def salvar_livro(titulo, autor, genero, nome, data):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO livros (titulo, autor, genero, nome, data) VALUES (?, ?, ?, ?, ?)",
        (titulo, autor, genero, nome, data)
    )
    conexao.commit()
    conexao.close()

def buscar_livros():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    dados = cursor.fetchall()
    conexao.close()
    return dados