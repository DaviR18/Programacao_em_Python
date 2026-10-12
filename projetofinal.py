print("Faça sua fixa de personagem:")
Nome = input("Digite seu nome: ")
Idade = input("Digite sua idade: ")
Inventario = []
Vida = 100.0
qnt_de_moeda = 30
Possui_espada = False
derrotar_boss = False

def decicao(mensagem):
    while True:
        try:
            escolha = int(input(mensagem))
            if escolha in [1, 2]:
                return escolha
            print("Digite apenas 1 ou 2.")
        except ValueError:
            print("Digite um número válido.")

print("vc encontou um mercador oferecendo uma espada por 20 moedas.")
comprar = decicao("Digite 1 pra comprar e 2 Guardar o ouro: ")

if comprar == 1:
    if qnt_de_moeda >= 20:
        qnt_de_moeda -= 20
        Possui_espada = True
        Inventario.append("Espada")
    else:
        print("vc n tem moedas suficientes, n comprou a espada")

def status(nome, vida, ouro, possedeespada, inventario):
    print("Seus status sao:")
    print(f"Nome: {nome}")
    print(f"Vida: {vida}")
    print(f"Quantos Ouros vc tem: {ouro}")
    print(f"Vc possui espada: {possedeespada}")
    print(f"Seu Inventario tem {inventario}")

status(Nome, Vida, qnt_de_moeda, Possui_espada, Inventario)

Lista4 = ["Winterfall", "Estrada Real", "Floresta", "Porto Real"]

def verificar_Lista(lista):
    global Possui_espada, Vida, derrotar_boss
    if lista == "Winterfall":
        return "tu ta no inverno, siga pra estrada real"
    elif lista == "Estrada Real":
        print("vc chegou na Estrada Real e um bandido apareceu")
        escolha_do_jogador = decicao("Digite 1 pra Lutar e 2 Fugir: ")
        if escolha_do_jogador == 1 and Possui_espada == True:
            print("vc derrotou o bandido, mas perdeu 20 de vida")
            Vida -= 20
        elif escolha_do_jogador == 1 and Possui_espada == False:
            print("vc apanhou do bandido, perdeu 40 de vida, mas conseguiu fugir")
            Vida -= 40
        else:
            print("vc conseguiu fugir")
        return "vc entao foi pra floresta"
    elif lista == "Floresta":
        print("vc chegou na Floresta e achou uma pocao")
        Inventario.append("Pocao")
        escolha_beber = decicao("Digite 1 pra beber e 2 pra nao beber: ")
        if escolha_beber == 1:
            print("vc bebeu e morreu, perdeu 100 de vida")
            Vida -= 100
        else:
            print("vc n bebeu e encontrou uma caminhonete branca q o levou para o porto real")
        return " "
    elif lista == "Porto Real":
        print("vc chegou no porto real e vai enfrentar um boss final em uma grande batalha final")
        escolha_do_jogador_no_boss = decicao("Digite 1 pra Lutar e 2 Fugir: ")
        if escolha_do_jogador_no_boss == 1 and Vida > 30:
            print("vc derrotou o boss, mas perdeu 20 de vida")
            Vida -= 20
            derrotar_boss = True
        else:
            print("vc fugiu")
        return "sua jornada terminou"

for i in Lista4:
    mensagem = verificar_Lista(i)
    print(mensagem)
    if Vida <= 0:
        break

print("status final:")
status(Nome, Vida, qnt_de_moeda, Possui_espada, Inventario)

if Vida <= 0:
    print("vc perdeu")
elif derrotar_boss == True:
    print("vc venceu")
else:
    print("vc sobreviveu")