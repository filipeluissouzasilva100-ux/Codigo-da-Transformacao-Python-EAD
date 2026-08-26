import random

def jogar():
    numero_secreto = random.randint(1, 24)
    max_tentativas = 6

    print("=" * 40)
    print("       JOGO DA ADIVINHAÇÃO")
    print("=" * 40)
    print("Tente adivinhar o número de 1 a 24.")
    print(f"Você tem {max_tentativas} tentativas.")
    print()

    for tentativa in range(1, max_tentativas + 1):

        try:
            palpite = int(input(
                f"Tentativa {tentativa}/{max_tentativas} - Digite seu palpite: "
            ))
        except ValueError:
            print("Digite apenas um número!")
            continue

        if palpite < 1 or palpite > 24:
            print("Digite um número entre 1 e 24.")
            continue

        if palpite == numero_secreto:
            print()
            print("🎉 PARABÉNS! VOCÊ ACERTOU!")
            print(f"Você acertou em {tentativa} tentativa(s).")
            break

        elif palpite < numero_secreto:
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")

        print()

    else:
        print()
        print("😢 FIM DE JOGO!")
        print(f"O número secreto era: {numero_secreto}")


if __name__ == "__main__":
    jogar()