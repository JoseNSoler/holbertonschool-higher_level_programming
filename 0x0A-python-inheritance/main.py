#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(4, 5)

print(r)
print(dir(r))

print(r.width)

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(True, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
