opcao = -1

while opcao != 5:
    opcao = int(input("1. Somar \n2. Subtrair \n3. Multiplicar \n4. Dividir \n5. Sair \nDigite a opção: "))

    if opcao == 5:
        print("Saindo do programa...")
        break

    if opcao == 0 or opcao not in [1, 2, 3, 4, 5]:
        print("Opção inválida! \nEscolha entre 1 e 5.")
        continue

    num1 = int(input("Primeiro valor: "))
    num2 = int(input("Segundo valor: "))

    if opcao == 1:
        print("Resultado é:", num1 + num2)
    elif opcao == 2:
        print("Resultado é:", num1 - num2)
    elif opcao == 3:
        print("Resultado é:", num1 * num2)
    elif opcao == 4:
        if num2 == 0:
            print("Erro: Divisão por zero!")
        else:
            print("Resultado é:", num1 / num2)
