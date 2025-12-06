from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass
    
    @abstractmethod
    def get_perimeter(self):
        pass
    
    @abstractmethod
    def getName(self):
        pass
    
class Point2d:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y 

    def __str__(self):
        return f"{self.x:.2f}, {self.y:.2f}"
    
    
class Circle(Shape):
    def __init__(self, point2d: Point2d, r: float):
        self.name = "Circ"
        self.center = point2d
        self.radius = r

    def getName(self):
        return self.name
    
    
    def get_perimeter(self):
        perimeter = 2*3.14*self.radius
        return perimeter
    
    def getArea(self):
        area = 3.14*(self.radius**2)
        return area
    

    def __str__(self):
        return f"{self.name}: C=({self.center}), R={self.radius:.2f}"
    


class Rectangle(Shape):
    def __init__(self, p1: Point2d, p2: Point2d):
        self.name = "Rect"
        self.p1 = p1
        self.p2 = p2

    def getName(self):
        return self.name
    
    def getArea(self):
        largura = self.p1.x - self.p2.x
        altura = self.p1.y - self.p2.y
        area = largura*altura
        return area
    
    def get_perimeter(self):
        largura = self.p1.x - self.p2.x
        altura = self.p1.y - self.p2.y
        perimeter = 2*(abs(largura)+abs(altura))
        return perimeter
    
    def __str__(self):
        return f"{self.name}: P1=({self.p1}) P2=({self.p2})"
    

def info(shape: Shape):
    name = shape.getName()
    area = shape.getArea()
    perimeter = shape.get_perimeter()
    return f"{name}: A={area:.2f} P={perimeter:.2f}"

def main():
    lista: list[Shape] = []
    while True:
        try:
            line = input()
            print("$"+line)
            args = line.split()
            if args[0] == "end":
                break
            elif args[0] == "circle":
                x = float(args[1])
                y = float(args[2])
                r = float(args[3])
                center = Point2d(x,y)
                circle = Circle(center,r)
                lista.append(circle)

            elif args[0] == "rect":
                p1 = Point2d(float(args[1]), float(args[2]))
                p2 = Point2d(float(args[3]), float(args[4]))
                rect = Rectangle(p1,p2)
                lista.append(rect)


            elif args[0] == "info":
                for shape in lista:
                    print(info(shape))

            elif args[0] == "show":
                for shape in lista:
                    print(shape)


            
            
        except Exception as e:
            print(e)


main()