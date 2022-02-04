# --------------------------------------------------------------------------
# EXEMPLO DE PROGRAMA PRINCIPAL
# Utilize o trecho de programa a seguir para auxiliar nos testes das funĂ§Ăľes

from ac01 import pertence, substituir, posicoes, reprovados, excluir_nota, menor_nota

lista = [2, 3, 4, 8, 7]
resultado = pertence(lista, 3, 8)               	
print(resultado)                        # True           	
 
lista = [2, 3, 4, 8, 7]
resultado = pertence(lista, 3, 9)               	
print(resultado)                        # False

lista = [2, 3, 4, 8, 7]
resultado = pertence(lista, 5, 9)               	
print(resultado)                        # False

lista = [1, 2, 3, 2, 4]
resultado = substituir(lista, 2, 99)              	
print(resultado)                        # [1, 99, 3, 99, 4]
 
lista = [1, 2, 2, 4]
resultado = substituir(lista, 2, 'abc')         	
print(resultado)                        # [1, 'abc', 'abc', 4]

lista = [1, 2, 2, 4]
resultado = substituir(lista, 3, 9)         	
print(resultado)                        # [1, 2, 2, 4]

tupla = (1, 2, 3, 4, 5)
resultado = posicoes(tupla, 2)                
print(resultado)                        # [1]

tupla = (2, 1, 2, 3, 2)
resultado = posicoes(tupla, 2)                
print(resultado)                        # [0, 2, 4]

tupla = (2, 1, 2, 3, 2)
resultado = posicoes(tupla, 5)                
print(resultado)                        # []

alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
          'Denise': [9.0, 8.5],
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = reprovados(alunos)			
print(resultado)                        # ['Augusto', 'Ana Paula']

alunos = {'Augusto': [10, 8.0, 7.0],
          'Denise': [9.0, 8.5],
          'Ana Paula': [8.0, 9.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = reprovados(alunos)			
print(resultado)                        # []

alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0], 
          'Denise': [9.0, 8.5], 
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = excluir_nota(alunos, 'Denise')        	
print(resultado)                        # {'Augusto': [4.5, 7.0, 6.0, 3.0], 
                                        #  'Denise': [8.5], 
                                        #  'Ana Paula': [3.5, 1.0, 6.5], 
                                        #  'Marcelo': [9.0, 10.0, 7.0, 7.0]}

alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0], 
          'Denise': [9.0, 8.5], 
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = excluir_nota(alunos, 'Marcelo')        	
print(resultado)                        # {'Augusto': [4.5, 7.0, 6.0, 3.0], 
                                        #  'Denise': [9.0, 8.5], 
                                        #  'Ana Paula': [3.5, 1.0, 6.5], 
                                        #  'Marcelo': [10.0, 7.0, 7.0]}

alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0], 
          'Denise': [9.0, 8.5], 
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = excluir_nota(alunos, 'JoĂŁo')        	
print(resultado)                        # {'Augusto': [4.5, 7.0, 6.0, 3.0], 
                                        #  'Denise': [9.0, 8.5], 
                                        #  'Ana Paula': [3.5, 1.0, 6.5], 
                                        #  'Marcelo': [9.0, 10.0, 7.0, 7.0]}

alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0], 
          'Denise': [9.0, 8.5], 
          'Ana Paula': [3.5, 1.0, 6.5],
          'Marcelo': [9.0, 10.0, 7.0, 7.0]}
resultado = menor_nota(alunos) 
print(resultado)                        # {'Augusto': 3.0,                
                                        #  'Denise': 8.5,
                                        #  'Ana Paula': 1.0,
                                        #  'Marcelo': 7.0}
