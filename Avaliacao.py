# elementos = ['Água', 'Fogo', 'Terra', 'Ar']
# elementos[3] = 'Metal'
# elementos.insert(1, 'Éter')
# elementos.pop(2)
# print(elementos)


# ========================================================================

# numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
# sequencia = numeros[1:11:3]
# print(sequencia)
# =========================================================================
# mala = [
#    'sabonete', 'xampu',
#    'camisas', 'roupas de baixo'
# ]
# print(mala.index('toalha'))

# ===========================================================================
# calculo = [3, 5, 7]*2 + [2]*3
# print(calculo)

#  ==========================================================================

livros = [
    'A Guerra dos tronos',
    'A Sociedade do Anel',
    'A Batalha do Apocalipse',
    'A Torre Negra',
    'O Castelo das Águias',
    'Os Cavaleiros do inverno'
]
paginas = [766, 694, 423, 586, 872, 171, 729]
livros_sel = []
paginas_sel = []
for i in livros:
    if 500 <= paginas(i) <= 750:
        livros_sel.append(livros[i])
        paginas_sel.append(paginas[i])
        print(livros_sel)