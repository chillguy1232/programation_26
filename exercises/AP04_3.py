

'''
print (m1, "\n", m2)
'''
'''
print (f'ID:{m1["id"]}')
print (f'nome:{m1["nome"]}')
'''



'''
musicas.append(m1)
musicas.append(m2)
'''
m1 = {'id':1, 'nome': "bring me to life"}
m2 = {'id':2, 'nome': "faint" }

m1['estilo'] = 'rock'
m2['estilo'] = 'rock'

musicas = [m1, m2]


print(musicas)

for rock in musicas:
    print(rock)
    print (f'ID:{rock["id"]}')
    print (f'nome:{rock["nome"]}')
    print('estilo:{rock["estilo"]}')


musicas.append({'id': 3, 'nome': 'welcome to the pleasure dome', 'estilo': 'rock'})
for rock in musicas:
    print(rock)
    print (f'ID:{rock["id"]}')
    print (f'nome:{rock["nome"]}')
    print('estilo:{rock["estilo"]}')

for rock in musicas:
    if rock['estilo'] == 'rock':
     for chave, valor in rock.items():
        print(f'{chave}:{valor}')
