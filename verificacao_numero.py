print("=== VERIFICAÇÃO DE NÚMERO ===")

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("O número é positivo.")

elif numero < 0:
    print("O número é negativo.")

else:
    print("O número é zero.")

if numero % 2 == 0:
    print("O número é par.")

else:
    print("O número é ímpar.")
