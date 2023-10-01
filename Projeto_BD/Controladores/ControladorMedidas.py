from psycopg2 import connect, DatabaseError
from DataBase.DB_config.config_db import config

class GerenciadorMedidas:
    # Função para criar medidas
    def criar_medida(coxa_esq: float, coxa_dir: float, braco_esq: float, braco_dir: float, 
                    altura: float, cintura: float, peso: float): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'INSERT INTO medidas (coxa_esq, coxa_dir, braco_esq, braco_dir, altura, cintura, peso) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING * '
                    insert_value = (coxa_esq, coxa_dir, braco_esq, braco_dir, altura, cintura, peso)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
            
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
            
            

    # Funções para alterar dados
    def alterar_coxa_esq(id: int, nova_medida: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE medidas SET coxa_esq = %s WHERE id_medida = %s RETURNING *'
                    insert_value = (nova_medida, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def alterar_coxa_dir(id: int, nova_medida: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE medidas SET coxa_dir = %s WHERE id_medida = %s RETURNING *'
                    insert_value = (nova_medida, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()

    def alterar_braco_esq(id: int, nova_medida: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE medidas SET braco_esq = %s WHERE id_medida = %s RETURNING *'
                    insert_value = (nova_medida, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()

    def alterar_braco_dir(id: int, nova_medida: str): #Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE medidas SET braco_dir = %s WHERE id_medida = %s RETURNING *'
                    insert_value = (nova_medida, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()

    def alterar_altura(id:int, nova_altura: float): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE medidas SET altura = %s WHERE id_medida = %s RETURNING *'
                    insert_value = (nova_altura, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def alterar_cintura(id:int, nova_cintura: float): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE medidas SET cintura = %s WHERE id_medida = %s RETURNING *'
                    insert_value = (nova_cintura, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def alterar_peso(id:int, novo_peso: float):
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE medidas SET peso = %s WHERE id_medida = %s RETURNING *'
                    insert_value = (novo_peso, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
        
        
    # Funções para pesquisar dados
    def pesquisar_por_id(id: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM medidas WHERE id_medida = %s', (id,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()   
                
    def pesquisar_por_coxa_esq(coxa_esq: float):
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM medidas WHERE coxa_esq = %s', (coxa_esq,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def pesquisar_por_coxa_dir(coxa_dir: float):
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM medidas WHERE coxa_dir = %s', (coxa_dir,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def pesquisar_por_braco_esq(braco_esq: float):
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM medidas WHERE braco_esq = %s', (braco_esq,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def pesquisar_por_braco_dir(braco_dir: float):
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM medidas WHERE braco_dir = %s', (braco_dir,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def pesquisar_por_altura(altura: float):
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM medidas WHERE altura = %s', (altura,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def pesquisar_por_cintura(cintura: float):
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM medidas WHERE cintura = %s', (cintura,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def pesquisar_por_peso(peso: float):
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM medidas WHERE peso = %s', (peso,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
        
        
    # Funções para remover dados
    def remover_por_id(id: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('DELETE FROM medidas WHERE id_medida = %s RETURNING *', (id,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
        

    # Funções para listar tudo
    def listar_medidas(): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM medidas ORDER BY id_medida')
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close() 