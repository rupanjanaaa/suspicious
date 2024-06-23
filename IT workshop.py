Experiment 1: Aim: Create a Python script that prompts the user for their name and age, then prints a message welcoming them if they are above 18 years old, otherwise, it asks them to come back when they are older. 
name = input("Enter your name: ")
 age = int(input("Enter your age: ")) if age >= 18: 
print("Welcome,", name, "! You are eligible.") 
else: print("Sorry,", name, ". Please come back when you are older.") 


Experiment 2: Aim: Write a program that calculates the area and perimeter of a rectangle given its length and width. Allow the user to input the dimensions.
 length = float(input("Enter the length of the rectangle: ")) 
width = float(input("Enter the width of the rectangle: ")) 
area = length * width
 perimeter = 2 * (length + width) 
print("Area of the rectangle:", area) 
print("Perimeter of the rectangle:", perimeter) 


 Experiment 3: Aim: Develop a simple temperature conversion program that converts Celsius to Fahrenheit and vice versa, based on user input. 
def celsius_to_fahrenheit(celsius):
 return (celsius * 9/5) + 32
 def fahrenheit_to_celsius(fahrenheit): 
return (fahrenheit - 32) * 5/9 
choice = input("Enter 'C' to convert Celsius to Fahrenheit, 'F' for Fahrenheit to Celsius: ").upper()
 if choice == 'C':
 celsius = float(input("Enter temperature in Celsius: "))
 fahrenheit = celsius_to_fahrenheit(celsius) 
print("Temperature in Fahrenheit:", fahrenheit)
 elif choice == 'F': 
fahrenheit = float(input("Enter temperature in Fahrenheit: ")) 
celsius = fahrenheit_to_celsius(fahrenheit) 
print("Temperature in Celsius:", celsius)
 else: 
print("Invalid choice!") 


 Experiment 4: Aim: Write a Python program that acts as a basic calculator performing addition, subtraction, multiplication, and division based on user input.
 def add(x, y):
 return x + y 
def subtract(x, y):
 return x – y
 def multiply(x, y):
 return x * y 
def divide(x, y): 
if y == 0:
 return "Error: Division by zero"
 else:
 return x / y 
print("Select operation:")
 print("1. Addition")
 print("2. Subtraction") 
print("3. Multiplication") 
print("4. Division")
 choice = input("Enter choice (1/2/3/4): ") 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))
 if choice == '1':
 print("Result:", add(num1, num2)) 
elif choice == '2':
 print("Result:", subtract(num1, num2))
 elif choice == '3':
 print("Result:", multiply(num1, num2)) 
elif choice == '4':
 print("Result:", divide(num1, num2))
 else: 
print("Invalid input") 


Experiment 5: Aim: Write a Python program that takes user input for the radius of a circle and calculates its area and circumference.
 import math 
radius = float(input("Enter the radius of the circle: "))
 area = math.pi ** radius 2 
circumference = 2 * math.pi * radius 
print("Area of the circle:", area) 
print("Circumference of the circle:", circumference) 

Experiment 6: Aim: Create a Python program that prompts the user for their birth year and calculates their age based on the current year.
 from datetime import date 
current_year = date.today().year
 birth_year = int(input("Enter your birth year: "))
 age = current_year - birth_year 
print("Your age is:", age) 

Experiment 7: Aim: Create a module for basic mathematical operations (addition, subtraction, multiplication, division) and import it into a main script to perform calculations. 
math_operations.py: 
 # math_operations.py - Module for basic mathematical operations 
def add(x, y): 
return x + y 
def subtract(x, y):
 return x - y 
def multiply(x, y): 
return x * y 
def divide(x, y):
 if y == 0:
 return "Error: Division by zero"
 else:
 return x / y 
# main_script.py - Main script importing math_operations module
 import math_operations
 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))
 print("Select operation:") 
print("1. Addition") 
print("2. Subtraction")
 print("3. Multiplication") 
print("4. Division") 
choice = input("Enter choice (1/2/3/4): ")
 if choice == '1':
 print("Result:", math_operations.add(num1, num2)) 
elif choice == '2':
 print("Result:", math_operations.subtract(num1, num2))
 elif choice == '3': 
print("Result:", math_operations.multiply(num1, num2)) 
elif choice == '4': 
print("Result:", math_operations.divide(num1, num2)) 
else:
 print("Invalid input") 


Experiment 8: Aim: Explore the time module to create a stopwatch program. Allow the user to start and stop the timer and display the elapsed time.
 import time
 start_time = 0 
end_time = 0 
def start_timer():
 global start_time
 start_time = time.time()
 def stop_timer():
 global end_time 
end_time = time.time() 
def elapsed_time(): 
return end_time - start_time
 start_timer()
 input("Press Enter to stop the timer...")
 stop_timer() 
print("Elapsed time:", elapsed_time(), "seconds") 

Experiment 9: Aim: Write a program that imports the random module to generate a random number between 1 and 100 and asks the user to guess it. Provide feedback on whether the guess is too high, too low, or correct. 
import random 
target_number = random.randint(1, 100) 
while True: 
guess = int(input("Guess the number (between 1 and 100): ")) 
if guess < target_number:
 print("Too low! Try again.") 
elif guess > target_number:
 print("Too high! Try again.") 
else: 
print("Congratulations! You guessed it right!") 
break 
Experiment 10: Aim: Develop a program that checks whether a given year is a leap year or not, considering leap year rules. Prompt the user to input a year
year = int(input("Enter a year: ")) 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 print(year, "is a leap year.") 
else:
 print(year, "is not a leap year.")

