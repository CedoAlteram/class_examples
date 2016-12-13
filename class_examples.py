import sys, os
#An example of a class
class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self):
        self.description = text


    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale
        return self.x, self.y

x = int(sys.argv[1])
y = int(sys.argv[2])

Shape1 = Shape(x,y)

print(Shape1.area())
print(Shape1.perimeter())
print(Shape1.scaleSize(0.5))

print("all clear go home")