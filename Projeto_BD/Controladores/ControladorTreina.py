from psycopg2 import connect, DatabaseError
from DataBase.DB_config.config_db import config
from Classes.Entidades.Exercicios import Exercicios
from Classes.Entidades.Aluno import Aluno
from Classes.Relacoes.Treina import Treina 

# Função para criar relação Treina
def criar_treina(Aluno: Aluno, Exercicios: Exercicios):
    connection = None
    
    try:
        params = config()
        with connect(**params) as conn:
            with conn.cursor() as cur:
                insert_script = 'INSERT INTO treina (aluno_id, exercicio_id) VALUES (%s, %s) RETURNING * '
                insert_value = (Aluno.get_id_aluno, Exercicios.get_id_exercicio)
                cur.execute(insert_script, insert_value)
                
                return cur.fetchone()
        
    except (Exception, DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()
    
    
    
# Funções para alterar dados
def alterar_aluno_id(id: int, novo_id: int):
    connection = None
    
    try:
        params = config()
        with connect(**params) as conn:
            with conn.cursor() as cur:
                insert_script = 'UPDATE treina SET aluno_id = %s WHERE id_treino = %s RETURNING *'
                insert_value = (novo_id, id)
                cur.execute(insert_script, insert_value)
                
                return cur.fetchone()
                
    except (Exception, DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()

def alterar_exercicio_id(id: int, novo_id: int):
    connection = None
    
    try:
        params = config()
        with connect(**params) as conn:
            with conn.cursor() as cur:
                insert_script = 'UPDATE treina SET exercicio_id = %s WHERE id_treino = %s RETURNING *'
                insert_value = (novo_id, id)
                cur.execute(insert_script, insert_value)
                
                return cur.fetchone()
                
    except (Exception, DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()
    
    
# Funções para pesquisar dados
def pesquisar_por_id_aluno(aluno: Aluno):
    connection = None
    
    try:
        params = config()
        with connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM treino_aluno WHERE aluno_id = %s', (Aluno.get_id_aluno(),))
                
                return cur.fetchone()
                
    except (Exception, DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()  

def pesquisar_por_nome_exercicio(exercicio: Exercicios):
    connection = None
    
    try:
        params = config()
        with connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM treino_aluno WHERE nome_exercicio = %s', (exercicio.get_nome_exercicio(),))
                
                return cur.fetchone()
                
    except (Exception, DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()  

def pesquisar_por_tipo_treino(exercicio: Exercicios):
    connection = None
    
    try:
        params = config()
        with connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM treino_aluno WHERE tipo_treino = %s', (exercicio.get_tipo_treino(),))
                
                return cur.fetchone()
                
    except (Exception, DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()  
    
def pesquisar_por_nome_aluno(aluno: Aluno):
    connection = None
    
    try:
        params = config()
        with connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM treino_aluno WHERE nome = %s', (aluno.get_nome_aluno(),))
                
                return cur.fetchone()
                
    except (Exception, DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()  

def pesquisar_por_tecnica_avancada(exercicio: Exercicios):
    connection = None
    
    try:
        params = config()
        with connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM treino_aluno WHERE tecnica = %s', (exercicio.get_tecnica_avancada(),))
                
                return cur.fetchone()
                
    except (Exception, DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()  
    
    
    
# Funções para remover dados
def deletar_por_id_aluno(aluno: Aluno):
    connection = None
    
    try:
        params = config()
        with connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('DELETE FROM treino_aluno WHERE id_aluno = %s RETURNING *', (aluno.get_id_aluno,))
                
                return cur.fetchone()
                
    except (Exception, DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()


# Função para listar tudo
def listar_treino_aluno():
    connection = None
    
    try:
        params = config()
        with connect(**params) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM treino_aluno ORDER BY id_aluno')
                
                return cur.fetchall()
                
    except (Exception, DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close() 