import os
import operator


class Arquivo(object):

    def __init__(self, nome=None):
        self.__nome = nome

    #CRIA ARQUIVO A PARTIR DE UMA LISTA DE ALUNOS ALEATÓRIOS
    def gerarArquivoInicial(self, lista):

        #fazer o arquivo Registro
        arqRegObject = self.__abreArquivo(self.__nome, 'w+b')
        for registro in lista:
            self.__escreveRegistro(arqRegObject, registro)
        self.__fechaArquivo(arqRegObject)

        #fazer o arquivo Index
        self.__fazerArquivoIndexInicial()

        print('\nNOVO ARQUIVO GERADO')

    #PERCORRE SEQUENCIALMENTE O ARQUIVO DE REGISTROS
    def exibirArquivoRegistro(self):
        arqObject = self.__abreArquivo(self.__nome, 'rb')
        if arqObject != None:
            print('\n------- REGISTROS -------')
            while arqObject.tell() != os.stat(self.__nome).st_size:
                self.__imprimirRegistro(arqObject)
            arqObject.close()

    # PERCORRE SEQUENCIALMENTE O ARQUIVO DE INDEX
    def exibirArquivoIndex(self):
        arqIndexObject = self.__abreArquivo(self.__nome,'rb')
        if arqIndexObject != None:
            print('\n---- ARQUIVO INDEX ----')
            while arqIndexObject.tell() != os.stat(self.__nome).st_size:
                cod = int.from_bytes(arqIndexObject.read(4), byteorder='big')
                posicao = int.from_bytes(arqIndexObject.read(4), byteorder='big')
                print('CÓDIGO: {} | POSIÇÃO: {}'.format(cod, posicao))
            arqIndexObject.close()

    # ALTERA A LAPIDE DO ANTIGO REGISTRO, ADICIONA O REGISTRO ALTERADO AO FINAL DO ARQUIVO E ATUALIZA O ARQUIVO INDEX
    def adicionarRegistroAlterado(self, registro, posAnterior):

        arqRegObject = self.__abreArquivo(self.__nome,'r+b')
        arqRegObject.seek(posAnterior)
        arqRegObject.write(b'N')
        arqRegObject.close()

        if self.__nome is not None:
            arqRegObject = self.__abreArquivo(self.__nome, 'a+b')
            # verificar posição inicial
            pos = arqRegObject.tell()
            print(pos)
            self.__escreveRegistro(arqRegObject, registro)
            arqRegObject.close()

            self.__adicionarIndex(registro.getCod(), pos)
            print('\nNOVO REGISTRO ADICIONADO')

            self.__fazerArquivoIndex()
            print('\nARQUIVO INDEX ATUALIZADO')

    #ADICIONA DE FORMA ORDENADA UM NOVO REGITRO NO ARQUIVO REGISTRO E SEU RESPECTIVO INDEX NO ARQUIVO INDEX
    def adicionarNovoRegistro(self, registro):
        num = 0
        arqIndexObject = self.__abreArquivo('arquivoIndex', 'rb')
        if arqIndexObject != None:
            arqIndexObject.seek(0,2)
            arqIndexObject.seek(arqIndexObject.tell() - 8)
            num = int.from_bytes(arqIndexObject.read(4), byteorder='big')
            arqIndexObject.read(4)
            arqIndexObject.close()

        registro.setCod(num + 1)

        arqRegObject = self.__abreArquivo(self.__nome, 'a+b')
        # verificar posição inicial
        pos = arqRegObject.tell()
        self.__escreveRegistro(arqRegObject, registro)
        arqRegObject.close()

        self.__adicionarIndex(registro.getCod(), pos)
        print('\nNOVO REGISTRO ADICIONADO COM CÓDIGO {}'.format(num+1))

    #BUSCA PELO CÓDIGO, ALTERA A LÁPIDE E ATUALIZA O ARQUIVO INDEX
    def excluirPorCodigo(self, codigo):
        arqIndexObject = self.__abreArquivo(self.__nome,'rb')
        if arqIndexObject != None:
            while arqIndexObject.tell() != os.stat(self.__nome).st_size:
                index = self.__lerIndex(arqIndexObject)
                if int.from_bytes(index[0], byteorder='big') == codigo:
                    pos = int.from_bytes(index[1], byteorder='big')
                    #print('Achei -> ', pos)
                    arqRegObject = open('arquivoRegistro','r+b')
                    arqRegObject.seek(pos)
                    arqRegObject.write(b'N')
                    arqRegObject.seek(pos)
                    self.__imprimirRegistro(arqRegObject)
                    arqRegObject.close()
                    break
            arqIndexObject.close()
            self.__fazerArquivoIndexInicial()

    #BUSCA SEQUENCIAL PELO CÓDIGO NO ARQUIVO INDEX E IMPRIME A INFORMAÇÃO PELA POSIÇÃO NO ARQUIVO DE REGISTRO
    def buscarPorCodigo(self, codigo):

        arqIndexObject = self.__abreArquivo(self.__nome,'rb')
        if arqIndexObject != None:
            check = 0;
            while arqIndexObject.tell() != os.stat(self.__nome).st_size and check==0:
                index = self.__lerIndex(arqIndexObject)
                if int.from_bytes(index[0], byteorder='big') == codigo:
                    pos = int.from_bytes(index[1], byteorder='big')
                    #print('Achei -> ', pos)
                    print('\n---- REGISTRO ENCONTRADO ----')
                    arqRegObject = open('arquivoRegistro','rb')
                    arqRegObject.seek(pos)
                    self.__imprimirRegistro(arqRegObject)
                    arqRegObject.close()
                    check = 1
                if int.from_bytes(index[0], byteorder='big') > codigo:
                    check = 2


            if check != 1:
                print('\nMATRÍCULA NÃO ENCONTRADA')
            arqIndexObject.close()

    #PERCORRE SEQUENCIALMENTE O ARQUIVO INDEX E IMPRIME INFORMAÇÃO DE CADA REGISTRO PELA POSIÇÃO NO ARQUIVO REGISTRO
    def exibirRegPorIndex(self):
        arqIndexObject = self.__abreArquivo(self.__nome, 'rb')
        arqRegObject = self.__abreArquivo('arquivoRegistro', 'rb')

        if arqIndexObject != None and arqRegObject != None:

            print('\n------ REGISTROS ------')
            while arqIndexObject.tell() != os.stat(self.__nome).st_size:
                # index = tuple(cod,pos)
                index = self.__lerIndex(arqIndexObject)
                pos = int.from_bytes(index[1], byteorder='big')
                arqRegObject.seek(pos)
                self.__imprimirRegistro(arqRegObject)

            arqIndexObject.close()
            arqRegObject.close()

    #BUSCA SEQUENCIAL ATE O CODIGO E RECUPERA INFORMAÇÕES DO REGISTRO PELA POSIÇÃO NO ARQUIVO REGISTRO
    def recuperarRegistro(self, codigo):
        arqIndexObject = self.__abreArquivo(self.__nome,'rb')
        if arqIndexObject != None:
            reg = None
            while arqIndexObject.tell() != os.stat(self.__nome).st_size:
                #index = tuple(cod,pos)
                index = self.__lerIndex(arqIndexObject)
                if int.from_bytes(index[0], byteorder='big') == codigo:
                    pos = int.from_bytes(index[1], byteorder='big')
                    #print('Achei -> ', pos)
                    arqRegObject = open('arquivoRegistro', 'rb')
                    arqRegObject.seek(pos)
                    reg = self.__lerRegistro(arqRegObject)
                    arqRegObject.close()
                    break
            arqIndexObject.close()
            return reg

    #LER E RETORNA 4 BYTES DE CODIGO(CHAVE) E 4 BYTES DE POSIÇÃO NO ARQUIVO INDEX
    def __lerIndex(self, arqIndexObject):
        cod = arqIndexObject.read(4)
        pos = arqIndexObject.read(4)
        return cod, pos

    #LER E RETORNA 1BYTE DE LAPIDE, 4 BYTES DE CODIGO(CHAVE), 4 BYTES DE TAMANHO E N BYTES DE INFORMAÇÃO NO ARQUIVO REGISTRO
    def __lerRegistro(self, arqRegObject):
        pos = arqRegObject.tell()
        lapide = bytes(arqRegObject.read(1)).decode()
        cod = int.from_bytes(arqRegObject.read(4), byteorder='big')
        tam = int.from_bytes(arqRegObject.read(4), byteorder='big')
        info = bytearray(arqRegObject.read(tam)).decode()
        return pos, lapide, cod, info

    #ESCREVE 4 BYTES DE CODIGO(CHAVE) E 4 BYTES DE POSIÇÃO NO ARQUIVO INDEX
    def __adicionarIndex(self, codigo, pos):
        arqIndexObject = open('arquivoIndex', 'a+b')
        arqIndexObject.write(int(codigo).to_bytes(4,byteorder='big'))
        arqIndexObject.write(int(pos).to_bytes(4,byteorder='big'))
        arqIndexObject.close()

    #LÊ E IMPRIME AS INFORAÇÕES DO REGISTRO
    def __imprimirRegistro(self, arqRegObject):
        lapide = bytes(arqRegObject.read(1)).decode()
        cod = int.from_bytes(arqRegObject.read(4), byteorder='big')
        tam = int.from_bytes(arqRegObject.read(4), byteorder='big')
        info = bytes(arqRegObject.read(tam)).decode()

        infoLista = info.split('-')

        nome = infoLista[0]
        curso = infoLista[1]
        cpf = infoLista[2]
        cpfImprimir = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9]+ '-' + cpf[9:]
        data= infoLista[3]
        dataimprimir = data[0:2] + '/' + data[2:4] + '/' + data[4:]

        #print(lapide, cod, infoLista)

        print('Situação: {} \n'
              'Código: {} \n'
              'Nome: {} \n'
              'Curso: {} \n'
              'CPF: {} \n'
              'Data de Nascimento: {} \n'.format(lapide, str(cod).zfill(6), nome, curso,
                                          cpfImprimir, dataimprimir))

    #ATUALIZA ARQUIVO INDEX
    def __fazerArquivoIndex(self):
        arqRegObject = self.__abreArquivo('arquivoRegistro', 'rb')
        listaChaves = {}
        while arqRegObject.tell() != os.stat('arquivoRegistro').st_size:
            posicao = arqRegObject.tell()
            #print(posicao)
            lap = arqRegObject.read(1) #LER LAPIDE
            cod = int.from_bytes(arqRegObject.read(4), byteorder='big')
            tam = int.from_bytes(arqRegObject.read(4), byteorder='big')
            arqRegObject.seek(arqRegObject.tell() + tam) #LER INFO
            if lap is not b'N':
                listaChaves[cod] = posicao #SALVAR COD:POSICAO
        arqRegObject.close()

        # ordenar pela chave
        listaOrdenada = sorted(listaChaves.items(), key=operator.itemgetter(0))

        #SALVAR INDEX ORDENADO POR CHAVE
        arqIndexObject = open('arquivoIndex', 'wb')
        for item in listaOrdenada:
            arqIndexObject.write(int(item[0]).to_bytes(4, byteorder='big'))
            arqIndexObject.write(int(item[1]).to_bytes(4, byteorder='big'))
        arqIndexObject.close()

    #CRIA PRIMEIRO ARQUIVO INDEX
    def __fazerArquivoIndexInicial(self):
        arqRegObject = self.__abreArquivo('arquivoRegistro', 'rb')
        arqIndexObject = open('arquivoIndex', 'wb')
        while arqRegObject.tell() != os.stat('arquivoRegistro').st_size:
            posicao = arqRegObject.tell()
            #print(posicao)
            lap = arqRegObject.read(1) #LER LAPIDE
            cod = arqRegObject.read(4)
            tam = int.from_bytes(arqRegObject.read(4), byteorder='big')
            arqRegObject.seek(arqRegObject.tell() + tam) #LER INFO
            if lap != b'N':
                #print(lap, cod)
                arqIndexObject.write(cod)
                arqIndexObject.write(int(posicao).to_bytes(4,byteorder='big'))
        arqRegObject.close()
        arqIndexObject.close()

    #ESCREVE 1BYTE DE LAPIDE, 4 BYTES DE CODIGO(CHAVE), 4 BYTES DE TAMANHO E N BYTES DE INFORMAÇÃO NO ARQUIVO REGISTRO
    def __escreveRegistro(self, arqObject, registro):
        # 1 byte de lapide | 4 bytes codigo | 4 bytes de tamanho| N bytes de info
        arqObject.write(registro.getLapide())
        arqObject.write(int(registro.getCod()).to_bytes(4, byteorder='big'))
        arqObject.write(len(registro.getByteArray()).to_bytes(4, byteorder='big'))
        arqObject.write(registro.getByteArray())

    #TESTA E ABRE ARQUIVO
    def __abreArquivo(self, nome, modo):
        arqObject = None
        try:
            arqObject = open(nome, modo)
            return arqObject
        except FileNotFoundError:
            return None

    #FECHA ARQUIVO
    def __fechaArquivo(self, arqObject):
        arqObject.close()