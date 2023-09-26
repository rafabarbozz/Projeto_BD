from fastapi import HTTPException

from psycopg.rows import class_row, dict_row

from Controladores import ControladorExercicio, ControladorAluno
from Classes.Entidades.Exercicios import Exercicios
from Classes.Entidades.Aluno import Aluno
from Classes.Relacoes.Treina import Treina
from psycopg import connection

# Função para criar relação Treina
def criar_treina(Aluno: Aluno, Exercicios: Exercicios, conn: connection):
     with conn.cursor(row_factory=class_row(Treina)) as cur:
        cur.execute("INSERT INTO treina (aluno_id, exercicio_id)"
                    "VALUES (%s, %s) RETURNING *",
                    (Aluno.get_id_aluno, Exercicios.get_id_exercicio))

        return cur.fetchone()
    
    
    
# Funções para alterar dados
def alterar_aluno_id(Treina: Treina, id: int, novo_id: int, conn: connection):
    with conn.cursor(row_factory=class_row(Treina)) as cur:
        cur.execute("UPDATE treina SET aluno_id = %s "
                    "WHERE aluno_id = %s RETURNING *",
                    (novo_id, id))
        return cur.fetchone()

def alterar_exercicio_id(Treina: Treina, id: int, novo_id: int, conn: connection):
    with conn.cursor(row_factory=class_row(Treina)) as cur:
        cur.execute("UPDATE treina SET exercicio_id = %s "
                    "WHERE exercicio_id = %s RETURNING *",
                    (novo_id, id))
        return cur.fetchone()
    
    
    
# Funções para pesquisar dados
def pesquisar_por_id_aluno(aluno: Aluno, conn: connection):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM treino_aluno WHERE id_aluno = %s", (aluno.get_id_aluno(),))
        return cur.fetchall()

def pesquisar_por_nome_exercicio(exercicio: Exercicios, conn: connection):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM treino_aluno WHERE exercicio = %s", (exercicio.get_nome_exercicio(),))
        return cur.fetchall()

def pesquisar_por_tipo_treino(exercicio: Exercicios, conn: connection):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM treino_aluno WHERE tipo_treino = %s", (exercicio.get_tipo_treino(),))
        return cur.fetchall()
    
def pesquisar_por_nome_aluno(aluno: Aluno, conn: connection):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM treino_aluno WHERE nome_aluno = %s", (aluno.get_nome_aluno(),))
        return cur.fetchall()

def pesquisar_por_tecnica_avancada(exercicio: Exercicios, conn: connection):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT * FROM treino_aluno WHERE tecnica = %s", (exercicio.get_tecnica_avancada(),))
        return cur.fetchall()
    
    
    
# Funções para deletar dados
def deletar_por_id_aluno(aluno: Aluno, conn: connection):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("DELETE FROM treino_aluno WHERE id_aluno = %s", (aluno.get_id_aluno(),))
        return cur.fetchall()

def deletar_por_nome_exercicio(exercicio: Exercicios, conn: connection):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("DELETE FROM treino_aluno WHERE exercicio = %s", (exercicio.get_nome_exercicio(),))
        return cur.fetchall()

def deletar_por_tipo_treino(exercicio: Exercicios, conn: connection):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("DELETE FROM treino_aluno WHERE tipo_treino = %s", (exercicio.get_tipo_treino(),))
        return cur.fetchall()

def deletar_por_nome_aluno(aluno: Aluno, conn: connection):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("DELETE FROM treino_aluno WHERE nome_aluno = %s", (aluno.get_nome_aluno(),))
        return cur.fetchall()
    
def deletar_por_tecnica_avancada(exercicio: Exercicios, conn: connection):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("DELETE FROM treino_aluno WHERE tecnica = %s", (exercicio.get_tecnica_avancada(),))
        return cur.fetchall()



# Função para listar tudo
def listar_treino_aluno(conn: connection):
    with conn.cursor(row_factory=class_row(Treina)) as cur:
        cur.execute("SELECT * FROM treino_aluno ORDER BY id_aluno")