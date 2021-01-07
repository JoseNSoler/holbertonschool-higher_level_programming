#!/usr/bin/python3
''' Square module '''


class Square:
    '''square class'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        """ Returns position of square """
        return self.__position

    @position.setter
    def position(self, value):
        '''
        Gives a x y position to square

        Args: coordinates x and y
        '''
        if (not all(num >= 0 for num in value) or
            not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        ''' Returns value of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Gives a size to a square

        Args: int to use for size
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Returns area of the square'''
        return(self.__size * self.__size)

    def my_print(self):
        '''Prints a square of # with this size
           and "space" for coordinates x and "\n" on y '''
        x_size, y_size = self.__size, self.__size
        z, a = 0, 0
        if x_size == 0:
            print()
        else:
            while a < self.__position[1]:
                print("")
                a += 1
            while y_size > 0:
                while x_size > 0:
                    while z < self.__position[0]:
                        print(" ", end="")
                        z += 1
                    print("#", end='')
                    x_size -= 1
                print()
                x_size = self.__size
                y_size -= 1
                z = 0
