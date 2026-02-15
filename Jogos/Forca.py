import random

def jogarForca():
    print("############################################")
    print("# Jogo da Forca                            #")
    print("############################################")

    enforcou = False
    acertou = False

    dicionario = open("dicionario.txt", "r")
    todasAsPalavras = []

    for linha in dicionario:
        todasAsPalavras.append(linha.strip())
    dicionario.close()

    palavra = todasAsPalavras[random.randrange(0, len(todasAsPalavras))].lower()
    
    letrasEscolhidas = []
    qntDeErros = 0

    while(not enforcou and not acertou):
        print("Digite uma letra:")
        escolha = input(": ").lower()
        if len(escolha) != 1:
            print("Só pode apenas um caráctere \n")
            continue
        if escolha in letrasEscolhidas:
            print("Você já colocou essa letra! \n")
            qntDeErros += 1
        if escolha not in palavra:
            print("A palavra não possui esse caráctere! \n")
            qntDeErros += 1

        enforcou = qntDeErros == 6
        qntDeAcertos = 0
        for i, letra in enumerate(palavra):
            if escolha == letra or letra in letrasEscolhidas:
                print("{} ".format(letra), end='')
                if escolha not in letrasEscolhidas:
                    letrasEscolhidas.append(escolha)
                qntDeAcertos += 1
            else:
                print("_ ", end='')

            if qntDeAcertos == len(palavra):
                print("\nVocê acertou a palavra!")
                acertou = True

        print("\n\n---------------------------------------------")

    print("jogo acabou.")

if(__name__ == "__main__"):
    jogarForca()