cursos = ['Engenharia de software', 'Python para data Science', 'Introdução a Java']
respostas = [1, 2, 0, 1, 1, 1, 1, 0, 0, 2, 2, 0, 1, 1, 1, 1, 2, 0, 1, 1, 0, 1, 0, 2, 1, 1, 0, 2, 2, 1, 0, 1, 1, 0, 0, 0, 1, 1, 2, 1]
pessoas = len(respostas)
print('Quantida de colegas que responderam a sua pesquisa: ',pessoas)
respostas.sort()
print('Sequencia crescente das respostas: ', respostas)
print('=== RESULTADO DA VOTAÇÃO ====')
engenharia = respostas.count(0)
print('Engenharia recebeu ', engenharia, ' votos.')
python = respostas.count(1)
print('Python recebeu ', python, ' votos.')
java = respostas.count(2)
print('Java recebeu ', java, ' votos.')
votacao = (engenharia, python, java)
print('Pela votação, o número maior de votos foi: ', max(votacao))
print('FIM DO CÓDIGO')



