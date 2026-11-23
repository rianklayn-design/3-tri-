# [2, 5, 3, 4, 1]
# [2, 3, 5, 4, 1]
# [2, 3, 4, 5, 1]
# [2, 3, 4, 1, 5]
# [2, 3, 1, 4, 5]
# [2, 1, 3, 4, 5]
# [1, 2, 3, 4, 5]

numeros = [5, 2]
print(numeros[0] > numeros[1])

numeros = [5 , 2]
if numeros[0] > numeros[1]:
    print("Precisa trocar")

numeros = [5, 2, 3]

for i in range(len(numeros) - 1):
    if numeros[i] > numeros[i + 1]:
        numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]

print(numeros) 

numeros = [5, 2, 3]

for i in range(len(numeros) - 1):
    if numeros[i] > numeros[i + 1]:
        numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
        print(numeros)

        numeros = [5, 2, 3, 4, 1]

for rodada in range(len(numeros)):
    for i in range(len(numeros) - 1):
        if numeros[i] > numeros[i + 1]:
            numeros[i], numeros[i + 1] = numeros[i + 1], numeros[i]
            print(numeros)

[2, 5, 3, 4, 1]
[2, 3, 5, 4, 1]
[2, 3, 4, 5, 1]
[2, 3, 4, 1, 5]
[2, 3, 1, 4, 5]
[2, 1, 3, 4, 5]
[1, 2, 3, 4, 5]
