# sum 

# a = int(input("Enter number 1 : "))
# b = int(input("Enter number 2 : "))

# sum = a+b;
# print("The sum is ", sum)     


# # even odd

# num = int(input("Enter a number : "))

# if num%2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # factorial

# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"Factorial of {num} is {factorial}")


# #palindorme

# word = input("Enter a word: ")
# if word == word[::-1]:
#     print("It's a palindrome!")
# else:
#     print("Not a palindrome.")


# #Prime Number Check


# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")



# #Find Largest Element in a List

# numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
# print(f"Largest number is: {max(numbers)}")


#Reverse a String

# string = input("Enter a string: ")
# reversed_string = string[::-1]
# print(f"Reversed string: {reversed_string}")


# #Check if a Number is Positive, Negative, or Zero

# num = float(input("Enter a number: "))
# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")



#Sum of Digits in a Number

# num = int(input("Enter a number: "))
# total = sum(int(digit) for digit in str(num))
# print(f"Sum of the digits: {total}")



# Print Multiplication Table of a Given Number

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")