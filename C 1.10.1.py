class Rectangle:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def set_parameters(self, x, y, width, height):
        if (x > 0 and isinstance(x, int)) and (y > 0 and isinstance(y, int)) and (
                width > 0 and isinstance(width, int)) and (height > 0 and isinstance(height, int)):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            return f"Rectangle ({self.x}, {self.y}, {self.width}, {self.height})"
        else:
            return False


rect_1 = Rectangle()
print(rect_1.set_parameters(1, 3, 10, 12))

rec2 = Rectangle()
print(rec2.set_parameters(5, 7, 20, 22))
