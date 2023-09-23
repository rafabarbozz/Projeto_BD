CREATE TABLE IF NOT EXISTS exercicios(
    id_exercicio SERIAL PRIMARY KEY,
    nome_exercicio TEXT NOT NULL UNIQUE,
    qtd_series INTEGER NOT NULL,
    qtd_reps INTEGER NOT NULL,
    tempo_descanso INTEGER NOT NULL,
    tecnica_avancada TEXT NOT NULL,
    tipo_treino CHAR(1) NOT NULL CONSTRAINT tipo_check CHECK(tipo_treino i ('A', 'B', 'C'))
); 

CREATE TABLE IF NOT EXISTS medidas(
    id_medida SERIAL PRIMARY KEY,
    coxa_esq NUMERIC(5,2) NOT NULL,
    coxa_dir NUMERIC (5,2) NOT NULL,
    braco_esq NUMERIC(4,2) NOT NULL,
    braco_dir NUMERIC(4,2) NOT NULL,
    altura NUMERIC(3,2) NOT NULL,
    cintura NUMERIC(5,2) NOT NULL,
    peso NUMERIC(5,2) NOT NULL
);  

CREATE TABLE IF NOT EXISTS aluno(
    id_aluno SERIAL PRIMARY KEY,
    nome_aluno TEXT NOT NULL,
    cpf_aluno TEXT NOT NULL UNIQUE,
    sexo_aluno CHAR(1) NOT NULL CONSTRAINT sexo_check CHECK(sexo_aluno in ('M', 'F')),
    medida_id INT NOT NULL UNIQUE,
    CONSTRAINT fk_aluno_medida FOREIGN KEY (medida_id) REFERENCES medidas(id_medida)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS treina(
    id_treino SERIAL PRIMARY KEY,
    aluno_id INT NOT NULL,
    exercicio_id INT NOT NULL,
    CONSTRAINT fk_treino_aluno FOREIGN KEY (aluno_id) REFERENCES (id_aluno) 
        ON DELETE CASCADE
        ON UPDATE CASCADE
);