from Arquivo import Arquivo
from Aluno import Aluno
import random


class GerarArquivo(Arquivo):

    __cursos = ['Astronomia', 'Bioengenharia', 'Biofísica', 'Ciência da Computação', 'Ciências Biomoleculares',
              'Ciências Matemáticas da Terra', 'Ciências Naturais', 'Educação do Campo', 'Engenharia aeroespacial',
              'Engenharia Agrícola', 'Engenharia de Alimentos', 'Engenharia Ambiental', 'Engenharia biomédica',
              'Engenharia Cartográfica', 'Engenharia Civil', 'Engenharia de Computação',
              'Engenharia de controle e automação', 'Engenharia Elétrica', 'Engenharia Física', 'Engenharia Florestal',
              'Engenharia geológica', 'Engenharia de Materiais', 'Engenharia Mecânica', 'Engenharia Mecatrônica',
              'Engenharia de Telecomunicações', 'Estatística', 'Farmácia', 'Física', 'Geologia', 'Matemática',
              'Química ambiental', 'Química industrial', 'Sistemas de Informação']

    __nomes = ['Sophia', 'Isabelly', 'Ana Laura', 'Ana Sophia', 'Alice', 'Sarah', 'Elisa', 'Bárbara', 'Julia',
             'Ana Julia', 'Emilly', 'Mariah', 'Isabella', 'Letícia', 'Eduarda', 'Antônia', 'Manuela', 'Ana Luiza', 'Pietra',
             'Natália', 'Laura', 'Melissa', 'Milena', 'Clarice', 'Luiza', 'Marina', 'Laís', 'Ísis', 'Valentina', 'Clara', 'Maria',
             'Julia', 'Ana Carolina', 'Giovanna', 'Cecília', 'Maria', 'Maya', 'Maria Eduarda', 'Esther', 'Eloá',
             'Alana', 'Enrico', 'João Pedro', 'Enzo', 'Luiz Felipe', 'Henry', 'Daniel', 'Bruno', 'Igor', 'Vitor', 'Gabriel',
             'Vitor Emanuel', 'Carlos', 'Eduardo', 'João Paulo', 'Leonardo', 'João Gabriel', 'Bento', 'Lucas',
             'Gabriel', 'Henrique', 'Ian', 'Raul', 'Luiz Fernando', 'Theo', 'Davi', 'Luiz', 'André Luiz', 'Otávio',
             'Murilo', 'Rodrigo', 'Levi', 'Renan', 'Eduardo', 'Otávio', 'Noah', 'Kevin', 'Helena', 'Emanuelly',
             'Olívia', 'Mirella', 'Beatriz', 'Rebeca', 'Maitê', 'Maria Vitória', 'Maria Luiza', 'Ana Beatriz', 'Stella',
             'Juliana', 'Lara', 'Lavínia', 'Maria Alice', 'Paola', 'Mariana Vitória', 'Sophie Marcela', 'Nicole', 'Bianca',
             'Bruna', 'Débora', 'Rafaela', 'Catarina', 'Camila', 'Maria Valentina', 'Heloísa', 'Larissa', 'Malu', 'Maria Sophia',
             'Isadora', 'Maria Fernanda', 'Luana', 'Ayla', 'Lívia', 'Fernanda', 'Ana', 'Nina', 'Maria Clara', 'Amanda',
             'Liz', 'Isabel', 'Ana Clara', 'Alícia', 'Luna', 'Ana Lívia', 'Lorena', 'Carolina', 'Maria Cecília', 'Hadassa',
             'Gabriela', 'Agatha', 'Antonella', 'Brenda', 'Yasmin', 'Gabrielly', 'Joana', 'Raquel', 'Miguel', 'Pedro Henrique',
             'Thomas', 'Augusto', 'Davi', 'Pietro', 'Benício', 'Diego', 'Arthur', 'Cauã', 'Erick', 'Kaique', 'Pedro', 'Isaac',
             'Nathan', 'Yago', 'Gabriel', 'Caio', 'Fernando', 'Pedro Lucas', 'Bernardo', 'Vinicius', 'Yuri', 'Diogo', 'Lucas', 'Benjamin',
             'Laís', 'Luiz Gustavo', 'Matheus', 'João', 'Davi Lucca', 'Luiz Miguel', 'Rafael', 'Lucca', 'Calebe', 'Ricardo',
             'Heitor', 'João Miguel', 'Thales', 'Kauê', 'Enzo', 'Bryan', 'Vicente', 'Luan', 'Guilherme', 'Joaquim',
             'João Guilherme', 'Luiz Henrique', 'Nicolas', 'João Vitor', 'Vitor Hugo', 'Danilo', 'Lorenzo', 'Thiago', 'Anthony',
             'Marcelo', 'Gustavo', 'Antônio', 'Ryan', 'Gael', 'Felipe', 'Davi Lucas', 'Breno', 'Juan', 'Samuel', 'Francisco', 'João Lucas']

    def __init__(self, nome):
        super().__init__(nome)
        self.__nome = nome
        self.__tamanho = None

    def sorteioAniversario(self):
        dia = str(random.randint(1,30))
        mes = str(random.randint(1,13))
        ano = str(random.randint(1960,2001))
        return dia.zfill(2)+mes.zfill(2)+ano

    def sorteioCpf(self):
        cpf = str(random.randint(10000000000, 99999999999))
        return cpf

    def sorteioCodigo(self):
        codigo = random.randint(100000, 700000)
        return codigo

    def sorteioNome(self):
        return random.choice(self.__nomes)

    def sorteioCurso(self):
        return random.choice(self.__cursos)

    def gerar(self):
        cont = 1
        listaAluno=[]
        for aluno in range(100):
            cod, nome, curso, cpf, anv = cont, \
                                         self.sorteioNome(), \
                                         self.sorteioCurso(), \
                                         self.sorteioCpf(), \
                                         self.sorteioAniversario()
            aluno = Aluno(cod, nome, curso, cpf, anv)
            listaAluno.append(aluno)
            cont += 1
        #print(listaAluno)
        self.gerarArquivoInicial(listaAluno)