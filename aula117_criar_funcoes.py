def multiplicar(multiplicador):
    def operacao (fator):
        return fator * multiplicador
    return operacao

numero = int(input('Informe um número inteiro: '))
multiplo = int(input('Informe em quantas vezes deseja multiplicar o número informado: '))
execucao = multiplicar(multiplo)
print('-=' * 35)
print(f'O resultado é {execucao(numero)}')
