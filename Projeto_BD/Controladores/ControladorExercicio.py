from psycopg2 import connect, DatabaseError
from DataBase.DB_config.config_db import config

class GerenciadorExercicio:
    def __init__(self):
        pass
    
    # Função para criar um exercício novo
    @staticmethod
    def criar_exercicio(nome_exercicio: str, qtd_series: int, qtd_reps: int, tempo_descanso:int,
                        tecnica_avancada: str, tipo_treino: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'INSERT INTO exercicios (nome_exercicio, qtd_series, qtd_reps, tempo_descanso, tecnica_avancada, tipo_treino) VALUES (%s, %s, %s, %s, %s, %s) RETURNING * '
                    insert_value = (nome_exercicio, qtd_series, qtd_reps, tempo_descanso, tecnica_avancada, tipo_treino)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
            
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
                


    # Funções para alterar dados
    @staticmethod
    def alterar_nome_exercicio(id: int, novo_nome: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE exercicios SET nome_exercicio = %s WHERE id_exercicio = %s RETURNING *'
                    insert_value = (novo_nome, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
     
    @staticmethod   
    def alterar_qtd_series(id: int, nova_qtd: int): # funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE exercicios SET qtd_series = %s WHERE id_exercicio = %s RETURNING *'
                    insert_value = (nova_qtd, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
    
    @staticmethod
    def alterar_qtd_reps(id: int, nova_qtd: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE exercicios SET qtd_reps = %s WHERE id_exercicio = %s RETURNING *'
                    insert_value = (nova_qtd, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()

    @staticmethod
    def alterar_tempo_descanso(id: int, novo_tempo: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE exercicios SET tempo_descanso = %s WHERE id_exercicio = %s RETURNING *'
                    insert_value = (novo_tempo, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
         
    @staticmethod
    def alterar_tecnica_avancada(id: int, nova_tecnica: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE exercicios SET tecnica_avancada = %s WHERE id_exercicio = %s RETURNING *'
                    insert_value = (nova_tecnica, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()

    @staticmethod
    def alterar_tipo_treino(id: int, novo_tipo: str): # Funiconando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE exercicios SET tipo_treino = %s WHERE id_exercicio = %s RETURNING *'
                    insert_value = (novo_tipo, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()



    # Funções para pesquisar dados
    @staticmethod
    def pesquisar_por_id(id: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM exercicios WHERE id_exercicio = %s', (id,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close() 
                
    @staticmethod          
    def pesquisar_por_nome(nome: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM exercicios WHERE nome_exercicio = %s', (nome,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
    
    @staticmethod          
    def pesquisar_por_qtd_series(qtd: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM exercicios WHERE qtd_series = %s', (qtd,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close() 
       
    @staticmethod         
    def pesquisar_por_qtd_reps(qtd: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM exercicios WHERE qtd_reps = %s', (qtd,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()   
    
    @staticmethod  
    def pesquisar_por_tempo_descanso(tempo: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('select * from exercicios where tempo_descanso = %s', (tempo,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()    
    
    @staticmethod     
    def pesquisar_por_tecnica(tecnica: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM exercicios WHERE tecnica_avancada = %s', (tecnica,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()   
    
    @staticmethod      
    def pesquisar_por_tipo_treino(tipo: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM exercicios WHERE tipo_treino = %s', (tipo,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()  



    # Funçöes para remover dados
    @staticmethod
    def remover_por_nome(nome: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('DELETE FROM exercicios WHERE nome_exercicio = %s RETURNING *', (nome,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
     
    @staticmethod   
    def remover_por_id(id: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('DELETE FROM exercicios WHERE id_exercicio = %s RETURNING *', (id,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        


    # Função para listar tudo
    @staticmethod
    def listar_exercicios(): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM exercicios ORDER BY id_exercicio')
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()   