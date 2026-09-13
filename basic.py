# print("******************Welcome to our Calculator*******************")
#
# num1 = int(input("Enter the First Number: "))
# num2 = int(input("Enter the Second Number: "))
#
# operator = int(input("Enter the Operator:\nMultiplication '*'\nAddition '+'\nSubtraction '-'\nDivision '/'\n")



# *****  Use of Arithmetic Operators ******
# Add two numbers (int) & (float)
# comparison of = & ==

# a = 10
# b = 20
# add = a + b
# print(add)
# print(a + b)
# print(a - b)
# print(b // a)
#
# x = 10
# x += 5
# print(x)

# num1 = int(input("Enter the First number: "))
# num2 = int(input("Enter the Second number: "))
#
# if num1 > num2 :
#     print(f"The Greatest number is: {num1}")
#
# elif num1 == num2 :
#     print(f"The Numbers are equal, {num1} = {num2}")
#
# else:
#     print(f"The Greatest number is: {num2}")

# n = int(input("Enter the Num: "))
#
# logic = int(n ** (1/2))
# print(f"The Square root of {n} is: {logic}")
#


# n1 = int(input("Enter the First Number: "))
# n2 = int(input("Enter the Second Number: "))
# n3 = int(input("Enter the Third Number: "))
# if n1 > n2 and n1 > n2:
#     print(f"{n1}, 'n1' is the Greatest number")
# elif n2 > n3:
#     print(f"{n2}, 'n2' is the Greatest number")
# else:
#     print(f"{n3}, 'n3' is the Greatest number")


# n1 = int(input("Enter the First Number: "))
# n2 = int(input("Enter the Second Number: "))
# n3 = int(input("Enter the Third Number: "))
# n4 = int(input("Enter the Fourth Number: "))
#
# if n1 > n2 and n1 > n3 and n1 > n4 :
#     print(f"{n1}, 'n1' is the Greatest number")
#
# elif n2 > n3 and n2 > n4 :
#     print(f"{n2}, 'n2' is the Greatest number")
# elif n4 > n3:
#     print(f"{n4}, 'n4' is the Greatest number")
# else:
#     print(f"{n3}, 'n3' is the Greatest number")


# first 100 prime numbers:
# n = 1
# count = 0
# for i in range (1, 100):
#     n += 1
#     c = 0
#
#     for j in range (1, n + 1):
#         if n % j == 0:
#             c += 1
#     if c == 2:
#         print(n)
#         count += 1
#     if count == 100:
#         break

# n = int(input("Enter the Number: "))
#
# prime = 0
#
# for i in range (1, n + 1):
#     if n % i == 0:
#         prime += 1
#
# if prime == 2:
#     print(n, "is the Prime number")
# else:
#     print(n, "is not the Prime number")

# number1 = 2
# number2 = 5
# print(number1)
# print(number2)
# for i in range (1,4):
#   number1 = number1 + 5
#   print(number1)
#   number2 = number1
# print("?")


# sum = 0
# for i in range (1,6):
#   sum = sum + i
#   sum = sum * i
#   print(sum)
# print("!")

num = int(input("Enter the Number "))
if num > 1:
  for i in range (2, num):
    if num % i == 0:
      print(f"{num} is not a prime number.")
      break
  else:
    print(f"{num} is a prime number.")
else:
  print(f"{num} is not a prime number.")