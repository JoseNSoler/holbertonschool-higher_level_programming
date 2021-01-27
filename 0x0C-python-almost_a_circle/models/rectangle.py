#!/usr/bin/python3
'''Module - Rectangle geometry '''

from models.base import Base


class Rectangle(Base):
    '''Class - Rectangle object '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializer for Rectangle

        Args:
            width: User's given width
            height: User's given height
            x: User's given x position
            y: User's given y position
            id: User's given id int for obj. Rectangle
            (validated through Parent class)
        '''
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super(Rectangle, self).__init__(id)
        self.__id = self.id

    @property
    def width(self):
        '''Getter for width of rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for width of rectangle

        TypeError if value is not int
        ValueError ir value is under or equal than 0
        '''
        if (not type(value) is int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Getter for height of rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for height of rectangle

        TypeError if value is not int
        ValueError ir value is under or equal than 0
        '''
        if (not type(value) is int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Getter for x of rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for x of rectangle

        TypeError if value is not int
        ValueError ir value is under than 0
        '''
        if (not type(value) is int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Getter for y of rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter for y of rectangle

        TypeError if value is not int
        ValueError ir value is under than 0
        '''
        if (not type(value) is int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Returns area of object <Rectangle> '''
        return (self.__height * self.__width)

    def display(self):
        '''
        Prints our shape object maded with `#`
        //Second Update: it take in consideration x and y coordinates
        '''
        for x in range(0, self.__y):
            print ()
        for x in range(0, self.__height):
            for y in range(0, self.__x):
                print(" ", end='')
            for y in range(0, self.__width):
                print("#", end='')
            print ()

    def update(self, *args, **kwargs):
        """
        Update the Rectangle.
        Args:
            *args (ints): New given user's attribute value
                - 1st argument= id attribute
                - 2nd argument= width attribute
                - 3rd argument= height attribute
                - 4th argument= x attribute
                - 5th argument= y attribute
            //Second Update:
                **kwargs (dict): key/value pairs of attributes
        """
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 1:
                    self.width = arg
                elif x == 2:
                    self.height = arg
                elif x == 3:
                    self.x = arg
                elif x == 4:
                    self.y = arg
                x += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary with values of object Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        '''Default print string'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
