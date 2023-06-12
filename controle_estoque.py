# função de cadastro das peças
def cadastrarpeca(codigo):
    while True:

        print('-----------CADASTRO DE PEÇAS---------------\n')
        nome = str(input('DIGITE O NOME DA PEÇA:\n'))
        fabricante = str(input('DIGITE O FABRICANTE DA PEÇA\n'))
        try:
            valor = float(input('DIGITE O VALOR DA PEÇA\n'))
        except ValueError:
            print('\nDIGITE UM NÚMERO INTEIRO!\n')
            continue

        dicionariopecas = {'código': codigo,
                           'nome': nome.upper(),
                           'fabricante': fabricante.upper(),
                           'valor': 'R$ {:.2f}'.format(valor)}

        listapecas.append(dicionariopecas.copy())

        print('\nCOD', codigo, nome.upper(), fabricante.upper(), 'R$ {:.2f}\n'.format(valor))
        break


#função de  consulta das peças
def consultarpeca():
    while True:
        try:
            print('-----------CONSULTA DE PEÇAS---------------\n')
            consultar = int(input(
                '\nDIGITE A OPÇÃO DESEJADA:\n1 - Consultar todas as peças\n2 - Consultar por código da peça\n3 - Consultar por fabricante\n4 - Retornar\n'))

            if consultar == 1:
                print('-------------LISTA DE PEÇAS--------------\n')
                for peca in listapecas:
                    for key, value in peca.items():
                        print("{} : {}\n".format(key, value))
            elif consultar == 2:
                print('------CONSULTA POR CÓDIGO DA PEÇA--------\n')
                entrada = int(input('\nDIGITE O CÓDIGO DA PEÇA:\n'))
                for pecas in listapecas:
                    if (pecas['código'] == entrada):
                        for key, value in pecas.items():
                            print("{} : {}\n".format(key, value))

            elif consultar == 3:
                print('-----CONSULTA POR FABRICANTE DA PEÇA------\n')
                entrada = str(input('\nDIGITE O FABRICANTE DA PEÇA:\n').upper())
                for pecas in listapecas:
                    if (pecas['fabricante'] == entrada):
                        for key, value in pecas.items():
                            print("{} : {}\n".format(key, value))

            elif consultar == 4:
                print('RETORNAR\n')
                break

            else:
                print("DIGITE UMA OPÇÃO DE 1 A 4!\n")
                continue

        except ValueError:
            print("DIGITE UMA OPÇÃO DE 1 A 4!\n")
            continue


#função de remover as peças
def removerpeca():
    print('----------REMOÇÃO DE PEÇAS-------------\n')

    while True:

        try:
            entrada = int(input('\nDIGITE O CÓDIGO DA PEÇA:\n'))

            for pecas in listapecas:

                if (pecas['código'] == entrada):


                    listapecas.remove(pecas)


        except ValueError:
            print('DIGITE SOMENTE NÚMEROS\n')
            continue

        break



#código principal
print('Bem vindo ao Controle de estoque da bicicletaria Erick Adriél Garcia RU 4045447\n')


listapecas = []
registrodepecas = 0

while True:
    try:
        opcao = int(input(
            '\nDIGITE A OPÇÃO DESEJADA:\n\n1 - CADASTRAR PEÇA\n2 - CONSULTAR PEÇA\n3 - REMOVER PEÇA\n4 - SAIR\n'))
        if opcao == 1:
            print('Opção 1 ok\n')

            registrodepecas += 1
            cadastrarpeca(registrodepecas)


        elif opcao == 2:
            print('Opção 2 ok\n')
            consultarpeca()

        elif opcao == 3:
            print('Opção 3 ok\n')
            removerpeca()

        elif opcao == 4:
            print('Opção 4 ok\n')
            print('FIM DO PROGRAMA')
            break

        else:
            print("DIGITE UMA OPÇÃO DE 1 A 4!\n")
            continue

    except ValueError:
        print("DIGITE UMA OPÇÃO DE 1 A 4!\n")
        continue
