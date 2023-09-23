from dataclasses import dataclass

@dataclass()
class Treina:
    id_treino: int
    exercicio_id: int
    aluno_id: int
    
    # Métodos para adquirir dados
    def get_id_treino(self):
        return self.id_treino

    def get_exercicio_id(self):
        return self.exercicio_id
    
    def get_aluno_id(self):
        return self.aluno_id
    
    
    # Métodos para alterar dados
    # id_treino não poderá ser alterado
    def alterar_exercicio_id(self, novo_exercicio_id: int):
        self.exercicio_id = novo_exercicio_id
        
    def alterar_aluno_id(self, novo_aluno_id: int):
        self.aluno_id - novo_aluno_id
        
    # Construtor
    def __eq__(self, other):
        if type(other) != Treina:
            return False
        return True if self.id_pedido == other.id_pedido else False

    def __int__(self, id_pedido: int, id_mesa: int, id_prato: int, quantidade: int, entregue: bool, data: date):
        self.id_pedido = id_pedido
        self.id_mesa = id_mesa
        self.id_prato = id_prato
        self.quantidade = quantidade
        self.entregue = entregue
        self.data = data