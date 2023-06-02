import random

# Lista de palavras
cores = ["azul", "vermelho", "amarelo"]
frutas = ["banana", "morango", "maçã"]
animais = ["cachorro", "gato", "elefante"]

# Função para selecionar uma palavra aleatória do tema escolhido
def selecionar_palavra(tema):
    if tema == 1:
        return random.choice(cores)
    elif tema == 2:
        return random.choice(frutas)
    elif tema == 3:
        return random.choice(animais)

# Função principal do jogo
def jogo_da_forca():
    tema = int(input("Escolha um tema:\n1. Cores\n2. Frutas\n3. Animais\n\nDigite o número correspondente ao tema desejado: "))
    palavra = selecionar_palavra(tema)
    palavra = palavra.lower()
    letras_erradas = []
    tentativas = 6
    palavra_oculta = "_" * len(palavra)

    print("\nVamos começar! A palavra tem", len(palavra), "letras.\n")

    # Loop principal do jogo
    while True:
        # Imprime as letras já adivinhadas corretamente e oculta as não adivinhadas
        print(" ".join(palavra_oculta) + "\n")

        # Verifica se todas as letras foram adivinhadas
        if "_" not in palavra_oculta:
            print("Parabéns meu nobre! Você desvendou a palavra:", palavra)
            break

        # Verifica se o jogador perdeu todas as tentativas
        if tentativas == 0:
            print("Poxa que pena, perdeu playboy! A palavra era:", palavra)
            break

        # Solicita uma nova letra ao jogador
        letra = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi tentada antes
        if letra in letras_erradas or letra in palavra_oculta:
            print("Você já tentou essa letra antes. Tente outra vez.")
            continue

        # Verifica se a letra está presente na palavra
        if letra in palavra:
            print("Letra correta!")
            # Atualiza a palavra oculta com a letra correta adivinhada
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta = palavra_oculta[:i] + letra + palavra_oculta[i + 1:]
        else:
            print("Letra errada!")
            letras_erradas.append(letra)
            tentativas -= 1

        # Imprime o número de tentativas restantes
        print("Tentativas restantes:", tentativas)

# Executa o jogo da forca
jogo_da_forca()
