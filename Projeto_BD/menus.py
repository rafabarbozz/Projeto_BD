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
        
def menu_exercicio():
    print("----------------------------------")
    print("      MENU      ".center(34, ' '))
    print("----------------------------------")
    print("Opções para Exercicio:")
    print("1 - Novo exercicio\n"
          "2 - Remover exercicio\n"
          "3 - Atualizar exercicio\n"
          "4 - Procurar exercicio\n"
          "5 - Listar toda tabela exercicio")
    
    opcao_exercicio = int(input("Digite a opção que deseja: "))
    print("\n")
    
    while (opcao_exercicio < 1) or (opcao_exercicio > 6):
        print("Opção inválida. Tente novamente!\n")
        
        print("----------------------------------")
        print("      MENU      ".center(34, ' '))
        print("----------------------------------")
        print("Opções para Exercicio:")
        print("1 - Novo exercicio\n"
              "2 - Remover exercicio\n"
              "3 - Atualizar exercicio\n"
              "4 - Procurar exercicio por nome\n"
              "5 - Procurar exercicio por id\n"
              "6 - Listar toda tabela exercicio")
        
        opcao_exercicio = int(input("Digite a opção que deseja: "))
        print("\n")
        
    return opcao_exercicio