from psycopg import connection
from psycopg.rows import class_row
from Classes.Entidades import Aluno
from fastapi import HTTPException

# Função para criar novo aluno
def criar_aluno(nome: str, cpf: str, sexo: str, medida_id: int, conn: connection):
    with conn.cursor(row_factory=class_row(Aluno)) as cur:
        cur.execute("INSERT INTO aluno (nome_aluno, cpf_aluno, sexo_aluno, medida_id) "
                    "VALUES (%s, %s, %s, %s) RETURNING * ", 
                    nome, cpf, sexo, medida_id)
        
        
        
# Função para alterar dados
def alterar_nome(id: int, novo_nome: str, conn: connection):
    with conn.cursor(row_factory=class_row(Aluno)) as cur:
        cur.execute("UPDATE aluno SET nome_aluno = %s WHERE id_aluno = %s", (novo_nome, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
        
def alterar_cpf(id: int, novo_cpf: str, conn: connection):
    with conn.cursor(row_factory=class_row(Aluno)) as cur:
        cur.execute("UPDATE aluno SET cpf_aluno = %s WHERE id_aluno = %s", (novo_cpf, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
def alterar_sexo(id: int, novo_sexo: str, conn: connection):
    with conn.cursor(row_factory=class_row(Aluno)) as cur:
            cur.execute("UPDATE aluno SET sexo_aluno = %s WHERE id_aluno = %s", (novo_sexo, id))
            temp = cur.fetchone()
            
            if temp is None:
                raise HTTPException(status_code=404)
            
            return temp
            
def alterar_medida_id(id: int, novo_medida_id: int, conn: connection):
    with conn.cursor(row_factory=class_row(Aluno)) as cur:
        cur.execute("UPDATE aluno SET medida_id = %s WHERE id_aluno = %s", (novo_medida_id, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
    

# Funções para pesquisar dados
def pesquisar_por_nome(nome: str, conn: connection):
    with conn.cursor(row_factory=class_row(Aluno)) as cur:
        cur.execute("SELECT * FROM aluno WHERE nome_aluno = %", (nome,))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
def pesquisar_por_cpf(cpf: str, conn: connection):
    with conn.cursor(row_factory=class_row(Aluno)) as cur:
        cur.execute("SELECT * FROM aluno WHERE cpf_aluno = %", (cpf,))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
    
# Funções para remover dados
def remover_por_nome(nome: str, conn: connection):
    with conn.cursor(row_factory=class_row(Aluno)) as cur:
        cur.execute("DELETE FROM aluno WHERE nome_aluno = %s RETURNING *", (nome,))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
def remover_por_id(id: int, conn: connection):
    with conn.cursor(row_factory=class_row(Aluno)) as cur:
        cur.execute("DELETE FROM aluno WHERE id_aluno = %s RETURNING *", (id,))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp



# Função para listar tudo
def listar_exercicios(conn: connection):
    with conn.cursor(row_factory=class_row(Aluno)) as cur:
        cur.execute("SELECT * FROM aluno ORDER BY id_aluno")
        return cur.fetchall()  
