Media = float(input("Digite sua media: "))

if Media >= 7:
    print("aprovado")
else:
    if Media >= 4:
        print("vai fazer AF")
        AF = float(input("Digite sua nota na AF: "))
        if AF >= 4 and ((AF + Media)/2) >= 5:
            print("aprovado")
        else:
            print("reprovado")
    else:
        print("reprovado")




Num = int(input("Digite um numero inteiro ae: "))
if Num % 2 == 0:
    print("eh par")
else:
    print("eh impar")