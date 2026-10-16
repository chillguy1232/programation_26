
'''
print("escreva o seu nome: ")
nome = input("nome:")

print("o seu nome é: ", nome)

print ("agora um número: ")
numero = int(input("número:"))
 #o input serve para obter um valor do utilizador, o igual guarda o valor da váriavel
print ("seu número é: ", numero)
'''



'''
print(f'valor inserido: {guess}, do tipo({type(guess).__name__})')
print(f'{guess.isnumeric()} ;{guess.isdecimal()}')
'''

import random
lmin,lmax = 1,100 
numbertoguess = random.randint(lmin,lmax)
guess = ""
attempt = 0
while (guess != numbertoguess):
    guess = input(f"adivinha o número entre {lmin} and {lmax}: ")
    if (guess.isnumeric()):
        guess = int(guess)
        print(f"numero inserido: {guess}")
        if (guess > numbertoguess):
            print("mais baixo")
        elif (guess < numbertoguess):
            print ("mais alto")
        else:
            print ("acertou")
        attempt += 1
       
    else:
        print(f"{guess} não é um número inteiro")
if (guess =='end'):
    print(f"desistiu ao fim de{attempt} tentativas")

else:
    print ("número de tentativas", attempt)
