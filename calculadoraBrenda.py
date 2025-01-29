import os
def limparTela():
    os.system("cls" if os.name == "nt" else "clear")
    
while True:
    print ("Tabela de possibilidades de operações matemáticas")
    print ("Escolha um número de acordo com a opção:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair da calculadora")
    
    operacao = int(input("Escolha um número de acordo com a opção:"))

    limparTela()

    if operacao == 5:
        print("Saindo...")
        break


    num1 = float(input("Digite o primeiro número da operação:"))
    num2 = float(input("Digite o segundo número da operação:"))
    

    def operacoesCalculadora (operacao, num1, num2):
        match operacao:
          case 1:
            return num1 + num2
          case 2:
            return num1 - num2
          case 3:
            return num1 * num2
          case 4:
            return num1 / num2
          case _:
            print("Opção inválida, tente novamente!")
        
        
         
    resultado = operacoesCalculadora(operacao, num1, num2)
    if resultado == "Opção inválida, tente novamente!":
        print(resultado)
    
    else:
        print(f"O resultado da sua operação matemática é:{resultado}")
        
    input("/nPressione Enter para continuar... ")
    limparTela()