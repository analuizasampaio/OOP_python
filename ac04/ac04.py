# PROGRAMAÇÃO ORIENTADA A OBJETOS
# ATIVIDADE CONTÍNUA 04

# ALUNO 1: Ana Luiza B Sampaio A
# ALUNO 2: Ingrid Priscila Alves de Sousa
# ALUNO 3: Guilherme Portes Bebiano
# ALUNO 4: Charles Eduardo Felipe de Souza
# ALUNO 5: Eliel Americo de Oliveira
# ALUNO 6: Pedro Fernandes Klein


from abc import ABC, abstractmethod


class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, casa):
        self.casas.append(casa)


class Casa:
    def __init__(self, nome, animal):
        self.nome = nome
        self.animal = animal
        self.diretor = None
        self.monitor = None

    def set_diretor(self, diretor):
        self.diretor = diretor

    def get_diretor(self):
        return self.diretor

    def set_monitor(self, monitor):
        self.monitor = monitor

    def get_monitor(self):
        return self.monitor


class Disciplina:
    def __init__(self, nome, ementa):
        self.nome = nome
        self.ementa = ementa


class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []

    @abstractmethod
    def incluir_disciplina(self, disciplina):
        pass


class Professor(Pessoa):
    def __init__(self, nome, nascimento):
        super().__init__(nome, nascimento)

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Aluno(Pessoa):
    def __init__(self, nome, nascimento, tipo):
        super().__init__(nome, nascimento)
        self.tipo = tipo
        self.casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def set_casa(self, casa):
        self.casa = casa

    def incluir_triunfo(self, pontos):
        self.__triunfos += pontos

    def incluir_mau_feito(self, pontos):
        self.__mau_feitos += pontos

    def get_triunfos(self):
        return self.__triunfos

    def get_mau_feitos(self):
        return self.__mau_feitos


class Torneio:
    def __init__(self, casa1, casa2):
        self.casa1 = casa1
        self.casa2 = casa2
        self.__pontos_casa1 = 0
        self.__pontos_casa2 = 0

    def marcar_ponto(self, casa, quantidade):
        if casa == self.casa1:
            self.__pontos_casa1 += quantidade
        else:
            self.__pontos_casa2 += quantidade

    def get_pontos_casa1(self):
        return self.__pontos_casa1

    def get_pontos_casa2(self):
        return self.__pontos_casa2
