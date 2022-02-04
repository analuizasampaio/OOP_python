# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Ana Luiza B Sampaio A
# ALUNO 2: Ingrid Priscila Alves de Sousa
# ALUNO 3: Guilherme Portes Bebiano
# ALUNO 4: Charles Eduardo Felipe de Souza
# ALUNO 5: Eliel Americo de Oliveira
# ALUNO 6: Pedro Fernandes Klein


class Socio:
    def __init__(self, nome, nascimento, cpf, mes, ano):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.mes = mes
        self.ano = ano


class Clube:
    def __init__(self):
        self.socios = []
    
    def associar(self, socio):
        self.socios.append(socio)
    
    def numero_de_socios(self):
        return len(self.socios)
    
    def mes_associacao(self, mes, ano):
        if mes < 1 or mes > 12:
            raise ValueError
        if len(str(ano)) != 4:
            raise TypeError

        result = []
        for socio in self.socios:
            if socio.mes == mes and socio.ano == ano:
                result.append(socio.nome)

        return len(result)

    def expulsar(self, mes, ano):
        if mes < 1 or mes > 12:
            raise ValueError
        if len(str(ano)) != 4:
            raise TypeError

        expulsos = []
        for socio in self.socios:
            if socio.mes == mes and socio.ano == ano:
                expulsos.append(socio.nome)
        expulsos.sort()
        
        socios_restantes = [socio for socio in self.socios if socio.nome not in expulsos]
        self.socios = socios_restantes
        
        return tuple(expulsos)
