student_name = str(input("Enter the name of the Student: "))
age = int(input("Enter the age: "))
marks = float(input("Enter the marks out of 100: "))

print(f"The name of Student is: {student_name}\nThe age of the student is: {age}\nThe grades are: {marks}")



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The sum is {num1 + num2}\nThe product is {num1 * num2}\nThe Difference is {num1 - num2}\nThe Quotient is {num1 / num2}\nThe Remainder is {num1 % num2}\nThe floor is {num1 // num2}")

length = int(input("Enter the Length: "))
breadth = int(input("Enter the Breadth: "))
area = length * breadth
perimeter = length + breadth
print(f"The Area of Rectangle is: {area}\nThe Perimeter of Rectangle is: {perimeter}")

radius = int(input("Enter the Radius: "))
area = 3.14 * (radius ** 2)
circumference = 2 * 3.14 * radius
print(f"The area of circle is: {area}\nThe circumference of circle is: {circumference}")

sub1 = int(input("Enter the Marks of first subject: "))
sub2 = int(input("Enter the Marks of second subject: "))
sub3 = int(input("Enter the Marks of third subject: "))
total_marks = sub1 + sub2 + sub3
average = total_marks / 3
print(f"The total marks are: {total_marks}\nThe average marks are: {average}")

cel = int(input("Enter the temperature (in Celsius): "))
faren = float((cel * (9/5)) + 32)
print(f"The Temperature in Faren is: {faren}")

principal = int(input("Enter the Principal amount: "))
rate = int(input("Enter the Rate: "))
time = int(input("Enter the Time: "))
simple_interest = (principal * rate * time) / 100
print(f"The Simple Interest is: {simple_interest}")

num = int(input("Enter the two Digit number: "))
tens_digit = num // 10
units_digit = num % 10
print(f"Tens digit for the number {num} is: {tens_digit}\nUnits digit for the number {num} is: {units_digit}")

price = int(input("Enter the Price: "))
quantity = int(input("Enter the Quantity: "))
bill = quantity * price
discount = int((bill * 0.1))
total_bill = bill - discount
print(f"The Price of an Iteam is: {price}₹\nThe Quantity is: {quantity}\nBill before the discount is: {bill}₹\nDiscount provided: {discount}%\nThe Total bill is: {total_bill}₹")

age = int(input("Enter the Age: "))
marks = int(input("Enter the Marks: "))
print(age>=18)
print(marks>=40)

a = "10"
b = "20"
print(a + b)