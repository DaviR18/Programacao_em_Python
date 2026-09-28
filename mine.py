inimigos = ["zumbi", "esqueleto", "aranha", "creeper", "boss"]
contador_de_creeper = 0
for i in range(len(inimigos)):
    if inimigos[i] == "zumbi":
        print("o inimigo eh zumbi")
        continue
    elif inimigos[i] == "esqueleto":
        print("o inimigo eh esqueleto")
    elif inimigos[i] == "esqueleto":
        print("o inimigo eh esqueleto")
    elif inimigos[i] == "aranha":
        print("o inimigo eh aranha")
    elif inimigos[i] == "creeper":
        print("o inimigo eh creeper")
        print("cuidado")
        contador_de_creeper += 1
    else:
        print("o inimigo eh boss")
        print("patrulha encerrada")
        break

print("a quantidade de creepers encontrados foi: ", contador_de_creeper)
    