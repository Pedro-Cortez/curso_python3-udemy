from random import randint

cpf_9digitos = []
cpf_completo = []
sequencia = []
cont = 0

for cont in range(0, 9):
    numero = randint(0, 9)
    sequencia.append(numero)

cpf_9digitos = sequencia.copy()
print(cpf_9digitos)

# Cálculo do 10º dígito do CPF:

soma_geral_digitos = 0
fator_multiplicao_digito10 = 10

for digito_10 in cpf_9digitos:
    produto = int(digito_10) * fator_multiplicao_digito10
    soma_geral_digitos += produto
    fator_multiplicao_digito10 -= 1

multiplicao_10 = soma_geral_digitos * 10
resto11_digito10 = multiplicao_10 % 11

if resto11_digito10 > 9:
    num_cpf_10 = 0
    cpf_9digitos.append(num_cpf_10)
    print(f'O 10º dígito do CPF fornecido é {num_cpf_10} (zero).')
else:
    num_cpf_10 = resto11_digito10
    cpf_9digitos.append(num_cpf_10)
    print(f'O 10º dígito do CPF fornecido é {num_cpf_10}')

#Cálculo do 11º dígito do CPF:

soma_geral_digito11 = 0
fator_multiplicao_digito11 = 11

for digito_11 in cpf_9digitos:
    produto_digito11 = int(digito_11) * fator_multiplicao_digito11
    soma_geral_digito11 += produto_digito11
    fator_multiplicao_digito11 -= 1

multiplicacao10_digito11 = soma_geral_digito11 * 10
resto11_digito11 = multiplicacao10_digito11 % 11

if resto11_digito11 > 9:
    num_cpf_11 = 0
    cpf_9digitos.append(num_cpf_11)
    print(f'O 11º dígito do CPF fornecido é {num_cpf_11} (zero).')
else:
    num_cpf_11 = resto11_digito11
    cpf_9digitos.append(num_cpf_11)
    print(f'O 11º dígito do CPF fornecido é {num_cpf_11}\n')

#Apresentação do CPF gerado:

cpf_completo = cpf_9digitos.copy()

for digito in cpf_completo:
    print(f'{digito}', end='')
