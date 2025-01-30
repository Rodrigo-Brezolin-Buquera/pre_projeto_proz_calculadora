def calculadora():
    while True: # Exibe o menu de operações a cada iteração do loop while.
        print("\nEscolha a operação:")
        print("1: Somar")
        print("2: Diminuir")
        print("3: Multiplicar")
        print("4: Dividir")
        print("5: Sair")
        
        # Entrada e verificação da operação. Se a entrada for válida continua. Senão exibe uma mensagem e retorna ao menu.
        opcao = input("Digite o número da operação desejada: ")
        
        # Verifica se o usuário quer sair
        if opcao == '5':
            print("Saindo da calculadora. Tchau, até a próxima!")
            break
        
        # Verifica se a opção é válida
        if opcao not in ['1', '2', '3', '4']:
            print("Essa opção não existe. Tente novamente!")
            continue
        
        # Solicita os dois valores numéricos e os converte para float
        try:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
        except ValueError: # Se o usuário inserir algo inválido, a função 'ValueError' será tratada.
            print("Valores inválidos! Insira números válidos.")
            continue
        
        # Realiza a operação com base na escolha
        if opcao == '1':
            resultado = num1 + num2
            print(f"Resultado da Soma: {num1} + {num2} = {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"Resultado da Subtração: {num1} - {num2} = {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"Resultado da Multiplicação: {num1} * {num2} = {resultado}")
        elif opcao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da Divisão: {num1} / {num2} = {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")

calculadora() # Chama a função calculadora novamente