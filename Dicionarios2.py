mensagem = input('Digite uma string qualquer: ')
ocorrencias = {}
for letra in mensagem:
    ocorrencias[letra] = ocorrencias.get(letra, 0) + 1 # método get() com dois parâmetros
    print('A mensagem digitada possui: {} caracteres, sendo {} caracteres únicos.'.format(len(mensagem), len(ocorrencias)))
    print('Cada um destes caracteres únicos ocorreu: ')
    for letra in sorted(ocorrencias):
        print("\t'{}' ocorreu {} vezes. ".format(letra, ocorrencias[letra]))

