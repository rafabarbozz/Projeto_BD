from Controladores.ControladorExercicio import GerenciadorExercicio
from Controladores.ControladorAluno import GerenciadorAluno
from Controladores.ControladorMedidas import GerenciadorMedidas
from Controladores.ControladorTreina import GerenciadorTreina
from menus import menu_tabela, menu_principal
from DataBase.DB_config.config_db import config
from psycopg2 import connect, DatabaseError



opcao = menu_principal() 

if (opcao == 1):
    # Manipulação da tabela Exercicios
    opcao_exercicio = menu_tabela('Exercicio')
        
        
    if (opcao_exercicio == 1): # Criar dados
        
        nome_exercicio = tecnica_avancada = tipo_treino = ''
        qtd_series = qtd_reps = tempo_descanso = 0
        
        nome_exercicio = str(input("Digite o nome do exercicio: "))
        connection = None
        lista_nome = [] # Vai conter todos os nomes dos exercicios da tabela exercicio
        
        # Conectando ao banco de dados
        try:
            params = config()
            with connect(**params) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT nome_exercicio FROM exercicios')
                    for i in cur.fetchall():
                        lista_nome.append(i[0])
                
        except (Exception, DatabaseError) as error:
            print(error)
            
        finally:
            if connection is not None:
                connection.close() 
                
        if nome_exercicio in lista_nome:
            print("Esse exercício já está na tabela Exercicios")
            
        else:            
            qtd_series = int(input("Digite a quantidade de séries: "))
            qtd_reps = int(input("Digite a quantidade de repetições: "))
            tempo_descanso = int(input("Digite o tempo de descanso: "))
            tecnica_avancada = str(input("Digite a técnica avançada: "))
            
            tipo_treino = str(input("Digite o tipo do treino (A, B, C): "))
            while tipo_treino not in "ABC":
                print("Tipo treino inválido. Tente novamente!")
                tipo_treino = str(input("Digite o tipo do treino (A, B, C): "))
        
            GerenciadorExercicio.criar_exercicio(nome_exercicio, qtd_series, qtd_reps, tempo_descanso, tecnica_avancada, tipo_treino)
            
            
    elif (opcao_exercicio == 2): # Remover dados
        atributo = 0
        print("Remover por:\n"
              "1 - Nome do exercicio\n"
              "2 - Id do exercicio")
        
        atributo = int(input("Digite a opção que deseja: "))
        print("\n")
        while (atributo < 1) or (atributo > 2):
            print("Opção inválida. Tente novamente!\n")
            print("Remover por:\n"
              "1 - Nome do exercicio\n"
              "2 - Id do exercicio")
        
            atributo = int(input("Digite a opção que deseja: "))
            print("\n")
        
        if (atributo == 1):
            nome =  ''
            
            nome = str(input("Digite o nome do exercicio que deseja excluir: "))
            print("\n")
            if (GerenciadorExercicio.remover_por_nome(nome) is not None):
                print("Exercício excluido com sucesso!")
            else:
                print("Não foi possível excluir esse exercício, pois ele não está presente na tabela")
        
        elif (atributo == 2):
            id = 0
            
            id = int(input("Digite o id do exercício que deseja excluir: "))
            print("\n")
            if (GerenciadorExercicio.remover_por_id(id) is not None):
                print("Exercício excluido com sucesso!")
            else:
                print("Não foi possível excluir esse exercício, pois ele não está presente na tabela")
        
        
    elif (opcao_exercicio == 3): # Atualizar dados
        atributo = 0
        print("Atualizar:\n"
              "1 - Nome do exercicio\n"
              "2 - Quantidade de séries\n"
              "3 - Quantidade de repetições\n"
              "4 - Tempo de descanso\n"
              "5 - Técnica avançada\n"
              "6 - Tipo do treino")
        
        atributo = int(input("Digite a opção que deseja: "))
        print("\n")
        while (atributo < 1) or (atributo > 6):
            print("Opção inválida. Tente novamente!\n")
            print("Atualizar:\n"
              "1 - Nome do exercicio\n"
              "2 - Quantidade de séries\n"
              "3 - Quantidade de repetições\n"
              "4 - Tempo de descanso\n"
              "5 - Técnica avançada\n"
              "6 - Tipo do treino")
            
            atributo = int(input("Digite a opção que deseja: "))
        
        if (atributo == 1): # Atualizar nome
            nome = ''
            id = 0
            
            id = int(input("Digite o id do exercício que deseja trocar o nome: "))
            nome = str(input("Digite o novo nome do exercício: "))
            
            if (GerenciadorExercicio.alterar_nome_exercicio(id, nome) is not None):
                print("Nome alterado com sucesso!")
            else:
                print("Não foi possível alterar o nome desse exercício, pois ele não se encontra na tabela!")
            
        elif (atributo == 2): # Atualizar qtd_series
            id = 0
            nova_qtd = 0
            
            id = int(input("Digite o id do exercício que deseja trocar a quantidade de séries: "))
            nova_qtd = int(input("Digite a nova quantidade de séries do exercício: "))
            
            if (GerenciadorExercicio.alterar_qtd_series(id, nova_qtd) is not None):
                print("Quantidade de séries alterada com sucesso!")
            else:
                print("Não foi possível alterar a quantidade de séries desse exercício, pois ele não se encontra na tabela!")
                
        elif (atributo == 3): # Atualizar qtd_reps
            id = 0
            nova_qtd = 0
            
            id = int(input("Digite o id do exercício que deseja trocar a quantidade de repetições: "))
            nova_qtd = int(input("Digite a nova quantidade de repetições do exercício: "))
            
            if (GerenciadorExercicio.alterar_qtd_reps(id, nova_qtd) is not None):
                print("Quantidade de repetições alterada com sucesso!")
            else:
                print("Não foi possível alterar a quantidade de repetições desse exercício, pois ele não se encontra na tabela!")
                
        elif (atributo == 4): # Atualizar tempo de descanso
            id = 0
            tempo_descanso = 0
            
            id = int(input("Digite o id do exercício que deseja trocar o tempo de descanso: "))
            tempo_descanso = int(input("Digite o novo tempo de descanso do exercício: "))
         
            if (GerenciadorExercicio.alterar_tempo_descanso(id, tempo_descanso) is not None):
                    print("Tempo de descanso alterado com sucesso!")
            else:
                print("Não foi possível alterar o tempo de descanso desse exercício, pois ele não se encontra na tabela!")
                
        elif (atributo == 5): # Atualizar técnica avançada
            id = 0
            tecnica_avancada = ''
            
            id = int(input("Digite o id do exercício que deseja trocar técnica avançada: "))
            tecnica_avancada = str(input("Digite a nova técnica avançada do exercício: "))
            
            if (GerenciadorExercicio.alterar_tecnica_avancada(id, tecnica_avancada) is not None):
                    print("Técnica avançada alterada com sucesso!")
            else:
                print("Não foi possível alterar a técnica avançada desse exercício, pois ele não se encontra na tabela!")
            
        elif (atributo == 6): # Atualizar o tipo do treino
            id = 0
            tipo_treino = ''
            
            id = int(input("Digite o id do exercício que deseja trocar o tipo do treino: "))
            
            tipo_treino = str(input("Digite o tipo do treino (A, B, C): "))
            while tipo_treino not in "ABC":
                print("Tipo treino inválido. Tente novamente!")
                tipo_treino = str(input("Digite o tipo do treino (A, B, C): "))
            
            if (GerenciadorExercicio.alterar_tipo_treino(id, tipo_treino) is not None):
                    print("Tipo do treino alterado com sucesso!")
            else:
                print("Não foi possível alterar o tipo do treino desse exercício, pois ele não se encontra na tabela!")
        
        
    elif (opcao_exercicio == 4): # Pesquisar dados
        atributo = 0
        print("Procurar por:\n"
              "1 - Id do exercício\n"
              "2 - Nome do exercicio\n"
              "3 - Quantidade de séries\n"
              "4 - Quantidade de repetições\n"
              "5 - Tempo de descanso\n"
              "6 - Técnica avançada\n"
              "7 - Tipo do treino")
        
        atributo = int(input("Digite a opção que deseja: "))
        print("\n")
        while (atributo < 1) or (atributo > 7):
            print("Opção inválida. Tente novamente!\n")
            print("Procurar por:\n"
              "1 - Id do exercício\n"
              "2 - Nome do exercicio\n"
              "3 - Quantidade de séries\n"
              "4 - Quantidade de repetições\n"
              "5 - Tempo de descanso\n"
              "6 - Técnica avançada\n"
              "7 - Tipo do treino")
            
            atributo = int(input("Digite a opção que deseja: "))
            
        if (atributo == 1): # Pesquisar por id
            id = 0
            resultado = []
            
            id = int(input("Digite o id do exercício que deseja procurar: "))
            resultado = GerenciadorExercicio.pesquisar_por_id(id)
            
            if (resultado is not None):
                for i in resultado:
                    print(i, end=' ')
            else:
                print("Não foi possível listar os dados com esse id, pois ele não existe na tabela")
        
        elif (atributo == 2): # Pesquisar por nome
            nome = ''
            resultado = []
            nome = str(input("Digite o nome do exercício que deseja procurar: "))
            resultado = GerenciadorExercicio.pesquisar_por_nome(nome)
            
            if (resultado is not None):
                for i in resultado:
                    print(i, end=' ')
            else:
                print("Não foi possível listar os dados com esse nome, pois ele não existe na tabela")
                
        elif (atributo == 3): # Pesquisar por qtd_series
            qtd_series = 0
            resultado = []
            
            qtd_series = int(input("Digite a quantidade de séries: "))
            resultado = GerenciadorExercicio.pesquisar_por_qtd_series(qtd_series)

            if (len(resultado) != 0):
                for i in resultado:
                    print(i)
            else:
                print("Nenhum exercício encontrado com essa quantidade de séries!")
        
        elif (atributo == 4): # Pesquisar por qtd_reps
            qtd_reps = 0
            resultado = []
            
            qtd_reps = int(input("Digite a quantidade de repetições: "))
            resultado = GerenciadorExercicio.pesquisar_por_qtd_reps(qtd_reps)
            
            if (len(resultado) != 0):
                for i in resultado:
                    print(i)
            else:
                print("Nenhum exercício encontrado com essa quantidade de repetições!")
                
        elif (atributo == 5): # Pesquisar por tempo de descanso
            tempo_descanso = 0
            resultado = []
            
            tempo_descanso = int(input("Digite o tempo de descanso: "))
            resultado = GerenciadorExercicio.pesquisar_por_tempo_descanso(tempo_descanso)
            if (len(resultado) != 0):
                for i in resultado:
                    print(i)
            else:
                print("Nenhum exercício encontrado com esse tempo de descanso!")

        elif (atributo == 6): # Pesquisar por técnica avançada
            tecnica_avancada = ''
            resultado = []
            
            tecnica_avancada = str(input("Digite a técnica avançada: "))
            resultado = GerenciadorExercicio.pesquisar_por_tecnica(tecnica_avancada)
            if (len(resultado) != 0):
                for i in resultado:
                    print(i)
            else:
                print("Nenhum exercício encontrado com essa técnica!")        
            
        elif (atributo == 7): # Pesquisar por tipo de treino
            tipo_treino = ''
            resultado = []
            
            tipo_treino = str(input("Digite o tipo do treino (A, B, C): "))
            while tipo_treino not in "ABC":
                print("Tipo treino inválido. Tente novamente!")
                tipo_treino = str(input("Digite o tipo do treino (A, B, C): "))
                
            resultado = GerenciadorExercicio.pesquisar_por_tipo_treino(tipo_treino)
            if (len(resultado) != 0):
                for i in resultado:
                    print(i)
            else:
                print("Nenhum exercício encontrado com esse tpo de treino!")
    
    
    elif (opcao_exercicio == 5): # Listar toda tabela
        resultado = []
        
        resultado = GerenciadorExercicio.listar_exercicios()
        for i in resultado:
            print(i)