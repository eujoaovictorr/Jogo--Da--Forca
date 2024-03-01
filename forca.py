import random
lista = ['carro', 'python', 'goiaba', 'gonorreia', 'batman','ornintorrinco', 'moto', 'cachoeira']

palavra = random.choice(lista)
for x in range(0):
    print()
digitadas = []
acertos = []
erros = 0
print('-' * 33)
print("SEJAM BEM VINDOS AO JOGO DA FORCA")
print('-' * 33)
print()
print("| ----- ")
print("|     |   ")
print("|        ")
print("|        ")
print("|        ")
print("| ______________")
print()

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "_ "
    print(senha)
    if senha == palavra:
        print("Você Ganhou!")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
            if erros == 0:
                print()
                print("| ----- ")
                print("|     |   ")
                print("|        ")
                print("|        ")
                print("|        ")
                print("| ______________")
                print()

            elif erros == 1:
                print()
                print("| -----  ")
                print("|     |   ")
                print("|     O  ")
                print("|         ")
                print("|         ")
                print("| ______________")
                print()

            elif erros == 2:
                print()
                print("| -----   ")
                print("|     |    ")
                print("|     O   ")
                print("|     |    ")
                print("|          ")
                print("| ______________")
                print()

            elif erros == 3:
                print()
                print("| -----   ")
                print("|     |    ")
                print("|     O   ")
                print("|    /|    ")
                print("|          ")
                print("| ______________")
                print()

            elif erros == 4:
                print()
                print("| -----   ")
                print("|     |    ")
                print("|     O   ")
                print("|    /|\   ")
                print("|          ")
                print("| ______________")
                print()

            elif erros == 4:
                print()
                print("| -----   ")
                print("|     |    ")
                print("|     O   ")
                print("|    /|\   ")
                print("|     |    ")
                print("| ______________")
                print()

            elif erros == 5:
                print()
                print("| -----   ")
                print("|     |    ")
                print("|     O  ")
                print("|    /|\   ")
                print("|     |    ")
                print("| ______________")
                print()

            elif erros == 6:
                print()
                print("| -----   ")
                print("|     |    ")
                print("|     O   ")
                print("|    /|\   ")
                print("|     |    ")
                print("|    /     ")
                print("| ______________")
                print()

            elif erros == 7:
                print()
                print("| -----   ")
                print("|     |    ")
                print("|     O   ")
                print("|    /|\   ")
                print("|     |    ")
                print("|    / \   ")
                print("| ______________")
                print()
            else:
                print("VOCÊ PERDEU")
                break