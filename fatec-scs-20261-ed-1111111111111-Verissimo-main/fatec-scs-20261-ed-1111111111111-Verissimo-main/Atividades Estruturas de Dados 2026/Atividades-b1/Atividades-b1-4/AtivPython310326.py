n1 = float(input("N1: "))
n2 = float(input("N2: "))
c = 0

while c <= 2:
    op = input("+, -, *, /: ")

    if op == "+":
        r = n1 + n2
    elif op == "-":
        r = n1 - n2
    elif op == "*":
        r = n1 * n2
    elif op == "/":
        if n2 != 0:
            r = n1 / n2
        else:
            print("Erro: divisão por zero!")
            
    else:
        print("Operação inválida!")

    print("Resultado:", r)
        
    if c == 2:
        break

    ru = input("Deseja continuar? (S/N): ").upper()

    if ru == "S":
        n1 = r
        n2 = float(input("Digite o próximo número: "))
        c += 1
    else:
        print("Fim")
        break
