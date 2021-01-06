#!/usr/bin/python3
''' Square module '''


class Square:
    '''square class'''
    def __init__(self, size=0):
        self.size = size

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
        '''Prints a square of # with this size '''
        x_size = self.__size
        y_size = self.__size

        if x_size == 0:
            print()
        else:
            while y_size > 0:
                while x_size > 0:
                    print("#", end='')
                    x_size -= 1
                print()
                x_size = self.__size
                y_size -= 1
