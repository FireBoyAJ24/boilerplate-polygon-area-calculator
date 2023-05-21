class Rectangle:

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def __repr__(self) :
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height


    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            pic_str = ""
            for i in range(0, self.height, 1):
                pic_str += self.width * "*" + "\n"
            return pic_str
        else:
            return "Too big for picture."
    
    def get_amount_inside(self, test):
        area_self = self.get_area()
        area_test = test.get_area()

        nheight = int(self.height / test.height)
        nwidth = int(self.width / test.width)
        ntimes = nheight * nwidth
        
        return ntimes
        
class Square(Rectangle):

    def __init__(self, side=0):
        self.height = side
        self.width = side

    def __repr__(self) :
        return "Square(side={})".format(self.height)
        
    def set_side(self, side):
        self.height = side
        self.width = side
    
    def set_height(self, height):
        self.height = height
        self.width = height

    def set_width(self, width):
        self.width = width
        self.height = width


