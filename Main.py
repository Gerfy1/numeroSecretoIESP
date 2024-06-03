import random;
print("Bem vindo ao jogo de numero secreto!\n"
      "O numero secreto está entre 0 e 10.\n"
      "Você terá 3 tentativas para acertar o numero.\n");
gerarNumeroSecreto = random.randint(0, 10)
maxTentativas = 3
tentativas = 0
while tentativas < maxTentativas:
    try:
        numeroDigitado = int(input("Digite o numero secreto: "));
        tentativas += 1
        if numeroDigitado == gerarNumeroSecreto:
            print(f"Você acertou com !!\n O numero é secreto era: {gerarNumeroSecreto}");
            break;
        elif (numeroDigitado > gerarNumeroSecreto):
            print("O numero digitado é maior que o numero secreto.");
        elif (numeroDigitado < gerarNumeroSecreto):
            print("O numero digitado é menor que o numero secreto!");
        if tentativas == maxTentativas:
            print("Você atingiu o maximo de tentativas! O número secreto era: ",gerarNumeroSecreto);
        else:
            print(f"Você possui {maxTentativas - tentativas} tentativas.");
    except Exception as e:
        print("Valor digitado não é um numero, verifique e tente novamente.");
print("Fim de jogo!");
