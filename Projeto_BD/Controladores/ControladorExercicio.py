from psycopg import connection
from psycopg.rows import class_row
from Classes.Entidades import Exercicios
from fastapi import HTTPException

# Função para criar um exercício novo
def criar_exercicio(nome_exercicio: str, qtd_series: int, qtd_reps: int, tempo_descanso:int,
                    tecnica_avancada: str, tipo_treino: str, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("INSERT INTO exercicios (nome_exercicio, qtd_series, qtd_reps, tempo_descanso, tecnica_avancada, tipo_treino) "
                    "VALUES (%s, %s, %s, %s, %s, %s) RETURNING * ", 
                    nome_exercicio, qtd_series, qtd_reps, tempo_descanso, tecnica_avancada, tipo_treino)


# Funções para alterar dados
def alterar_nome_exercicio(id: int, novo_nome: str, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("UPDATE exercicios SET nome_exercicio = %s WHERE id_exercicio = %s", (novo_nome, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
    
def alterar_qtd_series(id: int, nova_qtd: int, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("UPDATE exercicios SET qtd_series = %s WHERE id_exercicio = %s", (nova_qtd, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    

def alterar_qtd_reps(id: int, nova_qtd: int, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("UPDATE exercicios SET qtd_reps = %s WHERE id_exercicio = %s", (nova_qtd, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp


def alterar_tempo_descanso(id: int, novo_tempo: int, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("UPDATE exercicios SET tempo_descanso = %s WHERE id_exercicio = %s", (novo_tempo, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp


def alterar_tecnica_avancada(id: int, nova_tecnica: str, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("UPDATE exercicios SET tecnica_avancada = %s WHERE id_exercicio = %s", (nova_tecnica, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp


def alterar_tipo_treino(id: int, novo_tipo: str, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("UPDATE exercicios SET tipo_treino = %s WHERE id_exercicio = %s", (novo_tipo, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp


# Funções para pesquisar dados
def pesquisar_por_nome(nome: str, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("SELECT * FROM exercicios WHERE nome_exercicio = %", (nome,))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp


def pesquisar_por_id(id: int, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("SELECT * FROM exercicios WHERE id_exercicio = %s", (id,))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp


# Funçöes para remover dados
def remover_por_id(id: int, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("DELETE FROM exercicios WHERE id_exercicio = %s RETURNING *", (id,))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp


def remover_por_nome(nome: str, conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("DELETE FROM exercicios WHERE nome_exercicio = %s RETURNING *", (nome,))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp


# Função para listar tudo
def listar_exercicios(conn: connection):
    with conn.cursor(row_factory=class_row(Exercicios)) as cur:
        cur.execute("SELECT * FROM exercicios ORDER BY id_exercicio")
        return cur.fetchall()   