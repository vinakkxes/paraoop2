import math

class Shape:
    def __init__(self, color="неизвестный"):
        self.color = color
        self.area = 10  
    
    def get_area(self):
        print(self.area)
    
    def info(self):
        print(f"Фигура: {self.__class__.__name__}, Цвет: {self.color}, Площадь: {self.area}")


class Circle(Shape):
    def __init__(self, radius, color="неизвестный"):
        super().__init__(color)
        self.radius = radius
        self.area = self.get_area()
    
    def get_area(self):
        print(math.pi * (self.radius ** 2))
    
    def info(self):
        base_info = super().info()
        print(f"{base_info}, Радиус: {self.radius}")


class Square(Shape):
    def __init__(self, side, color="неизвестный"):
        super().__init__(color)
        self.side = side
        self.area = self.get_area()
    
    def get_area(self):
        print(self.side ** 2)
    
    def info(self):
        base_info = super().info()
        print(f"{base_info}, Сторона: {self.side}")
