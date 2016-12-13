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


Shape1 = Shape(10,10)
Shape2 = Shape(20,20)
Shape3 = Shape(30,30)

print(Shape1.area())
print(Shape2.perimeter())
print(Shape3.scaleSize(0.5))

print("all clear go home")