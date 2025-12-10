from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, entrada: int):
        self.id = id
        self.tipo = tipo
        self.entrada = entrada

    @abstractmethod
    def calcularValor(self):
        pass

    def __str__(self):
        return f"{self.id}:{self.tipo}:{self.entrada}"
    

class Bike(Veiculo):
    def __init__(self, id, tipo, entrada):
        super().__init__(id, tipo, entrada)

    def calcularValor(self) -> float:
        return 3.00
    
class Moto(Veiculo):
    def __init__(self, id, tipo, entrada):
        super().__init__(id, tipo, entrada)

    def calcularValor(self):
        valor = self.entrada / 20
        return valor
    

class Carro(Veiculo):
    def __init__(self, id, tipo, entrada):
        super().__init__(id, tipo, entrada)

    def calcularValor(self):
        valor = self.entrada / 10
        if valor >5:
            return valor
        else:
            return 5.00
        
class Estacionamento:
    def __init__(self):
        self.lista: list[Veiculo] = []
        self.hora = 0



    def passarTempo(self, tempo: int):
        self.hora += tempo 

    def Estacionar(self, veiculo: Veiculo):
        self.lista.append(veiculo)
