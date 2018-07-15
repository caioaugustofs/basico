#Data: 2018-09-14


class Calcula_Gasto_De_Energia(object):

    def __init__(self, lista, dias, horas, valor_KW):
        self.lista = lista
        self.dias = dias
        self.horas = horas
        self.valor_KW = valor_KW

    def calculaConsumoEletricaParaVariasLampadas(self):

        def soma(lista):

            if type(lista) == tuple:
                return sum(lista)

            else:
                return lista

        self.somaWatts = soma(self.lista)
        self.totalKWattsMes = (self.somaWatts * (self.dias * self.horas)) / 1000
        self.gasto = self.totalKWattsMes * self.valor_KW

        return self.gasto
