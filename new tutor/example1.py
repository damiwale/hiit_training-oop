print("welcome to class!")

# write a python program

#Ask the user for two numbers

#Display sum, Difference and product

num_1 = input("enter a number:")
num_2 = input("enter another number:")

conv_num1 = int(num_1)
conv_num2 = int(num_2)

the_sum = conv_num1 + conv_num2

diff = abs(conv_num1 - conv_num2)
prod = conv_num1 * conv_num2
avg = the_sum / 2

#print("The sum is: ", the_sum)
print(f"the sum of {num_1} and {num_2} is: {the_sum}")
print(f"The diff is:{diff}")
print(f"the prod is: {prod}")
print(f"The Average is:{avg}")



