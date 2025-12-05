from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:int, descricao: str):
        self.valor: float = valor
        self.descricao: str = descricao


    def resumo(self) -> str:
        print(f"Pagamento de R${self.valor}: {self.descricao}")

    def validarValor(self) -> bool:
        if self.valor <= 0:
            return False
        return True
    
    @abstractmethod
    def Processar():
        pass
    
class Pix(Pagamento):
    def __init__(self, valor, descricao, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def Processar(self):
        if self.validarValor():
            print(f"Pagamento de R$ {self.valor}: {self.descricao} \nPIX enviado via {self.banco} usando chave {self.chave}")
        else:
            print(f"Pagamento de R$ {self.valor}: {self.descricao} \nPIX não enviado via {self.banco} usando chave {self.chave}")




class Credito(Pagamento):
    def __init__(self, valor, descricao, numero: int, titular: str, limite: int):
        super().__init__(valor, descricao)
        self.numero = numero
        self.titular = titular
        self.limite = limite

    def Processar(self):
        if self.validarValor():
            if self.valor > self.limite:
                print(f"Pagamento de R$ {self.valor}: {self.descricao} \nPagamento reprovado no cartão Cliente {self.titular}. Limite restante: {self.limite}")
            else:
                restante = self.valor - self.limite
                self.limite = restante
                print(f"Pagamento de R$ {self.valor}: {self.descricao} \nPagamento aprovado no cartão Cliente {self.titular}. Limite restante: {self.limite}")










pix = Credito(100,"Blusa",66000,"Jose",200)
pix.Processar()

    

            
