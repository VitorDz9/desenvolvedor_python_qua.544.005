class Motor:
    def __init__(self,potencia):
        self.__potencia = potencia


    @property
    def potencia(self):
        return self.potencia

    @potencia.setter
    def potencia(self,potencia):
        self.__potencia= potencia

    def Info(self):
        return f"Potência: motor de {self.__potencia} cv."

class Carro:
    def __init__(self,fabricante,modelo,ano,cor,potencia):
        self.__fabricante=fabricante
        self.__modelo=modelo
        self.__ano=ano
        self.__cor=cor
        self.motor = Motor(potencia)#composição

    @property
    def fabricante(self):
        return self.__fabricante


    @fabricante.setter
    def fabricante(self,fabricante):
        self._fabricante=fabricante

    @property
    def modelo(self):
        return self.__modelo


    @modelo.setter
    def modelo(self,modelo):
        self._modelo=modelo


    @property
    def ano(self):
        return self.__ano


    @ano.setter
    def ano(self,ano):
        self._ano=ano

    @property
    def cor(self):
        return self.__cor


    @cor.setter
    def cor(self,cor):
        self.cor=cor

    def exibir_detalhes(self):
        return f"Fabricante: {self.__fabricante}\nModelo: {self.__modelo}\nAno: {self.__ano}\nCor: {self.__cor}\nMotor: {self.__motor.info()}"
