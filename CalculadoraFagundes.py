def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    return a / b

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

while True:
    print("\nCalculadora Simples")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "5":
        print("Encerrando a calculadora. Até mais!")
        break
    
    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida! Escolha uma opção entre 1 e 5.")
        continue
    
    num1 = obter_numero("Digite o primeiro número: ")
    num2 = obter_numero("Digite o segundo número: ")
    
    if opcao == "1":
        resultado = soma(num1, num2)
    elif opcao == "2":
        resultado = subtracao(num1, num2)
    elif opcao == "3":
        resultado = multiplicacao(num1, num2)
    elif opcao == "4":
        resultado = divisao(num1, num2)
    
    print(f"Resultado: {resultado}")
