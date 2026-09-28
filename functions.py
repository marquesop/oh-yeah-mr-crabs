def greet_user(name):
    print("Hello", {name}, "! Welcome to python!")

greet_user("Ava")


def add_numbers(a, b):
        total = a + b
        return total

result = add_numbers (10,5)
print(f"10 + 5 = {result}")


def describe_pet(name, animal="dog"):
      print(f"{name} has a {animal}")

describe_pet("Milo")
describe_pet("Zoe", "cat")


def area_of_rectangle(width, height):
      area = width * height
      return area

room_area = area_of_rectangle(8,5)
print(f"The area of this rectangle is {room_area} Sqaure feet")


def square(number):
      return number + number

def sqaure_and_double(number):
      squared = square(number)
      doubled = squared * 2
      print(f"Number: {number}")
      print(f"Square: {squared}")
      print(f"Double the squared {doubled}")

sqaure_and_double(4)


def is_even(number):
      if number % 2 == 0:
            return True
      return False

for value in [2, 7, 10, 13, 22]:
      print(f"{value} is even? {is_even(value)}")


print("\nLesson complete! You now know the basics of python functions!")