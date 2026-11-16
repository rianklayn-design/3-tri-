
# Lista com os itens do cardápio
cardapio = ['pastel', 'pizza', 'coxinha']

# Exibe os itens do cardápio inicial
print(f"Itens do cardápio: {cardapio}")

# Adicionando um novo item ao cardápio usando .append()
cardapio.append("hambúrguer")
print(f"Cardápio após adicionar: {cardapio}")

# Removendo um item específico pelo nome usando .remove()
cardapio.remove("pastel")
print(f"Cardápio após remover: {cardapio}")

# Inserindo um item numa posição específica usando .insert() (ex: índice 0)
cardapio.insert(0, "suco")
print(f"Cardápio após inserir na posição 0: {cardapio}")

# Removendo um item por índice usando .pop() (ex: índice 1, que é a segunda posição)
cardapio.pop(1)
print(f"Cardápio após remover o item do índice 1 com .pop(): {cardapio}")

# Pede ao utilizador para escolher o que quer comer
escolha = input("O que você quer comer hoje? ")

# Verifica se a escolha está presente na lista do cardápio
if escolha in cardapio:
    print(f"Ótima escolha! Saindo um(a) {escolha}.")
else:
    print(f"{escolha} não está no cardápio, que tal você pedir {cardapio}")