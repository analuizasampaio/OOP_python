# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Ana Luiza B Sampaio A
# ALUNO 2: Ingrid Priscila Alves de Sousa
# ALUNO 3: Guilherme Portes Bebiano
# ALUNO 4: Nailton Cerqueira de Paixão
# ALUNO 5: Eliel Americo de Oliveira
# ALUNO 6: Pedro Fernandes Klein


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
