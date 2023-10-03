from Controladores.ControladorExercicio import GerenciadorExercicio
from Controladores.ControladorAluno import GerenciadorAluno
from Controladores.ControladorMedidas import GerenciadorMedidas
from Controladores.ControladorTreina import GerenciadorTreina
from menus import menu_tabela, menu_principal
from DataBase.DB_config.config_db import config
from psycopg2 import connect, DatabaseError



continuaroperacao = 1

while (continuaroperacao == 1):
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
                
                print("REMOÇÃO POR NOME")
                nome = str(input("Digite o nome do exercicio que deseja excluir: "))
                print("\n")
                if (GerenciadorExercicio.remover_por_nome(nome) is not None):
                    print("Exercício excluido com sucesso!")
                else:
                    print("Não foi possível excluir esse exercício, pois ele não está presente na tabela")
            
            elif (atributo == 2):
                id = 0
                
                print("REMOÇÃO POR ID")
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
                print("\n")
            
            if (atributo == 1): # Atualizando nome
                nome = ''
                id = 0
                
                print("ATUAZALIZAR NOME")
                id = int(input("Digite o id do exercício que deseja alterar o nome: "))
                nome = str(input("Digite o novo nome do exercício: "))
                
                if (GerenciadorExercicio.alterar_nome_exercicio(id, nome) is not None):
                    print("Nome alterado com sucesso!")
                else:
                    print("Não foi possível alterar o nome desse exercício, pois ele não se encontra na tabela!")
                
            elif (atributo == 2): # Atualizando qtd_series
                id = 0
                nova_qtd = 0
                
                print("ATUALIZAR QUANTIDADE DE SÉRIES")
                id = int(input("Digite o id do exercício que deseja alterar a quantidade de séries: "))
                nova_qtd = int(input("Digite a nova quantidade de séries do exercício: "))
                
                if (GerenciadorExercicio.alterar_qtd_series(id, nova_qtd) is not None):
                    print("Quantidade de séries alterada com sucesso!")
                else:
                    print("Não foi possível alterar a quantidade de séries desse exercício, pois ele não se encontra na tabela!")
                    
            elif (atributo == 3): # Atualizando qtd_reps
                id = 0
                nova_qtd = 0
                
                print("ATUALIZAR QUANTIDADE DE REPETIÇÕES")
                id = int(input("Digite o id do exercício que deseja alterar a quantidade de repetições: "))
                nova_qtd = int(input("Digite a nova quantidade de repetições do exercício: "))
                
                if (GerenciadorExercicio.alterar_qtd_reps(id, nova_qtd) is not None):
                    print("Quantidade de repetições alterada com sucesso!")
                else:
                    print("Não foi possível alterar a quantidade de repetições desse exercício, pois ele não se encontra na tabela!")
                    
            elif (atributo == 4): # Atualizando tempo de descanso
                id = 0
                tempo_descanso = 0
                
                print("ATUALIZAR TEMPO DE DESCANSO")
                id = int(input("Digite o id do exercício que deseja alterar o tempo de descanso: "))
                tempo_descanso = int(input("Digite o novo tempo de descanso do exercício: "))
            
                if (GerenciadorExercicio.alterar_tempo_descanso(id, tempo_descanso) is not None):
                        print("Tempo de descanso alterado com sucesso!")
                else:
                    print("Não foi possível alterar o tempo de descanso desse exercício, pois ele não se encontra na tabela!")
                    
            elif (atributo == 5): # Atualizando técnica avançada
                id = 0
                tecnica_avancada = ''
                
                print("ATUALIZAR TÉCNICA AVANÇADA")
                id = int(input("Digite o id do exercício que deseja alterar técnica avançada: "))
                tecnica_avancada = str(input("Digite a nova técnica avançada do exercício: "))
                
                if (GerenciadorExercicio.alterar_tecnica_avancada(id, tecnica_avancada) is not None):
                        print("Técnica avançada alterada com sucesso!")
                else:
                    print("Não foi possível alterar a técnica avançada desse exercício, pois ele não se encontra na tabela!")
                
            elif (atributo == 6): # Atualizando o tipo do treino
                id = 0
                tipo_treino = ''
                
                print("ATUALIZAR TIPO DO TREINO")
                id = int(input("Digite o id do exercício que deseja alterar o tipo do treino: "))
                
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
                print("\n")
                
            if (atributo == 1): # Pesquisar por id
                id = 0
                resultado = []
                
                print("PESQUISAR POR ID")
                id = int(input("Digite o id do exercício que deseja procurar: "))
                resultado = GerenciadorExercicio.pesquisar_por_id(id)
                
                if (resultado is not None):
                    for i in resultado:
                        print(i, end=' ')
                else:
                    print("Não foi possível listar o exercício com esse id, pois ele não existe na tabela")
            
            elif (atributo == 2): # Pesquisar por nome
                nome = ''
                resultado = []
                
                print("PESQUISAR POR NOME")
                nome = str(input("Digite o nome do exercício que deseja procurar: "))
                resultado = GerenciadorExercicio.pesquisar_por_nome(nome)
                
                if (resultado is not None):
                    for i in resultado:
                        print(i, end=' ')
                else:
                    print("Não foi possível listar o exercício com esse nome, pois ele não existe na tabela")
                    
            elif (atributo == 3): # Pesquisar por qtd_series
                qtd_series = 0
                resultado = []
                
                print("PESQUISAR POR QUANTIDADE DE SÉRIES")
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
                
                print("PESQUISAR POR QUANTIDADE DE REPETIÇÕES")
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
                
                print("PESQUISAR POR TEMPO DE DESCANSO")
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
                
                print("PESQUISAR POR TÉCNICA AVANÇADA")
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
                
                print("PESQUISAR POR TIPO DO TREINO")
                tipo_treino = str(input("Digite o tipo do treino (A, B, C): "))
                while tipo_treino not in "ABC":
                    print("Tipo treino inválido. Tente novamente!")
                    tipo_treino = str(input("Digite o tipo do treino (A, B, C): "))
                    
                resultado = GerenciadorExercicio.pesquisar_por_tipo_treino(tipo_treino)
                if (len(resultado) != 0):
                    for i in resultado:
                        print(i)
                else:
                    print("Nenhum exercício encontrado com esse tipo de treino!")
        
        
        elif (opcao_exercicio == 5): # Listar toda tabela
            resultado = []
            
            resultado = GerenciadorExercicio.listar_exercicios()
            for i in resultado:
                print(i)
                
                
        elif (opcao_exercicio == 6):
            print("Operação cancelada!")
            pass
                

    elif (opcao == 2):
        # Manipulação da tabela Medidas
        opcao_medida = menu_tabela('Medidas')
        
        
        if (opcao_medida == 1): # Criar dados
            coxa_esq = coxa_dir = braco_esq = braco_dir = altura = cintura = peso = 0
                
            coxa_esq = float(input("Digite a medida da coxa esquerda: "))
            coxa_dir = float(input("Digite a medida da coxa direita: "))
            braco_esq = float(input("Digite a medida do braço esquerdo: "))
            braco_dir = float(input("Digite a medida do braço direito: "))
            altura = float(input("Digite a altura: "))
            cintura = float(input("Digite a cintura: "))
            peso = float(input("Digite o peso: "))
            
            GerenciadorMedidas.criar_medida(coxa_esq, coxa_dir, braco_esq, braco_dir, altura, cintura, peso)
            
        
        elif (opcao_medida == 2): # Remover dados
            id = 0
            
            print("REMOVER POR ID")
            id = int(input("Digite o id da medida que deseja excluir: "))
            
            if (GerenciadorMedidas.remover_por_id(id) is not None):
                print("Medida removida com sucesso!")
            else:
                print("Não foi possível remover essa medida, pois ela não se encontra na tabela!")
                
        elif (opcao_medida == 3): # Atualizar dados
            atributo = 0
            
            print("Atualizar:\n"
                "1 - Coxa esquerda\n"
                "2 - Coxa direita\n"
                "3 - Braço esquerdo\n"
                "4 - Braço direito\n"
                "5 - Altura\n"
                "6 - Cintura\n"
                "7 - Peso\n")
            
            atributo = int(input("Digite a opção que deseja: "))
            print("\n")
            while (atributo < 1) or (atributo > 7):
                print("Opção inválida. Tente novamente!\n")
                print("Atualizar:\n"
                "1 - Coxa esquerda\n"
                "2 - Coxa direita\n"
                "3 - Braço esquerdo\n"
                "4 - Braço direito\n"
                "5 - Altura\n"
                "6 - Cintura\n"
                "7 - Peso\n")
                
                atributo = int(input("Digite a opção que deseja: "))
                print("\n")
            
            if (atributo == 1): # Atualizando coxa esquerda
                id = 0 
                coxa_esq = 0
                
                print("ATUALIZAR COXA ESQUERDA")
                id = int(input("Digite o id que deseja alterar a medida da coxa esquerda: "))
                coxa_esq = float(input("Digite a nova medida da coxa esquerda: "))
                
                if (GerenciadorMedidas.alterar_coxa_esq(id, coxa_esq) is not None):
                    print("Coxa esquerda alterada com sucesso!")
                else:
                    print("Não foi possível alterar a medida da coxa esquerda, pois esse id não se encontra na tabela!")
            
            elif (atributo == 2): # Atualizando coxa direita
                id = 0
                coxa_dir = 0
                
                print("ATUALIZAR COXA DIREITA")
                id = int(input("Digite o id que deseja alterar a medida da coxa direita: "))
                coxa_dir = float(input("Digite a nova medida da coxa direita: "))
                
                if (GerenciadorMedidas.alterar_coxa_dir(id, coxa_dir) is not None):
                    print("Coxa direita alterado com sucesso!")
                else:
                    print("Não foi possível alterar a medida da coxa direita, pois esse id não se encontra na tabela!")

            elif (atributo == 3): # Atualizando braço esquerdo
                id = 0
                braco_esq = 0
                
                print("ATUALIZAR BRAÇO ESQUERDO")
                id = int(input("Digite o id que deseja alterar a medida do braço esquerdo: "))
                braco_esq = float(input("Digite a nova medida do braço esquerdo: "))
                
                if (GerenciadorMedidas.alterar_braco_esq(id, braco_esq) is not None):
                    print("Braço esquerdo alterado com sucesso!")
                else:
                    print("Não foi possível alterar a medida do braço esquerdo, pois esse id não se encontra na tabela!")
                    
            elif (atributo == 4): # Atualizando braço direito
                id = 0
                braco_dir = 0
                
                print("ATUALIZAR BRAÇO DIREITO")
                id = int(input("Digite o id que deseja alterar a medida do braço direito: "))
                braco_dir = float(input("Digite a nova medida do braço direito: "))
                
                if (GerenciadorMedidas.alterar_braco_dir(id, braco_dir) is not None):
                    print("Braço direito alterado com sucesso!")
                else:
                    print("Não foi possível alterar a medida do braço direito, pois esse id não se encontra na tabela!")
                    
            elif (atributo == 5): # Atualizando altura
                id = 0
                altura = 0
                
                print("ATUALIZAR ALTURA")
                id = int(input("Digite o id que deseja alterar a altura: "))
                altura = float(input("Digite a nova altura: "))
                
                if (GerenciadorMedidas.alterar_altura(id, altura) is not None):
                    print("Altura alterada com sucesso!")
                else:
                    print("Não foi possível alterar a altura, pois esse id não se encontra na tabela!")
                    
            elif (atributo == 6): # Atualizando cintura
                id = 0
                cintura = 0
                
                print("ATUALIZAR CINTURA")
                id = int(input("Digite o id que deseja alterar a cintura: "))
                cintura = float(input("Digite a nova cintura: "))
                
                if (GerenciadorMedidas.alterar_cintura(id, cintura) is not None):
                    print("Altura alterada com sucesso!")
                else:
                    print("Não foi possível alterar a cintura, pois esse id não se encontra na tabela!")
                    
            elif (atributo == 7): # Atualizando peso
                id = 0
                peso = 0
                
                print("ATUALIZAR PESO")
                id = int(input("Digite o id que deseja alterar o peso: "))
                peso = float(input("Digite a novo peso: "))
                
                if (GerenciadorMedidas.alterar_peso(id, peso) is not None):
                    print("Peso alterado com sucesso!")
                else:
                    print("Não foi possível alterar o peso, pois esse id não se encontra na tabela!")
                    
        elif (opcao_medida == 4): # Pesquisar dados
            atributo = 0
            
            print("Procurar por:\n"
                "1 - Id da medida\n"
                "2 - Coxa esquerda\n"
                "3 - Coxa direita\n"
                "4 - Braço esquerdo\n"
                "5 - Braço direito\n"
                "6 - Altura\n"
                "7 - Cintura\n"
                "8 - Peso")
            
            atributo = int(input("Digite a opção que deseja: "))
            print("\n")
            while (atributo < 1) or (atributo > 8):
                print("Opção inválida. Tente novamente!\n")
                print("Procurar por:\n"
                "1 - Id da medida\n"
                "2 - Coxa esquerda\n"
                "3 - Coxa direita\n"
                "4 - Braço esquerdo\n"
                "5 - Braço direito\n"
                "6 - Altura\n"
                "7 - Cintura\n"
                "8 - Peso")
                
                atributo = int(input("Digite a opção que deseja: "))
                print("\n")
                
            if (atributo == 1): # Pesquisar por id
                id = 0
                resultado = []
                
                print("PESQUISAR POR ID")
                id = int(input("Digite o id da medida que deseja procurar: "))
                resultado = GerenciadorMedidas.pesquisar_por_id(id)
                
                if (resultado is not None):
                    for i in resultado:
                        print(i, end=' ')
                else:
                    print("Não foi possível listar as medidas com esse id, pois ele não existe na tabela")
            
            elif (atributo == 2): # Pesquisar por coxa esquerda
                coxa_esq = 0
                resultado = []
                
                print("PESQUISAR COXA ESQUERDA")
                coxa_esq = float(input("Digite a medida da coxa esquerda que deseja procurar: "))
                resultado = GerenciadorMedidas.pesquisar_por_coxa_esq(coxa_esq)
                if (len(resultado) != 0):
                    for i in resultado:
                        print(i)
                else:
                    print("Nenhuma medida encontrada com essa coxa esquerda!")
            
            elif (atributo == 3): # Pesquisar por coxa direita
                coxa_dir = 0
                resultado = []
                
                print("PESQUISAR POR COXA DIREITA")
                coxa_dir = float(input("Digite a medida da coxa direita que deseja procurar: "))
                resultado = GerenciadorMedidas.pesquisar_por_coxa_dir(coxa_dir)
                if (len(resultado) != 0):
                    for i in resultado:
                        print(i)
                else:
                    print("Nenhuma medida encontrada com essa coxa direita!")
                    
            elif (atributo == 4): # Pesquisar por braço esquerdo
                braco_esq = 0
                resultado = []
                
                print("PESQUISAR POR BRAÇO ESQUERDO")
                braco_esq = float(input("Digite a medida do braço esquerdo que deseja procurar: "))
                resultado = GerenciadorMedidas.pesquisar_por_braco_esq(braco_esq)
                if (len(resultado) != 0):
                    for i in resultado:
                        print(i)
                else:
                    print("Nenhuma medida encontrada com esse braço esquerdo!")
                    
            elif (atributo == 5): # Pesquisar por braço direito
                braco_dir = 0
                resultado = []
                
                print("PESQUISAR POR BRAÇO DIREITO")
                braco_dir = float(input("Digite a medida do braço direito que deseja procurar: "))
                resultado = GerenciadorMedidas.pesquisar_por_braco_dir(braco_dir)
                if (len(resultado) != 0):
                    for i in resultado:
                        print(i)
                else:
                    print("Nenhuma medida encontrada com esse braço direito!")
            
            elif (atributo == 6): # Pesquisar por altura
                altura = 0
                resultado = []
                
                print("PESQUISAR POR ALTURA")
                altura = float(input("Digite a medida da altura que deseja procurar: "))
                resultado = GerenciadorMedidas.pesquisar_por_altura(altura)
                if (len(resultado) != 0):
                    for i in resultado:
                        print(i)
                else:
                    print("Nenhuma medida encontrada com essa altura!")
                    
            elif (atributo == 7): # Pesquisar por cintura
                cintura = 0
                resultado = []
                
                print("PESQUISAR POR CINTURA")
                cintura = float(input("Digite a medida da cintura que deseja procurar: "))
                resultado = GerenciadorMedidas.pesquisar_por_cintura(cintura)
                if (len(resultado) != 0):
                    for i in resultado:
                        print(i)
                else:
                    print("Nenhuma medida encontrada com essa cintura!")
                    
            elif (atributo == 8): # Pesquisar por peso
                peso = 0
                resultado = []
                
                print("PESQUISAR POR PESO")
                peso = float(input("Digite a medida do peso que deseja procurar: "))
                resultado = GerenciadorMedidas.pesquisar_por_peso(peso)
                if (len(resultado) != 0):
                    for i in resultado:
                        print(i)
                else:
                    print("Nenhuma medida encontrada com esse peso!")
        
        elif (opcao_medida == 5): # Listar toda tabela
            resultado = [] 
            
            resultado = GerenciadorMedidas.listar_medidas()
            for i in resultado:
                print(i)
                
        
        elif (opcao_medida == 6):
            print("Operação cancelada!")
            pass
        
        
    elif (opcao == 3):
        # Manipulação da tabela aluno
        opcao_aluno = menu_tabela('Aluno')
        
        
        if (opcao_aluno == 1): # Criar dados
            medida_id = 0
            cpf_aluno = nome_aluno = sexo_aluno = ''
            
            nome_aluno = str(input("Digite o nome do aluno: "))
            
            connection = None
            lista_cpf = [] # Vai conter todos os cpf da tabela aluno
            lista_medida_id = [] # Vai conter todos as medida_id da tabela aluno
            # Conectando ao banco de dados
            try:
                params = config()
                with connect(**params) as conn:
                    with conn.cursor() as cur:
                        cur.execute('SELECT cpf_aluno, medida_id FROM aluno')
                        for i in cur.fetchall():
                            lista_cpf.append(i[0])
                            lista_medida_id.append(i[1])
                    
            except (Exception, DatabaseError) as error:
                print(error)
                
            finally:
                if connection is not None:
                    connection.close() 
                    
            cpf_aluno = str(input("Digite o cpf do aluno: "))
            if (cpf_aluno in lista_cpf):
                print("Esse cpf já está na tabela aluno!")
            else:
                sexo_aluno = str(input("Digite o sexo do aluno(M ou F): "))
                while (sexo_aluno not in 'MF'):
                    print("Sexo inválido. Tente novamente!\n")
                    sexo_aluno = str(input("Digite o sexo do aluno(M ou F): "))
                
                medida_id = int(input("Digite o id das medidas associada a esse aluno: "))
                if (medida_id in lista_medida_id):
                    print("Esse id já está associado a outro aluno!")
                else:
                    if (GerenciadorAluno.criar_aluno(nome_aluno, cpf_aluno, sexo_aluno, medida_id) is not None):
                        print("Aluno criado com sucesso!")
                    else:
                        print("Não foi possível criar esse aluno!")
        
        
        elif (opcao_aluno == 2): # Remover dados
            atributo = 0
            
            print("Remover por:\n"
                "1 - Id aluno\n"
                "2 - Nome do aluno\n"
                "3 - CPF do aluno")
            
            atributo = int(input("Digite a opção que deseja: "))
            print("\n")
            while (atributo < 1) or (atributo > 3):
                print("Opção inválida. Tente novamente!\n")
                print("Remover por:\n"
                    "1 - Id aluno\n"
                    "2 - Nome do aluno\n"
                    "3 - CPF do aluno")
            
                atributo = int(input("Digite a opção que deseja: "))
                print("\n")
                
            if (atributo == 1): # Remover por id
                id = 0
            
                print("REMOVER POR ID")
                id = int(input("Digite o id do aluno que deseja excluir: "))
                
                if (GerenciadorAluno.remover_por_id(id) is not None):
                    print("Aluno removido com sucesso!")
                else:
                    print("Não foi possível remover esse aluno, pois ele não se encontra na tabela!")
            
            elif (atributo == 2): # Remover por nome
                nome = ''
                
                print("REMOVER POR NOME")
                nome = str(input("Digite o nome do aluno que deseja remover: "))
                
                if (GerenciadorAluno.remover_por_nome(nome) is not None):
                    print("Aluno removido com sucesso!")
                else:
                    print("Não foi possível remover esse aluno, pois ele não se encontra na tabela!")
            
            elif (atributo == 3): # Remover por cpf
                cpf = ''
                
                print("REMOVER POR CPF")
                cpf = str(input("Digite o cpf do aluno que deseja remover: "))
                
                if (GerenciadorAluno.remover_por_cpf(cpf) is not None):
                    print("Aluno removido com sucesso!")
                else:
                    print("Não foi possível remover esse aluno, pois ele não se encontra na tabela!")
            
                    
        elif (opcao_aluno == 3): # Atualizar dados
            atributo = 0
            
            print("Procurar por:\n"
                "1 - Nome do aluno\n"
                "2 - CPF do aluno\n"
                "3 - Sexo do aluno")
            
            atributo = int(input("Digite a opção que deseja: "))
            print("\n")
            while (atributo < 1) or (atributo > 3):
                print("Opção inválida. Tente novamente!\n")
                print("Procurar por:\n"
                "1 - Nome do aluno\n"
                "2 - CPF do aluno\n"
                "3 - Sexo do aluno")
                
                atributo = int(input("Digite a opção que deseja: "))     
                print("\n") 
        
            if (atributo == 1): # Atualizando nome 
                id = 0
                nome = ''
                
                print("ATUALIZAR NOME")
                id = int(input("Digite o id do aluno que deseja alterar a nome: "))
                nome = str(input("Digite o novo nome: "))
                
                if (GerenciadorAluno.alterar_nome(id, nome) is not None):
                    print("Nome alterado com sucesso!")
                else:
                    print("Não foi possível alterar o nome do aluno, pois esse id não se encontra na tabela!")
            
            elif (atributo == 2): # Atualizando cpf
                id = 0
                cpf = ''
                
                print("ATUALIZAR CPF")
                id = int(input("Digite o id do aluno que deseja alterar o CPF: "))
                cpf = str(input("Digite o novo cpf: "))
                
                if (GerenciadorAluno.alterar_cpf(id, cpf) is not None):
                    print("CPF alterado com sucesso!")
                else:
                    print("Não foi possível alterar o CPF do aluno, pois esse id não se encontra na tabela!")
            
            elif (atributo == 3): # Atualizando sexo
                id = 0
                sexo = ''
                
                print("ATUALIZAR SEXO")
                id = int(input("Digite o id do aluno que deseja alterar o sexo: "))
                sexo = str(input("Digite o novo sexo: "))
                
                if (GerenciadorAluno.alterar_sexo(id, sexo) is not None):
                    print("Sexo alterado com sucesso!")
                else:
                    print("Não foi possível alterar o sexo do aluno, pois esse id não se encontra na tabela!")
        
        
        elif (opcao_aluno == 4): # Pesquisar dados
            atributo = 0
            
            print("Procurar por:\n"
                "1 - Id do aluno\n"
                "2 - Nome do aluno\n"
                "3 - CPF do aluno\n"
                "4 - Sexo do aluno")
            
            atributo = int(input("Digite a opção que deseja: "))
            print("\n")
            while (atributo < 1) or (atributo > 4):
                print("Opção inválida. Tente novamente!\n")
                print("Procurar por:\n"
                "1 - Id do aluno\n"
                "2 - Nome do aluno\n"
                "3 - CPF do aluno\n"
                "4 - Sexo do aluno")
                
                atributo = int(input("Digite a opção que deseja: "))
                print("\n")
                
            if (atributo == 1): # Pesquisar por id
                id = 0
                resultado = []
                
                print("PESQUISAR POR ID")
                id = int(input("Digite o id do aluno que deseja procurar: "))
                resultado = GerenciadorAluno.pesquisar_por_id(id)
                
                if (resultado is not None):
                    for i in resultado:
                        print(i, end=' ')
                else:
                    print("Não foi possível listar o aluno com esse id, pois ele não existe na tabela")
            
            elif (atributo == 2): # Pesquisar por nome
                nome = ''
                resultado = []
                
                print("PESQUISAR POR NOME")
                nome = str(input("Digite o nome do aluno que deseja procurar: "))
                resultado = GerenciadorAluno.pesquisar_por_nome(nome)
                
                if (resultado is not None):
                    for i in resultado:
                        print(i, end=' ')
                else:
                    print("Não foi possível listar o aluno com esse nome, pois ele não existe na tabela")
            
            elif (atributo == 3): # Pesquisar por cpf
                cpf = ''
                resultado = []
                
                print("PESQUISAR POR CPF")
                cpf = str(input("Digite o CPF do aluno que deseja procurar: "))
                resultado = GerenciadorAluno.pesquisar_por_cpf(cpf)
                
                if (resultado is not None):
                    for i in resultado:
                        print(i, end=' ')
                else:
                    print("Não foi possível listar o aluno com esse CPF, pois ele não existe na tabela")
                    
            elif (atributo == 4): # Pesquisar por sexo
                sexo = ''
                resultado = []
                
                print("PESQUISAR POR SEXO")
                sexo = str(input("Digite o sexo do aluno que deseja procurar: "))
                resultado = GerenciadorAluno.pesquisar_por_sexo(sexo)
                
                if (len(resultado) != 0):
                    for i in resultado:
                        print(i)
                else:
                    print("Não foi possível listar os dados do alunos com esse sexo, pois ele não existe na tabela")
        
        
        elif (opcao_aluno == 5): # Listar toda tabela
            resultado = [] 
            
            resultado = GerenciadorAluno.listar_alunos()
            for i in resultado:
                print(i)
                
                
        elif (opcao_aluno == 6):
            print("Operação cancelada!")
            pass
        
    
    elif (opcao == 4):
        print("Programa finalizado!")
        break
    
    
    print("\n")
    continuaroperacao = int(input("Deseja continuar as operações nas tabelas(1 para sim e 0 para não): "))
    if (continuaroperacao == 0):
        print("\nPrograma finalizado!")
