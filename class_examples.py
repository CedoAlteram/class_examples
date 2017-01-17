import sys
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

    def describe(self, text):
        self.description = text
        return text + " and the value of the"

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale
        return self.x, self.y

x = int(sys.argv[1])
y = int(sys.argv[2])
x2 = int(sys.argv[3])
y2 = int(sys.argv[4])

Shape1 = Shape(x,y)
Shape2 = Shape(x2,y2)

#print(Shape1.area())
#print(Shape2.area())
#print(Shape1.perimeter())
#print(Shape1.scaleSize(0.5))
print(Shape1.describe("Aaron, this is the first shape,"), "area is", Shape1.area())
print(Shape2.describe("Aaron, this is the second Shape,"), "area is", Shape2.area())
#print(Shape1.description)
#print("all clear go home")

first_area = Shape1.area()
second_area = Shape2.area()

total_area = first_area + second_area

print("The total area is of both shapes is", total_area)