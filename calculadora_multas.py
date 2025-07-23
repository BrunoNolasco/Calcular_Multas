#
def localidade():
    while True:
        entrada = input("Indique a velocidade em que circulava: ").strip().lower()

        if entrada == "menu":
            break

        elif entrada.isdigit():
            velocidade = int(entrada)

            if 50 < velocidade < 90:
                print(f"A multa para a velocidade de {velocidade}km/h numa localidade é de €60.\n")
            elif 90 <= velocidade < 120:
                print(f"A multa para a velocidade de {velocidade}km/h numa localidade é de €120.\n")
            elif velocidade >= 120:
                print(f"A multa para a velocidade de {velocidade}km/h numa localidade é de €320.\n")
            else:
                print("Estava dentro do limite de velocidade.\n")
        else:
            print("Entrada inválida. Digite um número ou 'menu'.\n")


def fora_localidade():
    while True:
        entrada = input("Indique a velocidade em que circulava: ").strip().lower()

        if entrada == "menu":
            break

        elif entrada.isdigit():
            velocidade = int(entrada)

            if 90 < velocidade < 120:
                print(f"A multa para a velocidade de {velocidade}km/h fora de uma localidade é de €60.\n")
            elif velocidade >= 120:
                print(f"A multa para a velocidade de {velocidade}km/h fora de uma localidade é de €120.\n")
            else:
                print("Estava dentro do limite de velocidade.\n")
        else:
            print("Entrada inválida. Digite um número ou 'menu'.\n")


def autoestrada():
    while True:
        entrada = input("Indique a velocidade em que circulava: ").strip().lower()

        if entrada == "menu":
            break

        elif entrada.isdigit():
            velocidade = int(entrada)

            if 120 < velocidade < 150:
                print(f"A multa para a velocidade de {velocidade}km/h numa autoestrada é de €60.\n")
            elif 150 <= velocidade < 175:
                print(f"A multa para a velocidade de {velocidade}km/h numa autoestrada é de €120.\n")
            elif velocidade >= 175:
                print(f"A multa para a velocidade de {velocidade}km/h numa autoestrada é de €360.\n")
            else:
                print("Estava dentro do limite de velocidade.\n")
        else:
            print("Entrada inválida. Digite um número ou 'menu'.\n")


def menu():
    while True:
        print('Bem-Vindo(a) ao programa "Calcular Multas"! \n')
        print("Por onde circulava? \n")
        print("1 - Localidade")
        print("2 - Fora da Localidade")
        print("3 - Autoestrada")
        print("4 - Fechar programa\n") 
        opcao = input("Indique a opção a executar: ").strip()

        if opcao == "1":
            print('\nEscreva "menu" para voltar ao menu principal\n')
            localidade()
        elif opcao == "2":
            print('\nEscreva "menu" para voltar ao menu principal\n')
            fora_localidade()
        elif opcao == "3":
            print('\nEscreva "menu" para voltar ao menu principal\n')
            autoestrada()
        elif opcao == "4":
            print("Obrigado! ")
            exit()
        else:
            print("Opção inválida! Tente de novo!\n")


menu()
