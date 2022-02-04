# ATIVIDADE CONTÍNUA 03

# NOMES DOS ALUNOS (máximo 6 alunos)
# ALUNO 1: Ana Luiza B Sampaio A
# ALUNO 2: Ingrid Priscila Alves de Sousa
# ALUNO 3: Guilherme Portes Bebiano
# ALUNO 4: Charles Eduardo Felipe de Souza
# ALUNO 5: Eliel Americo de Oliveira
# ALUNO 6: Pedro Fernandes Klein


class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria


class Personagem:
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = []

    def adicionar_super_poder(self, superpoder):
        if len(self.__poderes) == 4:
            raise ValueError
        else:
            self.__poderes.append(superpoder)

    def get_poder_total(self):
        total = [poder.get_categoria() for poder in self.__poderes]
        return sum(total)


class SuperHeroi(Personagem):
    def __init__(self, nome, nome_vida_real):
        super().__init__(nome, nome_vida_real)

    def get_poder_total(self):
        return super().get_poder_total() * 1.1


class Vilao(Personagem):
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao


class Confronto:
    def lutar(self, superheroi, vilao):
        poder_heroi = superheroi.get_poder_total()
        poder_vilao = vilao.get_poder_total()
        if poder_heroi > poder_vilao:
            return 1
        if poder_heroi < poder_vilao:
            return 2
        elif poder_heroi == poder_vilao:
            return 0
