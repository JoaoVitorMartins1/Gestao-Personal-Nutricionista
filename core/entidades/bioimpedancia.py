class Bioimpedancia():
    def __init__(self,data_medicao,peso,altura,pct_gordura,cintura,peito,coxa,panturrilha,braco,aluno):
        self.__data_medicao = data_medicao
        self.__peso = peso
        self.__altura = altura
        self.__pct_gordura = pct_gordura
        self.__cintura = cintura
        self.__peito = peito
        self.__coxa = coxa
        self.__panturrilha = panturrilha
        self.__braco = braco
        self.__aluno = aluno

    @property
    def data_medicao(self):
        return self.__data_medicao

    @data_medicao.setter
    def data_medicao(self, data_medicao):
        self.__data_medicao = data_medicao

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    @property
    def pct_gordura(self):
        return self.__pct_gordura

    @pct_gordura.setter
    def pct_gordura(self, pct_gordura):
        self.__pct_gordura = pct_gordura

    @property
    def cintura(self):
        return self.__cintura

    @cintura.setter
    def cintura(self, cintura):
        self.__cintura = cintura

    @property
    def peito(self):
        return self.__peito

    @peito.setter
    def peito(self, peito):
        self.__peito = peito

    @property
    def coxa(self):
        return self.__coxa

    @coxa.setter
    def coxa(self, coxa):
        self.__coxa = coxa

    @property
    def panturrilha(self):
        return self.__panturrilha

    @panturrilha.setter
    def panturrilha(self, panturrilha):
        self.__panturrilha = panturrilha

    @property
    def braco(self):
        return self.__braco

    @braco.setter
    def braco(self, braco):
        self.__braco = braco

    @property
    def aluno(self):
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno