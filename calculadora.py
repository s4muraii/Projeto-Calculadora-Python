v = 1
w = 1
while v == 1:

    print ("Seja bem-vindo! Está é uma calculadora funcional em Python") # Mensagem de inicialização

    while w == 1:
        a = input("Qual operação deseja realizar? \n Adição = 1 \n Subtração = 2 \n Multiplicação = 3 \n Divisão = 4 \n") # Escolha da operação
        if a == "1": # Adição
            print("Adição selecionada")
            b = float(input("Digite o primeiro número "))
            c = float(input("Digite o segundo número "))
            d = (b + c)
            print (f"O resultado é {d}") # Resultado da operação
            e = input("Deseja continuar a operação? \n s - Sim \n n - Não \n") # Continuação da operação
            if e == "s":
                f = float(input(f"Acrescente o valor a {d}: \n"))
                g = (d + f)
                print (f"O resultado é {g}") # Resultado caso o usuário continue a operação
                m = input("Deseja sair agora? \n s = Sim \n n = Não \n") # Escolha do usuário para sair ou não do software
                if m == "s":
                    v = 2
                elif m == "n":
                    w = 1
            elif e == "n":
                m = input("Deseja sair agora? \n s = Sim \n n = Não \n")
                if m == "s":
                    v = 2
                elif m == "n":
                    w = 1
                
        if a == "2": # Subtração
            print("Subtração selecionada")
            b = float(input("Digite o primeiro número "))
            c = float(input("Digite o segundo número "))
            d = (b - c)
            print (f"O resultado é {d}")
            e = input("Deseja continuar a operação? \n s - Sim \n n - Não \n")
            if e == "s":
                f = float(input(f"Retire o valor a {d}: \n"))
                g = (d - f)
                print (f"O resultado é {g}")
                m = input("Deseja sair agora? \n s = Sim \n n = Não \n")
                if m == "s":
                    v = 2
                else:
                    w = 1
            elif e == "n":
                m = input("Deseja sair agora? \n s = Sim \n n = Não \n")
                if m == "s":
                    v = 2
                else:
                    w = 1

        if a == "3": # Multiplicação
            print("Multiplicação selecionada")
            b = float(input("Digite o primeiro número "))
            c = float(input("Digite o segundo número "))
            d = (b * c)
            print (f"O resultado é {d}")
            e = input("Deseja continuar a operação? \n s - Sim \n n - Não \n")
            if e == "s":
                f = float(input(f"Multiplique o valor a {d}: \n"))
                g = (d * f)
                print (f"O resultado é {g}")
                m = input("Deseja sair agora? \n s = Sim \n n = Não \n")
                if m == "s":
                    v = 2
                else:
                    w = 1
            elif e == "n":
                m = input("Deseja sair agora? \n s = Sim \n n = Não \n")
                if m == "s":
                    v = 2
                else:
                    w = 1

        if a == "4": # Divisão
            print("Divisão selecionada")
            b = float(input("Digite o primeiro número "))
            c = float(input("Digite o segundo número "))
            d = (b / c)
            print (f"O resultado é {d}")
            e = input("Deseja continuar a operação? \n s - Sim \n n - Não \n")
            if e == "s":
                f = float(input(f"Divida o valor a {d}: \n"))
                g = (d / f)
                print (f"O resultado é {g}")
                m = input("Deseja sair agora? \n s = Sim \n n = Não \n")
                if m == "s":
                    v = 2
                else:
                    w = 1
            elif e == "n":
                m = input("Deseja sair agora? \n s = Sim \n n = Não \n")
                if m == "s":
                    v = 2
                else:
                    w = 1
