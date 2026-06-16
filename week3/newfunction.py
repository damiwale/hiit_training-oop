# inbuilt function
# result = pow(10,2)  # mean 10 raise to power 2

def get_radius(d):
    radius = d/2
    return radius

def square_radius(radius):
    result = radius * radius
    return result


def multiply_by_pi(squared_radius):
    pi = 3.14
    area = pi * squared_radius
    return area


def calculate_area(d):

    r = get_radius(d)

    r_squared = square_radius(r)

    final_area = multiply_by_pi(r_squared)

    return final_area

result = calculate_area(10)

print("area of the circle is:", result)













