from dataclasses import dataclass

@dataclass()
class Medidas:
    id_medida: int
    coxa_esq: float 
    coxa_dir: float
    braco_esq: float
    braco_dir: float
    altura: float
    cintura: float
    peso: float
    
    # Métodos para adquirir dados:
    def get_id_medida(self):
        return self.id_medida
    
    def get_coxa_esq(self):
        return self.coxa_esq
    
    def get_coxa_dir(self):
        return self.coxa_dir
    
    def get_braco_esq(self):
        return self.braco_esq
    
    def get_braco_dir(self):
        return self.braco_dir
    
    def get_altura(self):
        return self.altura
    
    def get_cintura(self):
        return self.cintura
    
    def get_peso(self):
        return self.peso
    
    
    # Métodos para alterar dados
    # id não poderá ser alterado
    def alterar_coxa_esq(self, nova_coxa: float):
        self.coxa_esq = nova_coxa
        
    def alterar_coxa_dir(self, nova_coxa: float):
        self.coxa_dir = nova_coxa
        
    def alterar_braco_esq(self, novo_braco: float):
        self.braco_esq = novo_braco
        
    def alterar_braco_dir(self, novo_braco: float):
        self.braco_dir = novo_braco
        
    def alterar_altura(self, nova_altura: float):
        self.altura = nova_altura
        
    def alterar_cintura(self, nova_cintura: float):
        self.cintura = nova_cintura
        
    def alterar_peso(self, novo_peso:float):
        self.peso = novo_peso
        
        
    # Construtor
    
    def __init__(self, id: int, numero_integrantes: int, consumo_total: float, pago: bool):
        self.id = id
        self.numero_integrantes = numero_integrantes
        self.consumo_total = consumo_total
        self.pago = pago

    def __eq__(self, other):
        if type(other) != Medidas:
            return False

        return True if self.id == other.__id_pedido else False