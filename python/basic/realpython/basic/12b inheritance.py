# All methods that are called with super() need to have a call to their superclass’s version of that method. This means that you will need to add super().__init__() to the .__init__() methods of Triangle and Rectangle.

# Redesign all the .__init__() calls to take a keyword dictionary. See the complete code below.

class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    def volume(self):
        face_area = super().area()
        return face_area * self.length

class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)
    def tri_area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs['height'] = slant_height
        kwargs['length'] = base
        super().__init__(base=base, **kwargs)
    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area
    def area2(self):
        base_area = super().area()
        triangle_area = super().tri_area
        return triangle_area * 4 + base_area

pyramid = RightPyramid(base=2, slant_height=4)
print(pyramid.area())
print(pyramid.area_2())

# kwargs is modified in some places (such as RightPyramid.__init__()): This will allow users of these objects to instantiate them only with the arguments that make sense for that particular object.

# Setting up named arguments before **kwargs: You can see this in RightPyramid.__init__(). This has the neat effect of popping that key right out of the **kwargs dictionary, so that by the time that it ends up at the end of the MRO in the object class, **kwargs is empty.

# Class	Named   Arguments	        kwargs
# RightPyramid	base, slant_height	
# Square	    length	            base, height
# Rectangle	    length,width	    base, height
# Triangle	    base, height