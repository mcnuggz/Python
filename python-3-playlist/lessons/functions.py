# def greet(name = "John", time = "morning"):
#     print(f"Hello {name}, it is {time} time, hope you are well")

# name = input("Enter your name: ")
# time = input("Is it morning, afternoon, or evening? ")

# greet()

def area(radius):
    return 3.142 * radius**2

def vol(area, length):
    print(area * length)

radius = int(input("Enter the radius of your circle: "))
length = int(input("Enter a length: "))

#area_calc = area(radius)
vol(area(radius), length)