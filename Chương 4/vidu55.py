#Class Circle
class Circle:

    Pi = 3.141592

    def __init__(self, radius=1):
        self.r = radius

    def DienTich(self):
        return self.r * self.r * Circle.Pi


c = Circle(5)

print("Diện tích hình tròn là:",
      c.DienTich())