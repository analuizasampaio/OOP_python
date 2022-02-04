'''
Escreva uma função com o nome 'pertence', que recebe como argumentos de entrada
uma lista e dois itens e retorna True, se os dois itens estiverem
armazenado na lista, e False, caso contrário.
'''
def pertence(lista, item1, item2):
  if item1 in lista and item2 in lista:
    return True
  else:
    return False

'''
Escreva uma função chamada 'substituir' que recebe como argumentos de entrada uma
lista e dois itens (velho e novo) e retorna uma lista onde todas as ocorrências
do item velho são substituídas pelo item novo.
'''
def substituir(lista, velho, novo):
  for i in lista:
    if i == velho:
      aux = lista.index(i);
      lista[aux] = novo
  return lista


'''
Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada
uma tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''
def posicoes(tupla, item):
  if item not in list(tupla):
    return []
  resultado = []
  lista = list(tupla)
  for i in range(len(lista)):
    if lista[i] == item:
      resultado.append(i)
  return resultado


'''
Suponha um dicionario onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'reprovados' que recebe como argumentos de
entrada o dicionário e retorna uma lista com o nome dos alunos reprovados.
Considere que o aluno é reprovado se a média das suas notas é inferior a 6.
Caso nenhum aluno seja reprovado, deve retornar uma lista vazia.
'''
def reprovados(alunos):
  reprovados = []
  for chave in alunos:
    notas = alunos[chave]
    if sum(notas) / len(notas) < 6:
      reprovados.append(chave)
  return reprovados


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista de
notas. Escreva uma função chamada 'excluir_nota' que recebe como argumentos de
entrada o dicionário e o nome de um aluno. A função deve excluir a primeira
nota desse aluno e retornar o dicionário com as alterações realizadas.
Se o aluno não existir no dicionário, deve retornar o dicionário sem alterações.
'''
def excluir_nota(alunos, nome):
  if nome not in alunos:
    return alunos
    
  for chave in alunos:
    if chave == nome:
      alunos[chave].pop(0)
  return alunos


'''
Suponha um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada menor_nota que recebe como argumentos
de entrada o dicionário e retorna outro dicionário com o nome e a menor nota
de cada aluno.
'''
def menor_nota(alunos):
  lista = {}
  for chave in alunos:
    alunos[chave].sort()
    lista[chave] = alunos[chave][0]
  return lista

'''
 - - - - - - - - - - - - - - - - - - -
'''

#1
lista = [2, 3, 4, 8, 7]
resultado = pertence(lista, 3, 8)               	
print(resultado)                        # True
        	
lista = [2, 3, 4, 8, 7]
resultado = pertence(lista, 3, 9)               	
print(resultado)                        # False

#2
lista = [1, 2, 3, 2, 4]
resultado = substituir(lista, 2, 99)              	
print(resultado)                        # [1, 99, 3, 99, 4]

#3
tupla = (2, 1, 2, 3, 2)
resultado = posicoes(tupla, 2)                
print(resultado)                        # [0, 2, 4]

#4
alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
          'Denise': [9.0, 8.5],
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = reprovados(alunos)			
print(resultado)                        # ['Augusto', 'Ana Paula']

#5
alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0], 
          'Denise': [9.0, 8.5], 
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = excluir_nota(alunos, 'Denise')        	
print(resultado)                        
# {'Augusto': [4.5, 7.0, 6.0, 3.0], 
#  'Denise': [8.5], 
#  'Ana Paula': [3.5, 1.0, 6.5], 
#  'Marcelo': [9.0, 10.0, 7.0, 7.0]}

#6
alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0], 
          'Denise': [9.0, 8.5], 
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = menor_nota(alunos) 
print(resultado)                        
# {'Augusto': 3.0,                
#  'Denise': 8.5,
#  'Ana Paula': 1.0,
#  'Marcelo': 7.0}