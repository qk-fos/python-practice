import math


def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")


def rectangle_area():
    length = float(input("What's the length: "))
    height = float(input("What's the height: "))

    area = length * height

    print(f"Area of the rectangle is {area:.2f}")


def circle_area():
    radius = float(input("What's the radius: "))

    area = math.pi * (math.pow(radius, 2))

    print(f"Area of the circle is {area:.2f}")


def main():
    shape_type = input("What shape type: ")

    get_area(shape_type)


main()
