print('\t ----Cálculo do novo salário ---- ')

""" Salário atual	Reajuste
Abaixo de R$500,00	15%
de R$500,00 até R$1000,00	10%
Acima de R$1000,00	5% """

salario_atual = float(input('Informe o salario atual: '))

if (salario_atual < 500):
    salario_novo = salario_atual+(salario_atual*0.15)
    print('Salario com reajuste =', salario_novo)

if ((salario_atual >= 500) and (salario_atual <= 1000)):
    salario_novo = salario_atual+(salario_atual*0.10)
    print('Salario com reajuste =', salario_novo)

if (salario_atual > 1000):
    salario_novo = salario_atual+(salario_atual*0.05)
    print('Salario com reajuste =', salario_novo)
