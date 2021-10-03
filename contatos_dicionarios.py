contatos = {}
ctt = {}
print('---- Adição de mais um contato ---')
ctt['nome'] = input('Digite o nome do contato por favor: ')
ctt['telefone'] = input('Digite o telefone: ')
ctt['email'] = input('Digite o e-mail do contato: ')
inicial = ctt['nome'][0].upper()
if inicial not in contatos:
    contatos[inicial] = []
contatos[inicial].append(ctt)
print('Nome: {}\tTelefone: {}\tE-mail: {}'.format(ctt['nome'], ctt['telefone'], ctt['email']))

