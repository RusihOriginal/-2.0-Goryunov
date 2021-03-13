class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_parameters(self, width, height):
        if (isinstance(width, int)) and (isinstance(height, int)):
            self.width = width
            self.height = height
        else:
            return False

    def get_area(self):
        return self.width * self.height


area = Rectangle()
area.set_parameters(5, 8)
print(area.get_area())