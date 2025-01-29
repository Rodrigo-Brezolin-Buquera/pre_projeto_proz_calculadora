def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro! Digite um número válido.")

def somar():
  n1 = ler_numero('Insira o primeiro número da soma: ')
  n2 = ler_numero('Insira o segundo número da soma: ')
  resultado = n1 + n2
  return f'A soma de {n1} e {n2} é {resultado}'

def subtrair():
  n1 = ler_numero('Insira o primeiro número da subtração: ')
  n2 = ler_numero('Insira o segundo número da subtração: ')
  resultado = n1 - n2
  return f'A subtração de {n1} e {n2} é {resultado}'

def dividir():
    n1 = ler_numero('Insira o primeiro número da divisão: ')
    while True:
        n2 = ler_numero('Insira o segundo número da divisão: ')
        if n2 == 0:
            print("Erro! Não é possível dividir por zero. Tente novamente.")
        else:
            break
    resultado = n1 / n2
    return f'A divisão de {n1} por {n2} é {resultado}'

def multiplicar():
  n1 = ler_numero('Insira o primeiro número da multiplicação: ')
  n2 = ler_numero('Insira o segundo número da multiplicação: ')
  resultado = n1*n2
  return f'A multiplicação de {n1} e {n2} é {resultado}'

def menu():
    while True:
        print("\n--- ESCOLHA A OPERAÇÃO DESEJADA ---")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Dividir")
        print("4. Multiplicar")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(somar())
        elif escolha == "2":
            print(subtrair())
        elif escolha == "3":
            print(dividir())
        elif escolha == "4":
            print(multiplicar())
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha uma opção entre 1 e 4.")

menu()