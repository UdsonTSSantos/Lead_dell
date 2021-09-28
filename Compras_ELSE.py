compras = ['arroz', ' carne', 'leite', 'farinha']
print('Sua lista de compras possui os seguintes itens: ', len(compras), compras)
item = input('Qual item deseja adicionar? ')
if not (item in compras):
    compras.append(item)
    print("Foi adicionado na lista de compras o item: " + item)
    print("Agora sua lista de compras possui: ", len(compras), " itens, sendo eles ", compras)
else:
    print("Sua lista de compras já possui o item ", item)
print("FIM DO CÓDIGO")