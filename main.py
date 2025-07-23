while True:    
        
    print("Bem-Vindo(a) ao programa Calcular Multas! \n")
    print("Por onde circulava? \n")
    print("1 - Localidade \n")
    print("2 - Fora da Localidade \n")
    print("3 - Autoestrada \n")
    print("4 - Fechar programa \n") 
    opcao = input("Indique a opção a executar: ")
    
    if opcao == "1":
        print("A executar a soma: ")
        soma()    
    elif opcao == "2":
        print("A executar a subtração: ")
        subtracao()
    elif opcao == "3":
        print("Ã executar a multiplicação: ")
        multi()    
    elif opcao == "4":
        print("A executar a divisão: ")
        divisao()
    elif opcao == "5":
        print("A executar o calculo de área: ")
        area_retan()
    elif opcao == "6":
        print("A executar a verificação: ")
        verificar_par_impar()
    elif opcao == "7":
        print("Obrigado! ")
        break
    else:
        print("Opção inválida! Tente de novo! ")      