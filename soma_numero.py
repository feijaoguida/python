print('\t ---- Soma Numeros até o numero Digitado ---- ')

soma_numeros = 0

numero = int(input("Por favor, insira um número: "))

for i in range(1, numero + 1, 1):
    soma_numeros += i

print("A soma é = ", soma_numeros)
