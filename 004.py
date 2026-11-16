# Lista de números (notas) apresentada no slide
notas = [10, 3, 5]

# Exibe a lista completa de notas
print(f"Lista de notas: {notas}")

# Acedendo individualmente aos itens utilizando os índices
print(f"O valor 10 corresponde a notas[0]: {notas[0]}")
print(f"O valor 3 corresponde a notas[1]: {notas[1]}")
print(f"O valor 5 corresponde a notas[2]: {notas[2]}")

print("\n--- Percorrendo a lista com o for ---")
# Utilizando o for para percorrer os itens e calcular a média ou exibir
soma = 0
for i in range(len(notas)):
    print(f"Nota na posição {i}: {notas[i]}")
    soma = soma + notas[i]

# Calculando a média das notas
media = soma / len(notas)
print(f"\nA soma total das notas é {soma}")
print(f"A nota final (média) é {media}")

# Pede ao utilizador para procurar por uma nota específica
pesquisa = int(input("\nQue nota deseja procurar na lista? "))

# Verifica se a nota está presente na lista
if pesquisa in notas:
    print(f"A nota {pesquisa} está presente na lista de notas!")
else:
    print(f"A nota {pesquisa} não está na lista. As notas disponíveis são {notas}")