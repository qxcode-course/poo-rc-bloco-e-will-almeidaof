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
            print(f"PIX enviado via {self.banco} usando chave {self.chave}")
        else:
            print(f"Erro: PIX não enviado para a chave {self.chave}")




class Credito(Pagamento):
    def __init__(self, valor, descricao, numero: int, titular: str, limite: int):
        super().__init__(valor, descricao)
        self.numero = numero
        self.titular = titular
        self.limite = limite

    def Processar(self):
        if not self.validarValor():
            print(f"Erro: Valor inválido")
            return
        if self.validarValor():
            if self.valor > self.limite:
                print(f"Erro: Limite insuficiente no cartão {self.numero}")
            else:
                restante = self.limite - self.valor
                self.limite = restante
                print(f"Pagamento aprovado no cartão Cliente {self.titular}. Limite restante: {self.limite}")
            




class Boleto(Pagamento):
    def __init__(self, valor, descricao, codigo: str, vencimento: str):
        super().__init__(valor, descricao)
        self.codigo = codigo
        self.vencimento = vencimento

    def Processar(self):
        if self.validarValor():
            print(f"Boleto gerado. Aguardando pagamento...")
        else:
            print(f"Boleto não foi gerado. Valor inválido!")


def processar_pagamentos(pagamento: Pagamento):
        pagamento.validarValor()
        pagamento.resumo()
        pagamento.Processar()






pagamentos = [
    Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"),
    Credito(400, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500),
    Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10"),
    Credito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700),  # deve falhar
]
    
for pagamento in pagamentos:
    processar_pagamentos(pagamento)
