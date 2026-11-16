# Dicionário com os itens do cardápio e os respectivos preços
cardapio_precos = {
    'pizza': 10,
    'suco': 5,
    'bolo': 7,
    'refrigerante': 8
}

# Exibe os itens do cardápio inicial e os preços
print("Itens do cardápio e preços:")
for item, preco in cardapio_precos.items():
    print(f"Item: {item} - Preço R${preco}")

# Calcula o valor total do cardápio somando os preços
valor_total = sum(cardapio_precos.values())
print(f"Valor total do cardápio R${valor_total}")

# Pede ao utilizador para escolher o que quer comer
escolha = input("O que você quer comer hoje? ")

# Verifica se a escolha está presente no dicionário do cardápio
if escolha in cardapio_precos:
    print(f"Ótima escolha! Saindo um(a) {escolha} no valor de R${cardapio_precos[escolha]}.")
else:
    # Cria uma lista com as chaves para mostrar caso o item não exista
    lista_cardapio = list(cardapio_precos.keys())
    print(f"{escolha} não está no cardápio, que tal você pedir {lista_cardapio}")