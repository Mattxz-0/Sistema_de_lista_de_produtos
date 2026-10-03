produtos = []
valor_total = 0.0

while True:
    print("""
    ==========================
        MENU DE OPÇÕES      
    ==========================
    1 - Cadastrar produto
    2 - Visualizar pedido
    3 - Sair
    ==========================
    """)

    choice = int(input('Digte a opção desejada: '))
    match choice:
        case 1:
            while True:
                produto = str(input('\nDigite o nome do produto que deseja cadastrar: '))
                if produto == "":
                    print('\nPor favor, digite um produto válido.\n')
                else:
                    while True:
                        valor_str = input('\nDigite o valor do produto: ')
                        if valor_str == "":
                            print('\nPor favor, digite um valor válido.\n')
                        else:
                            valor = float(valor_str)
                            produtos = produtos + [[produto, valor]]
                            valor_total = valor_total + valor
                            break
                break
        case 2:
            if len(produtos) == 0:
                print('\nNenhum produto cadastrado!')
            else:
                print('\n--- SEUS PRODUTOS ---')
                i = 0
                while i < len(produtos):
                    item = produtos[i]
                    nome = item[0]
                    preco = float(item[1])
                    print(f'{i + 1} - {nome} | R${preco:.2f}')
                    i = i + 1

                print(f'\n{len(produtos)} produto(s) no carrinho')
                print(f'Valor total: {valor_total:.2f}')
                print('''
======== OPÇÕES ========
1- Remover produto
2- Voltar para o menu
                ''')
                choice_lista = int(input('Digite a opção desejada: '))

                match choice_lista:
                    case 1:
                        num_remover = int(input('\nDigite o número do produto que deseja remover: '))
                        indice = num_remover - 1

                        if indice >= 0 and indice < len(produtos):
                            produto_removido = produtos[indice]
                            valor_remover = produto_removido[1]
                            novos_produtos = []

                            i = 0
                            while i < len(produtos):
                                if i != indice:
                                    novos_produtos = novos_produtos + [produtos[i]]
                                i = i + 1

                            produtos = novos_produtos
                            valor_total = valor_total - valor_remover
                            print('\nItem removido com sucesso!')
                        else:
                            print('\nNúmero de produto errado!')

                    case 2:
                        print('\nRetornando ao menu.')

        case 3:
            print('\nSaindo do programa...\n')
            break
        case _:
            print('\nOpção inexistente, selecione uma válida!\n')