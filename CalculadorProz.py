def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."

while True:
    try:
        print("Calculadora")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == "+":
            print(soma(num1, num2))
        elif operacao == "-":
            print(subtracao(num1, num2))
        elif operacao == "*":
            print(multiplicacao(num1, num2))
        elif operacao == "/":
            print(divisao(num1, num2))
        else:
            print("Operação inválida.")
    except ValueError:
        print("Erro: Digite apenas números inteiros.")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar == "n":
        break