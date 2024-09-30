from colorama import Fore, Style, init

# Inicializa o colorama:
init(autoreset=True)

# Função principal da calculadora:
def calculadora():
    # Loop para manter a calculadora em execução:
    while True:
        # Exibe uma linha de separação para organizar o layout:
        print(Fore.CYAN + "\n" + "=" * 40)
        print(Fore.YELLOW + "               CALCULADORA            ")
        print(Fore.CYAN + "=" * 40)

        # Solicitar ao usuário os dois números e tratamento de exceção:
        try:
            num1 = float(input(Fore.GREEN + "\nDigite o primeiro número: "))
            num2 = float(input(Fore.GREEN + "Digite o segundo número: "))
        except ValueError:
            print(Fore.RED + "\nErro: Por favor, insira um número válido.")
            continue

        # Exibe as opções de operação de uma forma mais clara:
        print(Fore.BLUE + "\nEscolha a operação:")
        print(Fore.YELLOW + "[+] Soma")
        print(Fore.YELLOW + "[-] Subtração")
        print(Fore.YELLOW + "[*] Multiplicação")
        print(Fore.YELLOW + "[/] Divisão")

        # Solicita ao usuário o operador matemático:
        operador = input(Fore.GREEN + "\nDigite a operação desejada): ")

        # Condição para realizar a operação matemática escolhida:
        if operador == "+":
            resultado = num1 + num2
            print(Fore.MAGENTA + f"\nResultado: {num1} + {num2} = {resultado}")
        elif operador == "-":
            resultado = num1 - num2
            print(Fore.MAGENTA + f"\nResultado: {num1} - {num2} = {resultado}")
        elif operador == "*":
            resultado = num1 * num2
            print(Fore.MAGENTA + f"\nResultado: {num1} * {num2} = {resultado}")
        elif operador == "/":
            if num2 == 0:
                print(Fore.RED + "\nErro: divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print(Fore.MAGENTA + f"\nResultado: {num1} / {num2} = {resultado}")
        else:
            print(Fore.RED + "\nOperador inválido! Tente novamente.")
            continue

        # Pergunta se deseja realizar outra operação:
        repetir = input(Fore.CYAN + "\nDeseja realizar outra operação? (S/N): ").strip().upper()
        # Condição para encerrar a calculadora:
        if repetir == "N":
            print(Fore.YELLOW + "\nEncerrando a calculadora. Até logo!")
            print(Fore.CYAN + "=" * 40)
            break
        elif repetir != "S":
            print(Fore.RED + "\nEntrada inválida. Encerrando a calculadora.")
            print(Fore.CYAN + "=" * 40)
            break

# Inicializa a calculadora:
calculadora()
