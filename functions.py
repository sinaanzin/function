Fruits = ["Orange","Apple","Mango","Grapes","Gauva"]
length_of_list = len(Fruits)
print("The length of the list is:", length_of_list)

def msg():
    print("Hello,Sinaan!")
msg()


def find_maximum(numbers):
    if not numbers:
        return None
    max_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

numbers = [8, 5, 0, 9, 4]
print(find_maximum(numbers))


x = 5
def my_function():
    x = 10
    print("Inside the function, local x:", x)
my_function()
print("Outside the function, global x:", x)


def calculate_area(length, width=5):
    area = length * width
    return area
area_with_both = calculate_area(10, 4)
print("Area with both length and width:", area_with_both)
area_with_default_width = calculate_area(10)
print("Area with default width:", area_with_default_width)
