import sqlite3

# Conectar-se a um banco de dados ou entrar em um já existente
def conectar_db(nome_db):
    conexao = sqlite3.connect(nome_db)
    return conexao

# Criar a tabela do banco de dados 
def criar_tabela(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Alunos (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            turno TEXT NOT NULL,
            dataFormatura TEXT NOT NULL
        );
    ''')

    conexao.commit()

# Inserir dados na tabela 
def inserir_alunos(conexao, id, nome, turno, dataFormatura):
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO Alunos VALUES (?, ?, ?, ?)', (id, nome, turno, data_formatura))

    conexao.commit()


# Listar todos os dados de uma tabela 
def selecionar_todos_alunos(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Alunos')
    return cursor.fetchall()


# Alterar dados de uma tabela
def atualizar_alunos(conexao, id, cargo):
    cursor = conexao.cursor()
    cursor.execute('UPDATE Alunos SET turno = ? WHERE id = ?', (cargo, id))

    conexao.commit()

# Como excluir dados de uma tabela
def deletar_alunos(conexao, id):
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM Alunos WHERE id = ?', (id,))

    conexao.commit()


# Utilizando as funções 

# Criando ou entrando em um banco de dados 
conexao = conectar_db('Alunos.db')

# Criando uma tabela
criar_tabela(conexao)

# Exemplos de como receber dados do usuário na sua aplicação e depois passar para o banco de dados 
# nome = input('Digite o nome: ')
# turno = input('Digite o turno: ')
# data_formatura = input('Digite uma data no formato yyyy-mm-dd: ')

# inserir_alunos(conexao, 1, nome, turno, data_formatura)
# inserir_alunos(conexao, 2, nome, turno, data_formatura)

# Imprimir os dados da tabela na tela
print(selecionar_todos_alunos(conexao))

# Alterando os dados da tabela 
atualizar_alunos(conexao, 2, 'Noite')

# Imprimir os dados da tabela na tela
print(selecionar_todos_alunos(conexao))


# Deletando aluno da tabela
deletar_alunos(conexao, 2)

# Imprimir os dados da tabela na tela
print(selecionar_todos_alunos(conexao))

# Obrigatório, no caso do SQLite, fechar a conexão após finalizar as operações
conexao.close()