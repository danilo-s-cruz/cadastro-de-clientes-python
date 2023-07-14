'''
CADASTRO DE CLIENTES
'''
from funcoes import (gerar_codigo, codigo_existe, incluir, alterar, excluir, listar_filtro)

clientes = []

while True:
    print(f'''
    {'-' * 50}
    CADASTRO DE CLIENTES
    {'-' * 50}
    1 - Inclusão
    2 - Alteração de Endereço
    3 - Exclusão
    4 - Listagem Geral
    5 - Listagem por CPF / CNPJ
    {'-' * 50}
    ''')
    opcao = input('Digite uma das opções acima: ').strip().upper()
    
    if opcao == 'S': # sair
        print('Saindo... Volte Sempre!')
        break
    
    elif opcao == '1': # incluir
        while True:
            print('-' * 50)
            print('INCLUSÃO DE CLIENTES')
            print('-' * 50)
            codigo = gerar_codigo(clientes)
            nome = input('Digite o Nome: ').strip().upper()
            end = input('Digite o Endereço: ').strip().upper()
            tipo = input('Pessoa [F]ísica ou [J]urídica: ').strip().upper()
            if tipo == 'F':
                cpf_cnpj = input('Informe o CPF: ').strip().upper()
            else:
                cpf_cnpj = input('Informe o CNPJ: ').strip().upper()
            print(incluir(clientes, codigo, nome, end, tipo, cpf_cnpj))
            opcao = input('Deseja continuar cadastrando [S/N]? ').strip().upper()
            if opcao != 'S':
                break
            
    elif opcao == '2': # alterar
        while True:
            print('-' * 50)
            print('ALTERAÇÃO DE ENDEREÇO')
            print('-' * 50)
            codigo = input('Informe o código: ').strip().upper()
            posicao = codigo_existe(clientes, codigo)
            if posicao > '-1':
                print(alterar(clientes, codigo))
                break
            elif posicao == '-1':
                print('Código informado não encontrado.')
            opcao = input('Tecle Enter para continuar ou [C] para Cancelar: ').strip().upper()
            if opcao == 'C':
                break

    elif opcao == '3': # excluir
        print('-' * 50)
        print('EXCLUSÃO DE CLIENTES')
        print('-' * 50)
        codigo = input('Informe o código: ').strip().upper()
        posicao = codigo_existe(clientes, codigo)
        if posicao > '-1':
            print(excluir(clientes, codigo))
        elif posicao == '-1':
            print('Código informado não encontrado.')
        opcao = input('Tecle Enter para continuar ou [C] para Cancelar: ').strip().upper()
        if opcao == 'C':
            break

    elif opcao == '4': # listar
        print('-' * 50)
        print('CLIENTES CADASTRADOS')
        print('-' * 50)
        for cliente in clientes:
            print(f'{cliente}')

    elif opcao == '5': # listar por tipo
        print('-' * 50)
        print('CLIENTES CADASTRADOS POR TIPO - CPF / CNPJ')
        print('-' * 50)
        print(listar_filtro(clientes))

    else:
        print('Opção Inválida! Tente novamente.')