import sys
sys.stdout.reconfigure(encoding="utf-8")
#comentário
'''
comentario de varias linhas

'''


nome =' Joseph_Florentino' 
print ("olá" + nome)

print(f"olá{nome},\nbem-vindo! ")

#receber dados de utilizador
nomealuno = input ("Qual o seu nome:")
dis_n = input("Escreve o nome de uma disciplina:")

print(f"olá{nomealuno},\nbem-vindo a {dis_n} ")

print("nome é do tipo: " + type(nome).__name__)
