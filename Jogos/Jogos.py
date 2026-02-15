import Adivinhação
import Forca

print("############################################")
print("# Jogos do Alura                           #")
print("############################################")

jogoSelecionado = False

while not jogoSelecionado:
    print("Insira um dos seguintes jogos para jogar: ")
    print("(1): Adivinhação")
    print("(2): Forca")
    jogo = int(input(": ", ))

    if jogo == 1:
        Adivinhação.jogarAdivinhacao()
        jogoSelecionado = True
    elif jogo == 2:
        Forca.jogarForca()
        jogoSelecionado = True
    else:
        print("insira um valor válido!")