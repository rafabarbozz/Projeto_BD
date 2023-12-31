PGDMP     5    3                {         	   projetoBD    15.3    15.3 &    '           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            (           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            )           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            *           1262    24677 	   projetoBD    DATABASE     �   CREATE DATABASE "projetoBD" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "projetoBD";
                postgres    false            �            1259    24793    aluno    TABLE       CREATE TABLE public.aluno (
    id_aluno integer NOT NULL,
    nome_aluno text NOT NULL,
    cpf_aluno text NOT NULL,
    sexo_aluno character(1) NOT NULL,
    medida_id integer NOT NULL,
    CONSTRAINT sexo_check CHECK ((sexo_aluno = ANY (ARRAY['M'::bpchar, 'F'::bpchar])))
);
    DROP TABLE public.aluno;
       public         heap    postgres    false            �            1259    24792    aluno_id_aluno_seq    SEQUENCE     �   CREATE SEQUENCE public.aluno_id_aluno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.aluno_id_aluno_seq;
       public          postgres    false    219            +           0    0    aluno_id_aluno_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.aluno_id_aluno_seq OWNED BY public.aluno.id_aluno;
          public          postgres    false    218            �            1259    24774 
   exercicios    TABLE     ~  CREATE TABLE public.exercicios (
    id_exercicio integer NOT NULL,
    nome_exercicio text NOT NULL,
    qtd_series integer NOT NULL,
    qtd_reps integer NOT NULL,
    tempo_descanso integer NOT NULL,
    tecnica_avancada text NOT NULL,
    tipo_treino character(1) NOT NULL,
    CONSTRAINT tipo_check CHECK ((tipo_treino = ANY (ARRAY['A'::bpchar, 'B'::bpchar, 'C'::bpchar])))
);
    DROP TABLE public.exercicios;
       public         heap    postgres    false            �            1259    24773    exercicios_id_exercicio_seq    SEQUENCE     �   CREATE SEQUENCE public.exercicios_id_exercicio_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.exercicios_id_exercicio_seq;
       public          postgres    false    215            ,           0    0    exercicios_id_exercicio_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.exercicios_id_exercicio_seq OWNED BY public.exercicios.id_exercicio;
          public          postgres    false    214            �            1259    24786    medidas    TABLE     7  CREATE TABLE public.medidas (
    id_medida integer NOT NULL,
    coxa_esq numeric(5,2) NOT NULL,
    coxa_dir numeric(5,2) NOT NULL,
    braco_esq numeric(4,2) NOT NULL,
    braco_dir numeric(4,2) NOT NULL,
    altura numeric(3,2) NOT NULL,
    cintura numeric(5,2) NOT NULL,
    peso numeric(5,2) NOT NULL
);
    DROP TABLE public.medidas;
       public         heap    postgres    false            �            1259    24785    medidas_id_medida_seq    SEQUENCE     �   CREATE SEQUENCE public.medidas_id_medida_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.medidas_id_medida_seq;
       public          postgres    false    217            -           0    0    medidas_id_medida_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.medidas_id_medida_seq OWNED BY public.medidas.id_medida;
          public          postgres    false    216            �            1259    24812    treina    TABLE     �   CREATE TABLE public.treina (
    id_treino integer NOT NULL,
    aluno_id integer NOT NULL,
    exercicio_id integer NOT NULL
);
    DROP TABLE public.treina;
       public         heap    postgres    false            �            1259    24811    treina_id_treino_seq    SEQUENCE     �   CREATE SEQUENCE public.treina_id_treino_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.treina_id_treino_seq;
       public          postgres    false    221            .           0    0    treina_id_treino_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.treina_id_treino_seq OWNED BY public.treina.id_treino;
          public          postgres    false    220            �            1259    24827    treino_aluno    VIEW     �  CREATE VIEW public.treino_aluno AS
 SELECT aluno.nome_aluno AS nome,
    exercicios.nome_exercicio AS exercicio,
    exercicios.qtd_series AS series,
    exercicios.qtd_reps AS reps,
    exercicios.tempo_descanso AS descanso,
    exercicios.tecnica_avancada AS tecnica,
    exercicios.tipo_treino
   FROM ((public.treina
     JOIN public.aluno ON ((treina.aluno_id = aluno.id_aluno)))
     JOIN public.exercicios ON ((treina.exercicio_id = exercicios.id_exercicio)));
    DROP VIEW public.treino_aluno;
       public          postgres    false    215    215    215    215    215    215    215    219    219    221    221            z           2604    24796    aluno id_aluno    DEFAULT     p   ALTER TABLE ONLY public.aluno ALTER COLUMN id_aluno SET DEFAULT nextval('public.aluno_id_aluno_seq'::regclass);
 =   ALTER TABLE public.aluno ALTER COLUMN id_aluno DROP DEFAULT;
       public          postgres    false    219    218    219            x           2604    24777    exercicios id_exercicio    DEFAULT     �   ALTER TABLE ONLY public.exercicios ALTER COLUMN id_exercicio SET DEFAULT nextval('public.exercicios_id_exercicio_seq'::regclass);
 F   ALTER TABLE public.exercicios ALTER COLUMN id_exercicio DROP DEFAULT;
       public          postgres    false    214    215    215            y           2604    24789    medidas id_medida    DEFAULT     v   ALTER TABLE ONLY public.medidas ALTER COLUMN id_medida SET DEFAULT nextval('public.medidas_id_medida_seq'::regclass);
 @   ALTER TABLE public.medidas ALTER COLUMN id_medida DROP DEFAULT;
       public          postgres    false    216    217    217            {           2604    24815    treina id_treino    DEFAULT     t   ALTER TABLE ONLY public.treina ALTER COLUMN id_treino SET DEFAULT nextval('public.treina_id_treino_seq'::regclass);
 ?   ALTER TABLE public.treina ALTER COLUMN id_treino DROP DEFAULT;
       public          postgres    false    221    220    221            "          0    24793    aluno 
   TABLE DATA           W   COPY public.aluno (id_aluno, nome_aluno, cpf_aluno, sexo_aluno, medida_id) FROM stdin;
    public          postgres    false    219   [.                 0    24774 
   exercicios 
   TABLE DATA           �   COPY public.exercicios (id_exercicio, nome_exercicio, qtd_series, qtd_reps, tempo_descanso, tecnica_avancada, tipo_treino) FROM stdin;
    public          postgres    false    215   �.                  0    24786    medidas 
   TABLE DATA           m   COPY public.medidas (id_medida, coxa_esq, coxa_dir, braco_esq, braco_dir, altura, cintura, peso) FROM stdin;
    public          postgres    false    217   10       $          0    24812    treina 
   TABLE DATA           C   COPY public.treina (id_treino, aluno_id, exercicio_id) FROM stdin;
    public          postgres    false    221   �0       /           0    0    aluno_id_aluno_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.aluno_id_aluno_seq', 3, true);
          public          postgres    false    218            0           0    0    exercicios_id_exercicio_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.exercicios_id_exercicio_seq', 17, true);
          public          postgres    false    214            1           0    0    medidas_id_medida_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.medidas_id_medida_seq', 3, true);
          public          postgres    false    216            2           0    0    treina_id_treino_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.treina_id_treino_seq', 28, true);
          public          postgres    false    220            �           2606    24803    aluno aluno_cpf_aluno_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT aluno_cpf_aluno_key UNIQUE (cpf_aluno);
 C   ALTER TABLE ONLY public.aluno DROP CONSTRAINT aluno_cpf_aluno_key;
       public            postgres    false    219            �           2606    24805    aluno aluno_medida_id_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT aluno_medida_id_key UNIQUE (medida_id);
 C   ALTER TABLE ONLY public.aluno DROP CONSTRAINT aluno_medida_id_key;
       public            postgres    false    219            �           2606    24801    aluno aluno_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT aluno_pkey PRIMARY KEY (id_aluno);
 :   ALTER TABLE ONLY public.aluno DROP CONSTRAINT aluno_pkey;
       public            postgres    false    219                       2606    24784 (   exercicios exercicios_nome_exercicio_key 
   CONSTRAINT     m   ALTER TABLE ONLY public.exercicios
    ADD CONSTRAINT exercicios_nome_exercicio_key UNIQUE (nome_exercicio);
 R   ALTER TABLE ONLY public.exercicios DROP CONSTRAINT exercicios_nome_exercicio_key;
       public            postgres    false    215            �           2606    24782    exercicios exercicios_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.exercicios
    ADD CONSTRAINT exercicios_pkey PRIMARY KEY (id_exercicio);
 D   ALTER TABLE ONLY public.exercicios DROP CONSTRAINT exercicios_pkey;
       public            postgres    false    215            �           2606    24791    medidas medidas_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.medidas
    ADD CONSTRAINT medidas_pkey PRIMARY KEY (id_medida);
 >   ALTER TABLE ONLY public.medidas DROP CONSTRAINT medidas_pkey;
       public            postgres    false    217            �           2606    24817    treina treina_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.treina
    ADD CONSTRAINT treina_pkey PRIMARY KEY (id_treino);
 <   ALTER TABLE ONLY public.treina DROP CONSTRAINT treina_pkey;
       public            postgres    false    221            �           2606    24806    aluno fk_aluno_medida    FK CONSTRAINT     �   ALTER TABLE ONLY public.aluno
    ADD CONSTRAINT fk_aluno_medida FOREIGN KEY (medida_id) REFERENCES public.medidas(id_medida) ON UPDATE CASCADE ON DELETE SET NULL;
 ?   ALTER TABLE ONLY public.aluno DROP CONSTRAINT fk_aluno_medida;
       public          postgres    false    217    219    3203            �           2606    24818    treina fk_treino_aluno    FK CONSTRAINT     �   ALTER TABLE ONLY public.treina
    ADD CONSTRAINT fk_treino_aluno FOREIGN KEY (aluno_id) REFERENCES public.aluno(id_aluno) ON UPDATE CASCADE ON DELETE CASCADE;
 @   ALTER TABLE ONLY public.treina DROP CONSTRAINT fk_treino_aluno;
       public          postgres    false    219    221    3209            "   J   x�3�JLKL�QpJ,JʯJ�4 N_NC.#N��Ë��2�K�9� (l�e��X��ZZ�i@!c�=... �H         l  x�}�IN�@D�ߧ�er�e����Î͗����v��@�,�[_�ߊe"+��W�U��@Xle��c)�b���6���T}k�,+$L�n.)�"҉��dzd�@��+�1	�PQ��z��"�+���UNƺwap��g���$���[е���m+��)��X�X��,�w��L)��Ԫ�	G�bQ}�\�P�z�!,)��_��~�������k*�>TSֽq��!(vV83:͹Js��6��A����z�*gH�:�PL�����'�/�Z�@�����&�繄{�r��9��t�0Yc����sY��>X�W��5��ώ���4�����B�:�,|i-2���0�j���pj�v�8�0�h          M   x�5�� 1�P��p���ױ��|F�56
���`(��Sٙ�7y<u���V��I���;��U�B4��0��m�      $   N   x�̹�0��W�G��ǽ��:&�����ӝ�[,w��M�P�5�"/"R��
U�g����B��趇�~��u     