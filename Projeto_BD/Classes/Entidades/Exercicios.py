from dataclasses import dataclass

@dataclass()
class Exercicios:
    id_exercicio: int
    nome_exercicio: str
    qtd_series: int
    qtd_reps: int
    tempo_descanso: int
    tecnica_avancada: str
    tipo_treino: str
    
    
    # Métodos para pegar dados
    def get_id_exercicio(self):
        return self.id_exercicio
    
    def get_nome_exercicio(self):
        return self.nome_exercicio
    
    def get_qtd_series(self):
        return self.qtd_series
    
    def get_qtd_reps(self):
        return self.qtd_reps
    
    def get_tempo_descanso(self):
        return self.tempo_descanso
    
    def get_tecnica_avancada(self):
        return self.tecnica_avancada
    
    def get_tipo_treino(self):
        return self.tipo_treino


    # Médotos para alteração de dados
    # obs.: id_exercicio será imutável
    def alterar_nome_exercicio(self, novo_nome: str):
        self.nome_exercicio = novo_nome
        
    def alterar_qtd_series(self, nova_qtd: int):
        self.qtd_series = nova_qtd
        
    def alterar_qtd_reps(self, nova_qtd: int):
        self.qtd_reps = nova_qtd
        
    def alterar_tempo(self, novo_tempo: int):
        self.tempo_descanso = novo_tempo
        
    def alterar_tecnica(self, nova_tecnica: str):
        self.tecnica_avancada = nova_tecnica
        
    def alterar_tipo(self, novo_tipo: str):
        self.tipo_treino = novo_tipo
        
        
    # Construtor
    def __init__(self, id_exercicio: int, nome_exercicio: str, qtd_series: int, qtd_reps: int, 
                 tempo_descanso: int, tecnica_avancada: str, tipo_treino: str):
        self.id_exercicio = id_exercicio
        self.nome_exercicio = nome_exercicio
        self.qtd_series = qtd_series
        self.qtd_reps = qtd_reps
        self.tempo_descanso = tempo_descanso
        self.tecnica_avancada = tecnica_avancada
        self.tipo_treino = tipo_treino
        
    def __eq__(self, other):
        if type(other) != Exercicios:
            return False

        return True if self.id_exercicio == other.id_exercicio else False
    