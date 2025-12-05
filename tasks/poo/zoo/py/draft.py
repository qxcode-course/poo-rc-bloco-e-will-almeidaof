from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name
        pass

    def apresentarNome(self):
        print(f"eu sou o(a) {self.name}")
        pass

    @abstractmethod
    def fazer_som(self):
        print("auuuu")
        pass

    @abstractmethod
    def mover(self):
        print("inhec")
        pass


class Leão(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def apresentarNome(self):
        return super().apresentarNome()
    
    def fazer_som(self):
        print("waaarhh")
    
    def mover(self):
        return super().mover()
    
class Girafa(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def apresentarNome(self):
        return super().apresentarNome()
    
    def fazer_som(self):
        print("uuuin")
    
    def mover(self):
        return super().mover()
    


class Macaco(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def apresentarNome(self):
        return super().apresentarNome()
    
    def fazer_som(self):
        print("nhic")
    
    def mover(self):
        return super().mover()
    
def Apresentar(animal: Animal):
    animal.apresentarNome()
    animal.fazer_som()
    animal.mover()
    print(type(animal).__name__)

animais: list[Animal] = [Leão("toto"), Girafa("Gloria"), Macaco("bob")]
for animal in animais:
    Apresentar(animal)
