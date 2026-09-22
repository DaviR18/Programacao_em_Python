

Nome = input("Digite seu nome: ")
Idade = int(input("Digite sua idade: "))
Qnt_de_ouro = int(input("Digite a qtd de ouro: "))
Possuir_espada = input("vc tem espada: ")

if Possuir_espada == 'sim':
    Possuir_espada = True
else:
    Possuir_espada = False



print (Possuir_espada)

Qnt_de_ouro += 20
Qnt_de_ouro -= 15

print(Qnt_de_ouro)

if Idade > 18:
    print("ele é de maior")



print("ele tem espada") if Possuir_espada == True else print("ele nao tem espada")



print("Ficha do personagem: ")
print("nome: ", Nome)
print("Idade: ", Idade)
print("quantidade de ouro: ", Qnt_de_ouro)
if Possuir_espada == True:
    print("ele tem espada")
else:
    print("ele nao tem espada")