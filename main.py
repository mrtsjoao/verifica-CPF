cpfUsuario = input('Informe um CPF: ').replace(".", "").replace("-", "")

noveDigitos = cpfUsuario[:9]

verificaPrimeiroDigito = 0
verificaSegundoDigito = 0

#Verificando o primeiro digito

for i, numero in enumerate(noveDigitos):
    verificaPrimeiroDigito += int(numero) * (10 - i)

verificaPrimeiroDigito = (verificaPrimeiroDigito * 10) % 11

primeiroDigito = verificaPrimeiroDigito if verificaPrimeiroDigito < 9 else 0

#Verificando o segundo digito

dezDigitos = noveDigitos + str(primeiroDigito)

for j, numero in enumerate(dezDigitos):
    verificaSegundoDigito += int(numero) * (10 - i)

verificaSegundoDigito = (verificaSegundoDigito * 10) % 11

segundoDigito = verificaSegundoDigito if verificaSegundoDigito < 9 else 0

#Compara o CPF enviado pelo usuário com o CPF "gerado" pelo algoritmo para validar

cpfNovo = f'{noveDigitos}{primeiroDigito}{segundoDigito}' #CPF gerado pelo algorítmo

if cpfUsuario == cpfNovo:
    print('CPF válido')
else:
    print('CPF inválido')
