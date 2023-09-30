def menu_principal():
    opcao = 0
    print("----------------------------------")
    print("      MENU      ".center(34, ' '))
    print("----------------------------------")
    print("Opções:")
    print("1 - Exercicio\n"
        "2 - Aluno\n"
        "3 - Medida")
    opcao = int(input("Digite o que deseja gerenciar: "))
    print("\n")
    
    while (opcao < 1) or (opcao > 3):
        print("Opção inválida. Tente novamente!\n")
        
        print("----------------------------------")
        print("      MENU      ".center(34, ' '))
        print("----------------------------------")
        print("Opções:")
        print("1 - Exercicio\n"
            "2 - Aluno\n"
            "3 - Medida")
        
        opcao = int(input("Digite o que deseja gerenciar: "))
        print("\n")
        
    return opcao
        
def menu_tabela(tabela: str):
    print("----------------------------------")
    print("      MENU      ".center(34, ' '))
    print("----------------------------------")
    print(f"Opções para {tabela}:")
    print(f"1 - Novo {tabela}\n"
          f"2 - Remover {tabela}\n"
          f"3 - Atualizar {tabela}\n"
          f"4 - Procurar {tabela}\n"
          f"5 - Listar toda tabela {tabela}")
    
    opcao_tabela = int(input("Digite a opção que deseja: "))
    print("\n")
    
    while (opcao_tabela  < 1) or (opcao_tabela  > 6):
        print("Opção inválida. Tente novamente!\n")
        
        print("----------------------------------")
        print("      MENU      ".center(34, ' '))
        print("----------------------------------")
        print("Opções para {tabela}:")
        print(f"1 - Novo {tabela}\n"
              f"2 - Remover {tabela}\n"
              f"3 - Atualizar {tabela}\n"
              f"4 - Procurar {tabela}\n"
              f"5 - Listar toda tabela {tabela}")
        
        opcao_tabela  = int(input("Digite a opção que deseja: "))
        print("\n")
        
    return opcao_tabela 