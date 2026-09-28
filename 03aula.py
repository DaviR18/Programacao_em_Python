print("Faça sua fixa de personagem:")
Nome = input("Digite seu nome: ")
Vida = int(input("Digite a sua vida: "))
Comida = int(input("Digite a sua comida: "))
Possui_espada = input("Digite se vc tem espada (sim ou nao): ")
if Possui_espada == "sim":
    Possui_espada = True
else:
    Possui_espada = False
Possui_armadura = input("Digite se vc tem armadura (sim ou nao): ")
if Possui_armadura == "sim":
    Possui_armadura = True
else:
    Possui_armadura = False

if Vida < 50 or Comida < 10:
    print("vc eh insuficiente")

if not Possui_espada:
    print("vc n tem espada")

if not Possui_armadura:
    print("vc n tem armadura")