from datetime import date


class Plano:
    def __init__(self,aluno,valor,data_inicio,data_vencimento,status):
        self.__aluno=aluno
        self.__valor=valor
        self.__data_inicio=data_inicio
        self.__data_vencimento=data_vencimento
        self.__status=status




    @property
    def aluno(self):
        return self.__aluno

    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self.__data_inicio = data_inicio

    @property
    def data_vencimento(self):
        return self.__data_vencimento

    @data_vencimento.setter
    def data_vencimento(self, data_vencimento):
        self.__data_vencimento = data_vencimento

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def esta_ativo(self):
        return self.__data_vencimento >= date.today()
