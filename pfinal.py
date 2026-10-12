print("Faça sua fixa de personagem:")
Nome = input("Digite seu nome: ")
Idade = input("Digite sua idade: ")
Inventario = []
Vida = 100
qnt_de_moeda = 30
Possui_espada = False



escolha_do_jogador = int(input("Digite 1 pra Lutar e 2 Fugir: "))

def decicao(escolha):
    if escolha > 2:
        escolha = int(input("Digite 1 pra Lutar e 2 Fugir: "))
        if escolha > 2 :
            decicao(escolha)
        return escolha
    else:
        return escolha

decicao(escolha_do_jogador)

def status(nome,vida,ouro,possedeespada,inventario):
    print("Seus status sao:")
    print(f"Nome: {nome}")
    print(f"Vida: {vida}")
    print(f"Quantos Ouros vc tem: {ouro}")
    print(f"Vc possui espada: {possedeespada}")
    print(f"Seu Inventario tem {inventario}")

status(Nome,Vida,qnt_de_moeda,Possui_espada,Inventario)

Lista4 = ["Winterfall", "Estrada Real", "Floresta", "Porto Real"]

def verificar_Lista(lista):
    if lista == "Winterfall":
        return "tu ta no inverno"
    elif lista == "Estrada Real":
        return "tu chegou na estrada real"
    elif lista == "Floresta":
        return "tu ta na floresta"
    elif lista == "Porto Real":
         return "tu chegou no porto real"

for i in Lista4:
    mensagem  = verificar_Lista(i)
    print(mensagem)