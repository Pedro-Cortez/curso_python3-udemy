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

soma_geral_a = 0
fator_a = 10

for digito_a in cpf_9digitos:
    produto_a = int(digito_a) * fator_a
    soma_geral_a += produto_a
    fator_a -= 1

multi_10_a = soma_geral_a * 10
resto11_a = multi_10_a % 11

if resto11_a > 9:
    num_cpf_10 = 0
    cpf_9digitos.append(num_cpf_10)
    print(f'O 10º dígito do CPF fornecido é {num_cpf_10} (zero).')
else:
    num_cpf_10 = resto11_a
    cpf_9digitos.append(num_cpf_10)
    print(f'O 10º dígito do CPF fornecido é {num_cpf_10}')


soma_geral_b = 0
fator_b = 11

for digito_b in cpf_9digitos:
    produto_b = int(digito_b) * fator_b
    soma_geral_b += produto_b
    fator_b -= 1

multi_10_b = soma_geral_b * 10
resto11_b = multi_10_b % 11

if resto11_b > 9:
    num_cpf_11 = 0
    cpf_9digitos.append(num_cpf_11)
    print(f'O 11º dígito do CPF fornecido é {num_cpf_11} (zero).')
else:
    num_cpf_11 = resto11_b
    cpf_9digitos.append(num_cpf_11)
    print(f'O 11º dígito do CPF fornecido é {num_cpf_11}')

print()

cpf_completo = cpf_9digitos.copy()

for digito in cpf_completo:
    print(f'{digito}', end='')
