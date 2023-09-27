from dataclasses import dataclass

@dataclass()
class Aluno:
    id_aluno: int
    cpf_aluno: str
    nome_aluno: str
    sexo_aluno: str
    medida_id: int
    
    
    # Métodos para pegar dados
    def get_id_aluno(self):
        return self.id_aluno
    
    def get_cpf_aluno(self):
        return self.cpf_aluno
    
    def get_nome_aluno(self):
        return self.nome_aluno
    
    def get_sexo_aluno(self):
        return self.sexo_aluno
    
    def get_medida_id(self):
        self.medida_id
        
    
    # Métodos para alterar dados
    # id_aluno não poderá ser alterado
    def alterar_cpf_aluno(self, novo_cpf: str):
        self.cpf_aluno = novo_cpf
        
    def alterar_nome_aluno(self, novo_nome: str):
        self.nome_aluno = novo_nome
        
    def alterar_sexo_aluno(self, novo_sexo: str):
        self.sexo_aluno = novo_sexo
        
    def alterar_medida_id(self, nova_medida_id: int):
        self.medida_id = nova_medida_id
    
    
    # Construtor
    def __init__(self, id_aluno: int, cpf: str, nome: str, sexo: str, medida_id: int):
        self.id_aluno = id_aluno 
        self.cpf_aluno = cpf
        self.nome_aluno = nome
        self.sexo_aluno = sexo
        self.medida_id = medida_id

    def __eq__(self, other):
        if type(other) != Aluno:
            return False

        return True if self.id_aluno == other.id_aluno else False
        