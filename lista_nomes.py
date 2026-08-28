print("=== LISTA DE NOMES ===")

nomes = []

for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)

print("\nNomes cadastrados:")

for nome in nomes:
    print(nome)

print("\nQuantidade de nomes cadastrados:", len(nomes))

pesquisa = input("\nDigite um nome para pesquisar: ")

if pesquisa in nomes:
    print("O nome está na lista.")

else:
    print("O nome não está na lista.")
