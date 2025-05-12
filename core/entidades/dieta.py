class Dieta:
    def __init__(self,aluno,descricao):
        self.__aluno = aluno
        # self.__data_criacao = data_criacao
        self.__descricao = descricao

    @property
    def aluno(self):
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    # @property
    # def data_criacao(self):
    #     return self.__data_criacao
    #
    # @data_criacao.setter
    # def data_criacao(self, data_criacao):
    #     self.__data_criacao = data_criacao