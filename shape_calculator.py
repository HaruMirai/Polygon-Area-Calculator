class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    # width and height setters
    def set_width(self,value):
        self.width=value
    def set_height(self,value):
        self.height=value
    #methods
    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return  (2 *self.width + 2*self.height)
    
    def get_diagonal(self):
        return (self.width **2 + self.height **2)**.5
    
    def get_picture(self):
        if self.width >50 or self.height>50:
            return  "Too big for picture."
        rectanglePicture=['*'*self.width for i in range(self.height)]
        return '\n'.join(rectanglePicture)
    
    def get_amount_inside(self,shape):
        amountInside=int(self.get_area()/shape.get_area())
        if amountInside < 1:
            return 0
        return amountInside
    #str output
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self,side):
        self.side=side
        super().__init__(side,side)
    #setter
    def set_side(self,value):
        self.side=value
        self.width=value
        self.height=value
    def set_width(self,value):
        self.set_side(value)
    def set_height(self,value):
        self.set_side(value)
    #str ouput
    def __str__(self):
        return f"Square(side={self.side})"