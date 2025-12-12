from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, entrada: int):
        self.id = id
        self.tipo = tipo
        self.entrada = entrada


    @abstractmethod
    def calcularValor(self, saida: int):
        pass

    def __str__(self):
        id = self.id.rjust(10,"_")
        tipo = self.tipo.rjust(10,"_")
        return f"{tipo} : {id} : {self.entrada}"
    

class Bike(Veiculo):
    def __init__(self, id, tipo , entrada):
        super().__init__(id, tipo, entrada)

    def calcularValor(self, saida: int = 0) -> float:
        return f"{3:.2f}"
    
class Moto(Veiculo):
    def __init__(self, id, tipo, entrada):
        super().__init__(id, tipo, entrada)

    def calcularValor(self, saida: int):
        valor = (saida - self.entrada) / 20
        return f"{valor:.2f}"
    

class Carro(Veiculo):
    def __init__(self, id, tipo, entrada):
        super().__init__(id, tipo, entrada)

    def calcularValor(self, saida: int):
        valor = (saida - self.entrada) / 10
        if valor >5:
            return f"{valor:.2f}"
        else:
            return f"{5:.2f}"
        
class Estacionamento:
    def __init__(self):
        self.lista: list[Veiculo] = []
        self.hora = 0

    def getHora(self):
        return self.hora

    def passarTempo(self, tempo: int):
        self.hora += tempo 

    def Estacionar(self, veiculo: Veiculo):
        self.lista.append(veiculo)


    def procurar(self, id: str) -> Veiculo | None:
        for veiculo in self.lista:
            if veiculo.id == id:
                return veiculo
        return None

    def pagar(self, veiculo: Veiculo):
        entrada = veiculo.entrada
        saida = self.getHora()
        valor = veiculo.calcularValor(saida)
        return f"{veiculo.tipo} chegou {entrada} saiu {saida}. Pagar R$ {valor}"





    def __str__(self):
        lista = "\n".join([str(x) for x in self.lista])
        if not lista:
            return f"Hora atual: {self.hora}"
        return f"{lista}\nHora atual: {self.hora}"

def main():
    estaciona = Estacionamento()
    while True:
        line = input()
        print("$"+line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estaciona)
        elif args[0] == "tempo":
            estaciona.passarTempo(int(args[1]))
        elif args[0] == "estacionar":
            if args[1] == "bike":
                bike = Bike(args[2],"Bike", estaciona.getHora())
                estaciona.Estacionar(bike)
            elif args[1] == "moto":
                moto = Moto(args[2],"Moto", estaciona.getHora())
                estaciona.Estacionar(moto)
            elif args[1] == "carro":
                carro = Carro(args[2],"Carro", estaciona.getHora())
                estaciona.Estacionar(carro)

        elif args[0] == "pagar":
            id = args[1]
            veic = estaciona.procurar(id)
            if veic:
                print(estaciona.pagar(veic))
                estaciona.lista.remove(veic)





main()