import os

lista = []
while True:
    print("Selecione uma opção")
    opcao = input('[i]nserir, [a]pagar, [l]istar: ')

    if opcao == 'i' :
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a' :
        os.system('cls')
        indice_str = input('Escolha indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Nada foi apagado')

    elif opcao == 'l' :
        os.system('cls')

        if len(lista) == 0 :
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else :
        print('Favor selecionar opção válida!')