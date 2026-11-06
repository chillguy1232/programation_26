import math
import random

guess = ""
attempt = 0
tentativas = []

lmin,lmax = 1,100 
numbertoguess = random.randint(lmin,lmax)
guess = ""


attempt = 0
while (guess != numbertoguess):
    guess = input(f"adivinha o número entre {lmin} and {lmax}: ")
    guess = guess.strip()

  

    try:
        guess = int(guess)
        if (guess > numbertoguess):
            print("mais baixo")
        elif (guess < numbertoguess):
            print ("mais alto")
        else:
            print ("acertou")
        


    except Exception as ex:
        if (guess != 'end'):
            print(f"{guess} não é um número inteiro: {type(ex).__name__}: {ex}")
    finally:
        print((f'valor inserido: {guess} a tentativa {attempt}ª'))
        attempt += 1
        tentativas.append(guess)
#fim do while


if (guess =='end'):
    print(f"desistiu ao fim de{attempt} tentativas")

else:
    print ("número de tentativas", attempt)
