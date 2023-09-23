from psycopg import connection
from psycopg.rows import class_row
from Classes.Entidades import Medidas
from fastapi import HTTPException

# Função para criar medidas
def criar_medida(coxa_esq: float, coxa_dir: float, braco_esq: float, braco_dir: float, 
                 altura: float, cintura: float, peso: float, conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("INSERT INTO medidas () "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING * ", 
                    coxa_esq, coxa_dir, braco_esq, braco_dir, altura, cintura, peso)
        
        

# Funções para alterar dados
def alterar_coxa_esq(id: int, nova_medida: str, conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("UPDATE medidas SET coxa_esq = %s WHERE id_exercicio = %s", (nova_medida, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
def alterar_coxa_dir(id: int, nova_medida: str, conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("UPDATE medidas SET coxa_dir = %s WHERE id_exercicio = %s", (nova_medida, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp


def alterar_braco_esq(id: int, nova_medida: str, conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("UPDATE medidas SET braco_esq = %s WHERE id_exercicio = %s", (nova_medida, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp

def alterar_braco_dir(id: int, nova_medida: str, conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("UPDATE medidas SET braco_dir = %s WHERE id_exercicio = %s", (nova_medida, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp

def alterar_altura(id:int, nova_altura: float, conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("UPDATE medidas SET altura = %s WHERE id_exercicio = %s", (nova_altura, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
def alterar_cintura(id:int, nova_cintura: float, conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("UPDATE medidas SET altura = %s WHERE id_exercicio = %s", (nova_cintura, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
def alterar_peso(id:int, novo_peso: float, conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("UPDATE medidas SET altura = %s WHERE id_exercicio = %s", (novo_peso, id))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
    
    
# Funções para pesquisar dados
def pesquisar_por_id(id: int, conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("SELECT * FROM medidas WHERE id_medidas = %s", (id,))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
    
    
# Funções para remover dados
def remover_por_id(id: str, conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("DELETE FROM medidas WHERE id_medidas = %s RETURNING *", (id,))
        temp = cur.fetchone()
        
        if temp is None:
            raise HTTPException(status_code=404)
        
        return temp
    
    

# Funções para listar tudo
def listar_exercicios(conn: connection):
    with conn.cursor(row_factory=class_row(Medidas)) as cur:
        cur.execute("SELECT * FROM medidas ORDER BY id_medidas")
        return cur.fetchall() 