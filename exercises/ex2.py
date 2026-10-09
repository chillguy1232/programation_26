import sys
sys.stdout.reconfigure(encoding="utf-8")

print ("olá, escreva dois números:")

numero_1 = int(input("número 1:"))
numero_2 = int(input("número 2:"))
resultado = numero_1 + numero_2

if type(numero_1).__name__ == 'str':
    print(f"{numero_1} é uma string")

print ("a soma dos dois números recebidos é", resultado)
print (numero_1, "+", numero_2, "=", resultado)