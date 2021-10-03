populacao = {'Ceará':9132078, 'Bahia':14873064, 'Alagoas':3337045 }
print('O Ceará possui {} habitantes.'.format(populacao['Ceará']))

populacao['Maranhão'] = 7075181
print(populacao)

for chave, valor in populacao.items():
    print('O {} possui {} habitantes.'.format(chave, valor))

del populacao['Maranhão']
print(populacao)

print('O estado de Alagoas é muito pequeno em comparação ao estado de Minas gerais, a população de Alagoas é de: {}'.format(populacao.get('Alagoas')))

estado = input('De qual estado você quer saber a população? ')
pop = populacao.get(estado)
if pop == None:
    print('Infelizmente não sabemos informar a população deste estado: ',estado)
else:
    print('{} possui {} habitantes.'.format(estado, pop))


print('Escolha entre os estados:' + ','.join(populacao.keys()))

populacao['Maranhão'] = 4562366
print('Escolha entre os estados:' + ','.join(populacao.keys()))

for estado in sorted(populacao):
    print('{} possui {} habitantes.'.format(estado, populacao[estado]))

print('======= Usando lambda =======')


for estado in sorted(populacao, key=lambda chave : populacao.get(chave)):
    print('{} possui {} habitantes.'.format(estado, populacao[estado]))

