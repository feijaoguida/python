print('\t ----Multiplos de 5 não divisiveis por 7 ---- ')

for num in range(5, 100):
    if (num % 5 == 0 and num % 7 != 0):
        print(num)
