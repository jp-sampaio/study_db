# Entendendo como se conectar um banco de dados com uma aplicação python

import sqlite3

# Conectando a um banco de dados caso ele exista, senão vai ser criado um banco com o nome passado
conexao = sqlite3.connect('alunos.db')

# Criando uma tabela no banco de dados alunos.db
# A função curso serve para utilizar comando sql no python
cursor = conexao.cursor()
# A função execute roda o comando sql que aqui cria uma tabela caso ela não exista, e não pode ter informações nulas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alunos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        turno TEXT NOT NULL,
        dataFormacao TEXT NOT NULL
    );
''')
# Salvar as alterações que foram realizadas com os comando sql
conexao.commit()

# Inserir dados na tabela 
# Inserindo os dados fixos no código
# cursor.execute('INSERT INTO Alunos (nome, turno, dataFormacao) VALUES ("Maria", "Manha", "2025-11-30")')

# Inserindo os dados de forma dinâmica
# nome = input('Informe o nome do aluno: ')
# turno = input('Informe o turno que o aluno estuda (manha, tarde ou noite): ')
# data_formatura = input('Informe a data de formatura no formato yyyy-mm-dd: ')

# cursor.execute('INSERT INTO Alunos VALUES (?, ?, ?, ?)', (2, nome, turno, data_formatura))
# conexao.commit()

# Listar os dados de uma tabela 
cursor.execute('SELECT * FROM Alunos') # Seleciona todas a colunas da tabela Alunos
alunos = cursor.fetchall() # Faz uma busca por essas tabelas
print(alunos) # Mostra ela na tela

# Alterando os dados de uma tabela 
cursor.execute('UPDATE Alunos SET dataFormacao = ? WHERE id = ?', ("2022-03-12", 1))
conexao.commit()

# Deletando dados da tabela 
cursor.execute('DELETE FROM Alunos WHERE id = ?', (1,))
conexao.commit()

# Obrigatório, no caso do SQLite, fechar a conexão, após finalizar as operações;
conexao.close()