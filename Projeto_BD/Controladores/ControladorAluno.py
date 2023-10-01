from psycopg2 import connect, DatabaseError
from DataBase.DB_config.config_db import config

class GerenciadorAluno:
    # Função para criar novo aluno
    def criar_aluno(nome: str, cpf: str, sexo: str, medida_id: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'INSERT INTO aluno (nome_aluno, cpf_aluno, sexo_aluno, medida_id) VALUES (%s, %s, %s, %s) RETURNING *'
                    insert_value = (nome, cpf, sexo, medida_id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
            
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
            
            
            
    # Função para alterar dados 
    def alterar_nome(id: int, novo_nome: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE aluno SET nome_aluno = %s WHERE id_aluno = %s RETURNING *'
                    insert_value = (novo_nome, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
            
    def alterar_cpf(id: int, novo_cpf: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE aluno SET cpf_aluno = %s WHERE id_aluno = %s RETURNING *'
                    insert_value = (novo_cpf, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def alterar_sexo(id: int, novo_sexo: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE aluno SET sexo_aluno = %s WHERE id_aluno = %s RETURNING *'
                    insert_value = (novo_sexo, id)
                    cur.execute(insert_script, insert_value)
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
                
    def alterar_medida_id(id: int, novo_medida_id: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    insert_script = 'UPDATE aluno SET medida_id = %s WHERE id_aluno = %s RETURNING *'
                    insert_value = (novo_medida_id, id)
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
                    cur.execute('SELECT * FROM aluno WHERE id_aluno = %s', (id,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close() 
                
    def pesquisar_por_nome(nome: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM aluno WHERE nome_aluno = %s', (nome,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close() 
        
    def pesquisar_por_cpf(cpf: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM aluno WHERE cpf_aluno = %s', (cpf,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close() 
    
    def pesquisar_por_sexo(sexo: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM aluno WHERE sexo_aluno = %s', (sexo,))
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close() 

        
        
    # Funções para remover dados
    def remover_por_nome(nome: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('DELETE FROM aluno WHERE nome_aluno = %s RETURNING *', (nome,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
        
    def remover_por_id(id: int): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('DELETE FROM aluno WHERE id_aluno = %s RETURNING *', (id,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()
                
    def remover_por_cpf(cpf: str): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('DELETE FROM aluno WHERE cpf_aluno = %s RETURNING *', (cpf,))
                    
                    return cur.fetchone()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()



    # Função para listar tudo
    def listar_exercicios(): # Funcionando
        connection = None
        
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT * FROM aluno ORDER BY id_aluno')
                    
                    return cur.fetchall()
                    
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close()