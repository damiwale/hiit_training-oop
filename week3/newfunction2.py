from newfunction import get_radius, square_radius, multiply_by_pi, calculate_area
import numpy as np

numbers = [2,3,4,5]
average = np.mean(numbers)
print(f"average is {average}")
def calculate_area(d):

    r = get_radius(d)

    r_squared = square_radius(r)

    final_area = multiply_by_pi(r_squared)

    return final_area

result = calculate_area(10)
print("area of the circle is:", result)











