from Aluno import Aluno
from Arquivo import Arquivo
from GerarArquivo import GerarArquivo

def menu():
    print('\n---- MENU PRINCIPAL ----')
    print('0 - SAIR')
    print('1 - GERAR ARQUIVO NOVO')
    print('2 - LER ARQUIVO - ARQUIVO REGISTRO')
    print('3 - LER ARQUIVO - ARQUIVO INDEX (ORDENADO)')
    print('4 - ADICIONAR')
    print('5 - EXCLUIR POR CÓDIGO')
    print('6 - BUSCAR POR CÓDIGO')
    print('7 - ALTERAR REGISTRO')

    op = input('Opção: ')
    return op

def menuAlterar():
    print('\n---- MENU DE ALTERAÇÃO ----')
    print('O QUE DESEJA ALTERAR?\n'
          '0 - SAIR\n'
          '1 - NOME\n'
          '2 - CURSO\n'
          '3 - CPF\n'
          '4 - ANIVERSÁRIO\n'
          '5 - SALVAR E SAIR')
    op2 = input('Opção: ')
    return op2

arquivoOriginal = 'arquivoRegistro'
arquivoIndex = 'arquivoIndex'

op = menu()
while op != '0':
    if op == '1': #GERAR NOVO ARQUIVO COM REGISTROS
        gerarArquivo = GerarArquivo(arquivoOriginal)
        gerarArquivo.gerar()

    elif op == '2': #LISTAR ARQUIVO REGISTRO
        arquivo = Arquivo(arquivoIndex)
        arquivo.exibirRegPorIndex()

    elif op == '3': #LISTAR ARQUIVO INDEX
        arquivo = Arquivo(arquivoIndex)
        arquivo.exibirArquivoIndex()

    elif op == '4':
        aluno = Aluno()
        nome = input('NOME: ')
        aluno.setNome(nome)

        curso = input('CURSO: ')
        aluno.setCurso(curso)

        cpf = input('CPF: ')
        aluno.setCpf(cpf)

        data = input('DATA DA NASCIMENTO: ')
        aluno.setAniversario(data)

        arquivo = Arquivo(arquivoOriginal)
        arquivo.adicionarNovoRegistro(aluno)

    elif op == '5':
        matricula = int(input('MATRICULA: '))
        arquivo = Arquivo(arquivoIndex)
        arquivo.excluirPorCodigo(matricula)

    elif op == '6':

        matricula = int(input('MATRICULA: '))
        arquivo = Arquivo(arquivoIndex)
        arquivo.buscarPorCodigo(matricula)

    elif op == '7':
        matricula = int(input('MATRÍCULA: '))
        arquivo = Arquivo(arquivoIndex)
        reg = arquivo.recuperarRegistro(matricula)
        if reg != None:
            info = reg[3].split('-')

            aluno = Aluno()
            aluno.setCod(reg[2])
            aluno.setNome(info[0])
            aluno.setCurso(info[1])
            aluno.setCpf(info[2])
            aluno.setAniversario(info[3])
            #print(aluno.__dict__)

            op2 = menuAlterar()

            while op2 != '0':

                if op2 == '1':
                    nome = input('Digite o novo nome: ')
                    aluno.setNome(nome)
                elif op2 == '2':
                    curso = input('Digite o novo curso: ')
                    aluno.setCurso(curso)
                elif op2 == '3':
                    cpf = input('Digite o novo número de CPF')
                    aluno.setCpf(cpf)
                elif op2 == '4':
                    aniversario = input('Digite nova data de aniversário')
                    aluno.setAniversario(aniversario)
                elif op2 == '5':
                    arquivoReg = Arquivo(arquivoOriginal)
                    arquivoReg.adicionarRegistroAlterado(aluno, reg[0])
                    break

                op2 = menuAlterar()



    op = menu()