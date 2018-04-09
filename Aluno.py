import re
import datetime

class Aluno(object):

    __lapide = b'S'

    def __init__(self, codigo=0, nome=' ', curso=' ', cpf='00000000000', aniversario='01010001'):
        self.__codigo = int(codigo)
        self.__nome = nome
        self.__curso = curso
        self.__cpf = cpf
        self.__aniversario = aniversario

    def setLapide(self, lapide):
        self.__lapide = lapide

    def setCod(self, codigo):
        self.__codigo = codigo

    def setNome(self, nome):
        self.__nome = nome

    def setCurso(self, curso):
        self.__curso = curso

    def setCpf(self, cpf):
        while len(cpf) != 11:
            cpf = input('CPF INVÁLIDO\n'
                        'DIGITE OS 11 DÍGITOS DO CPF: ')

        padraoCPF = ('(\d{11})')
        comp = re.search(padraoCPF, cpf)

        while comp == None:
            cpf = input('CPF INVÁLIDO\n'
                        'DIGITE SOMENTE NÚMEROS: ')
            comp = re.search(padraoCPF, cpf)

        self.__cpf = cpf

    def setAniversario(self, aniversario):

        while len(aniversario) != 8:
            aniversario = input('DATA INVÁLIDO\n'
                        'DIGITE A DATA (DDMMAAAA): ')

        check = False

        while check == False:
            try:
                datetime.datetime.strptime(aniversario, '%d%m%Y')
                check = True
            except ValueError:
                check = False
                aniversario = input('DATA INVÁLIDA\n'
                      'DIGITE NOVAMENTE A DATA DE NASCIMENTO (DDMMAAAA): ')
        self.__aniversario = aniversario

    def getLapide(self):
        return self.__lapide

    def getNome(self):
        return self.__nome

    def getCod(self):
        return self.__codigo

    def getCurso(self):
        return self.__curso

    def getCpf(self):
        return self.__cpf

    def getAniversario(self):
        return self.__aniversario

    def getByteArray(self):
        return bytearray(self.__str__(), 'utf-8')

    def __str__(self):
        return str(self.__nome) + '-' + str(self.__curso) + '-' + str(self.__cpf) + '-' + str(self.__aniversario)






