import random

def jogarAdivinhacao():
    print("############################################")
    print("# Jogo de adivinhação de número            #")
    print("############################################")

    numeroMagico = int(random.randrange(0, 101))
    pontos = 1000

    tentativasDificuldade = [20, 10, 5]

    def perguntarDificuldade():
        print("Insira uma das dificuldade: ")
        print("(1): Fácil")
        print("(2): Médio")
        print("(3): Difícil")
        dificuldade = input(": ")
        return dificuldade

    totalDeTentativas = 0

    while(totalDeTentativas == 0):
        d = perguntarDificuldade()

        if int(d) in range(1,4):
            totalDeTentativas = tentativasDificuldade[int(d)-1]
        else:
            print(d)
            print("retorne um valor válido.")

    for i in range(totalDeTentativas):
        print("\n\nTentativa {} de {} \n".format(i+1, totalDeTentativas))
        print("Insira um número entre 0 à 100.")
        n = int(input(": "))
        
        if(n not in range(0, 101)):
            print("Você deve colocar um número válido entre 0 à 100!")
            continue

        if(n == numeroMagico):
            print("Você acertou, Parabéns! Sua pontuação foi: {}".format(pontos))
            break
        elif(n < numeroMagico):
            print("O número inserido é menor que o número certo")
        else:
            print("O número inserido é maior que o número certo")
        
        pontos -= abs(numeroMagico - n)

if(__name__ == "__main__"):
    jogarAdivinhacao()