Experiment 11: Aim: Write a program that simulates a basic ATM transaction. Allow the user to enter their account balance and withdraw a specified amount if sufficient funds are available.
 balance = float(input("Enter your account balance: "))
 withdrawal = float(input("Enter the amount to withdraw: "))
 if withdrawal <= balance: 
balance -= withdrawal
 print("Withdrawal successful! Remaining balance:", balance) 
else:
 print("Insufficient funds! Transaction failed.")
 
Experiment 12: Aim: Create a program that prompts the user to input their exam score and displays their grade based on the score range (e.g., A, B, C, D, F). 
score = int(input("Enter your exam score: "))
 if score >= 90: 
grade = 'A' 
elif score >= 80: 
grade = 'B' 
elif score >= 70:
 grade = 'C' 
elif score >= 60: 
grade = 'D' else:
 grade = 'F'
 print("Your grade is:", grade) 
Experiment 13: Aim: Implement a program that generates and prints the Fibonacci sequence up to a specified number of terms using a while loop.
 num_terms = int(input("Enter the number of terms: "))
 # First two terms of the Fibonacci sequence 
first_term = 0 
second_term = 1 
count = 0
 # Check if the number of terms is valid 
if num_terms <= 0: 
print("Please enter a positive integer.") 
elif num_terms == 1: 
print("Fibonacci sequence:") 
print(first_term) 
else: 
print("Fibonacci sequence:") 
while count < num_terms:
 print(first_term, end=", ") 
nth_term = first_term + second_term 
# Update values for the next iteration
 first_term = second_term 
second_term = nth_term 
count += 1 

 Experiment 14: Aim: Write a program that prompts the user to input a number and checks if it's a prime number or not using a for loop and conditional statements.
 num = int(input("Enter a number: ")) 
if num <= 1:
 print("Not a prime number.")
 else:
 is_prime = True 
for i in range(2, int(num 0.5) + 1): 
if num % i == 0: 
is_prime = False 
break
 if is_prime:
 print(num, "is a prime number.")
 else:
 print(num, "is not a prime number.") 

Experiment 15: Aim: Develop a program that simulates rolling a dice. Allow the user to roll the dice and keep rolling until they choose to stop. Display the results of each roll and the total sum.
 import random 
total_sum = 0 
while True: 
roll = random.randint(1, 6) 
print("You rolled:", roll) 
total_sum += roll
 choice = input("Do you want to roll again? (yes/no): ").lower()
 if choice != 'yes':
 break 
print("Total sum of rolls:", total_sum) 


Experiment 16: Aim: Create a function that calculates the factorial of a given number recursively.
 def factorial(n):
 if n == 0: 
return 1 .
else:
 return n * factorial(n - 1) 
# Test the function
 num = int(input("Enter a number to calculate its factorial: ")) 
print("Factorial of", num, "is", factorial(num))

Experiment 17:Aim: Develop a program that calculates the area of different geometric shapes (Circle, rectangle, triangle) based on user input. Define separate functions you each shape.
import math
def area_circle (radius):
   return math.pi*radius**2
def area_rectangle (length,width):
   return length*width

def area_triangle (base, height): 
   return 0.5*base*height

shape = input("Enter the shape (circle/rectangle/triangle):). lower()

if shape == "circle":

   radius = float(input("Enter the radius the circle:"))  
print("Area of the circle:",area_circle(radius))

elif shape="rectangle": 
   length = float(input("Enter the length of the rectangle:"))       
     width= float(input("Enter the width of the rectangle:")

print ("Area of the rectangle:", area_rectangle(length, width))

elif shape == "triangle":

base=float(input("Enter the base length of the triangle:")) height=float(input("Enter the height of the triangle:")) 
print("Area of the triangle:", area_triangle (base, height))

else:

print ("Invalid shape entered. Please enter 'circle', 'rectangle' or 'triangle'.")



Experiment 18: Aim: Write a program that demonstrates various string manipulation operations such as slicing, concatenation and formatting.

S= "Hello, World!"
print("Original string:", S) 
print("Slice [7:]:", s[7:])
print("slice [2:9]:", s[2:9]
S1="Hello"
S2= "World"
S3= S1 +", "+S2 +"!"
print("concatenated string:"S3)
name = Harry
age = 35 
formatted_string = "Name{}, Age: {}". format (name, age)
print ("Formatted string:", formatted_string)


Experiment 19: Aim: Write a python script that demonstrates basic arithmatic operations(addition, subrtaction, multiplication, division) on two numbers using lambda functions.

num1=10
num2=5
addition = lambda x,y: x+y
subtraction = lambda x,y: x-y 
multiplication = lambda x, y: x*y
division = lambda x,y: x/y
 if y!= 0
 else 'undefined'
add = addition (num1, num2)
sub = subtraction (num1, num2) 
multi = multiplication (num1, num2)
divide = division (num1, num2)
print (f" Addition: {num1} + {num2} = {add}") 
print (f" Subtraction: {num1} - {num2} = {sub}") 
print (f"multiplication: {num1} * {num2} = {multi}") 
print (f"division: {num1}/{num2} = {divide}")

Experiment 20: Aim: Implement a function that filters even numbers from a given list using a lambda function and filter() "function.

def filter_even_numbers (numbers): 
    even numbers = list (filter (lambda x:x%2==0, numbers))
return even numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
 even_numbers = filter_even_numbers(numbers)
 print (f"original list:{numbers}")
print (f" Filtered list (even_ numbers): {even numbers}")





Experiment 21: Aim: Create a list comprehension to generate a list of squared numbers from 1 to 10.

Squared_numbers = [x** 2 for x in range (1, 11)]
print (f" Squared numbers from 1 to 10: {Squared_numbers")





