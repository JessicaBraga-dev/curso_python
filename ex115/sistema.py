from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursopython.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver Pessoas cadastradas ', 'Cadastrar nova pessoa', 'Sair do programa'])
    if resposta == 1:
        #opção de lista o conteúdo de um arquivo!
        leiaArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema ... Até logo!')
        break
    else:
        cabecalho('\033[31mERRO! Digite uma opção válido!\033[m')
    sleep(2)
