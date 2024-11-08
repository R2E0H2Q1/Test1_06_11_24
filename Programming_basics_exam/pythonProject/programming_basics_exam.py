"""Introductory Programming Test"""
print('-----> Conditionals:')
print()

#1. Receive two decimal numbers. Print the smaller one 3 times.

num1: float = float(input('Enter your first number: '))
num2: float = float(input('Enter your second number: '))

if num1 < num2:
    smaller = num1
else:
    smaller = num2

for _ in range(3):
    print(f'The smaller number between the provided ones is: {smaller}')

#2. Receive two  numbers and print their sum and average.

n1: int = int(input('Enter your first number: '))
n2: int = int(input('Enter your second number: '))

count = n1 + n2
average = count / 2

print(f'The sum of numbers {n1} and {n2} is equal to {count} and their average is {average}')

#3. Receive 3 numbers and print the largest one of them.

x: int = int(input('Enter the first number: '))
y: int = int(input('Enter the second number: '))
z: int = int(input('Enter the third number: '))

if x >= y and x >= z:
    highest = x
    print(f'The higher number is {x}!')

elif y >= x and y >= z:
    highest = y
    print(f'The higher number is {y}!')

else:
    highest = z
    print(f'The higher number is {z}!')

#4. Receive the duration of a movie in minutes and print how many hours and minutes is:
#- For example if you receive 105 the answer will be: 1 hour and 45 minutes.

mov_min: int = int(input('How long in minutes it last the movie? '))

minInH = 60
hours = mov_min // minInH
minutes: int = mov_min % 60

print(f'The duration of the movie was {hours} hour and {minutes} minutes!')

#5. Receive a 4 digit number, check if is divisble by 4 without a remainder. If so, find and print the leftmost digit.

fourth_digits = int(input('Enter a fourth digits number: '))

if fourth_digits < 1000 or fourth_digits > 9999:
    print('Error, you must enter a 4 digits number!')

else:
    if fourth_digits % 4 == 0:
        l_digit = str(fourth_digits)[0]
        print(f'The leftmost digit of {fourth_digits} is {l_digit}!')

    else:
        print(f'Number {fourth_digits} is not divisible by 4!')

#6. Receive a number and check if is 4 digit number and print the second one on the right.

if fourth_digits < 1000 or fourth_digits > 9999:
    print('Error, you must enter a 4 digits number!')

else:
    second_right = (fourth_digits // 10) % 10 #the first section
    print(f' From right to left the second digit of {fourth_digits} is {second_right}')

#7. Enter a two digit number and print the sum of its digits.

two_digits = int(input('Enter a two digits number: '))

if two_digits < 10 or two_digits > 99:
    print('Error, you must enter a 2 digits number!')

else:
    tens = two_digits // 10 #extracts the tens
    units = two_digits % 10 #extracts the units
    total_digits = tens + units

    print(f'The sum of these digits is: {total_digits}')

#8. Enter a two-digit number and reverse it's digits. For example if 61 is received the answer will be 16.

reversed_number = int(str(two_digits)[::-1])
print('The reversed number is:', reversed_number)

#9. Collect a number and print even or odd:

try:
    even_odd = int(input('Enter a number: '))

    if even_odd % 2 == 0:
        print('The number is even!')

    else:
        print('The number is odd!')

except:
    print('Enter a valid number!')

#10. --->


#11. You can board the train only if you are:
#- Between 8 and 18 years or old and your height is equal or higher than 115 cm.
#- If you are older than 18 years old and your height is more than 100 cm.
#- Collect from the user the age an height in centimeters and check if is allowed to board the train.

age = int(input('Enter your age: '))
heigth = int(input('Enter your height in centimeters: '))

if age >= 8 and age <= 18 and heigth > 115:
    print('Welcome aboard!')

elif age >= 18 and heigth >= 100:
    print('Welcome aboard!')

else:
    print('You dont meet the required criteria to board the train!')

print()
print('-----> Loops:')
print()

#1. Receives a natural number (positive integer).top and print all numbers in the range from 1 to top(inclusive).

top = int(input("Enter a natural number: "))

print('The list of numbers until top is: ', end=' ')
for _ in range(1, top +1):
    print(_, end=' ')
print()

#2. Take two integers and display all the integers between them (inclusive) in ascending order.
# It is not guaranteed that the second figure is greater than the first.

beg = int(input("Enter a number: "))
end = int(input("Enter a number: "))

if beg < end:
    print('The list of numbers is: ', end=' ')
    for _ in range(beg, end +1):
        print(_, end=" ")
elif beg > end:
    print('The list of reversed numbers is: ', end=' ')
    for _ in range(beg, end -1, -1):
        print(_, end=" ")
print()

#3.Enter a natural number: 'n'. Display all even numbers from 0 to n(inclusive). Not guaranteed that n is even.

n = int(input("Enter a natural number: "))

print(f'The list of natural numbers is: ', end=' ')
for _ in range(0, n +1, 2):
#from 0 to n, creates the limits of the numbers. +1 so it includes n, and 2 so it prints only the even numbers.
    print(_, end=' ')
print()

#4. Input two natural numbers max and den.  Display all natural numbers up to max(inclusive).
# which are divided by den.   It is not guaranteed that max itself is divisible by den.

max_ = int(input('Enter a number: '))
den = int(input('Enter a number: '))

print(f'This is a list of all numbers up to {max} that are divisible by {den}: ', end=' ')
for _ in range(0, max_ +1):
    if _ % den == 0:
        print(f'{_}', end=' ')
print()

print('-----> Data processing:')
print()

#1. Recive numbers until -99 is received and print their sum. If the first entry is -99 print None.

total = 0
numb = int(input('Enter a number(-99 to exit): '))

if numb == -99:
    print(None)
else:
    while numb != -99:
        total += numb
        numb = int(input('Enter a number(-99 to exit): '))
    print(f'The gross of all provided numbers is: {total}')

#2. Receive numbers until 0 or a negative number is collected. print the biggest and the smallest number.
#If the first entry is -99 print None.

numbs = int(input('Enter a number(-99 to exit: '))

if numbs == -99:
    print(None)
else:
    h = lo = numbs
    while True:
        numbs = int(input('Enter a number(-99 to exit): '))
        if numbs <= 0:
            break
        h = max(h, numbs)
        lo = min(lo, numbs)
    print(f"The biggest entered number is {h} and the lowest {lo}")

#3. Receive 5 numbers. Print the serial number of the highest value. For example if receives: -12, 5, 4, 99, 88
#The answer will be 4 because 99 we will get in the fourth input.

fiv_num = []

for _ in range(5):
    fiv_num.append(int(input('Enter a number: ')))

mx_v = max(fiv_num)
mx_indx = fiv_num.index(mx_v) +1

print(f'The bigger number was provided on attempt number: {mx_indx}')

#4."Capture 2 numbers and print the result of their multiplication using addition only."

d1 = int(input('Enter a number: '))
d2 = int(input('Enter a number: '))

result = 0

if d2 < 0:
    for _ in range(-d2):
        result -= d1

else:
    for _ in range(d2):
        result += d1

print(f'The result of the multiplication of {d1} and {d2} is: {result}!')

#5. "Pick 2 numbers and print their results of their exponentiation, using multiplication only."

d3 = int(input('Enter a number: '))
d4 = int(input('Enter a number: '))
result2 = 1

for _ in range(d4):
    result2 *= d3
print(f'{d3} raised to the power of {d4} is: {result2}')

#6. Challenge: Collect a number and a digit and print True if the digit is part of the number and False if doesn't.
#For example:
# -If 789 and 3 are received the answer is False. If 476 and 7 are received the answer is True.

number = input('Enter a number: ')
digit = input('Enter a digit: ')

if digit in number:
    print(f'{True}, {digit} is part of {number}!')

else:
    print(f'{False}, {digit} is not part of {number}!')


#7. Challenge: Input two numbers and print their greatest common divisor.
#- For example: The greatest common divisor of 60 and 72 is: 12.
import math

d5 = int(input('Enter a number: '))
d6 = int(input('Enter a number: '))

gcdOfD5_D6 = math.gcd(d5, d6)

print(f'The greatest common divisor of {d5} and {d6} is {gcdOfD5_D6} ')

"""8. A prime number is a number that is divisible only by itself and 1.
Write a program that receives a number and prints whether it is prime or not.
Hint: Run a loop with i from 2 up to the number and check if the number is divisible by i at any point.
If it is, the number is not prime. If no such divisor is found, the number is prime"""

d7 = int(input('Enter a number: '))
prime = True

for _ in range(2, d7):
    if d7 % _ == 0:
        prime = False
        break

if prime and d7 > 1:
    print(f'{d7} is a prime number!')

else:
    print(f'{d7} is not prime!')
print()

print('-----> Complex Loops:')
print()

#There are 12 cards. Insert the average temperature in the Tel Aviv area every month in 2023,
# know that the temperature in Tel Aviv is never above 40° and never drops below -5°.  Accept the cards
#and check if a wrong card did not fall in the input, if so stop and print "wrong data" if not print "correct data".
#- Add try and except in case that the provided data is not a number.
#-Save all the values on a list.
#- If 0 is entered twice in a row, the user will receive "Error" Enter again:
#- Calculate the annual average temperature.
#- Print the highest temperature on a list and the lowest temperature.

temps_tlv = []
twice_zero = False

while True:
    temps_tlv.clear()

    for month in range(1, 13): #to request 12 inputs
        try:
            temp = float(input(f"Provide the temperature for month {month} in Tel Aviv area: "))

            if temp < -5 or temp > 40:
                print("wrong data")
                break

            if temp == 0 and twice_zero: #checks if 0 was entered twice in a row
                print(f'Error, try again: ')
                break
            if temp == 0:
                twice_zero = True

            temps_tlv. append(temp)

        except ValueError:
            print("wrong data")
            break

    if len(temps_tlv) == 12:
        yearly_2023_average = sum(temps_tlv) / len(temps_tlv)
        higest = max(temps_tlv)
        lowest = min(temps_tlv)
        print(f'During 2023 the higher temperature in the city of Tel Aviv was {higest}, the lowest {lowest} with an average of: {yearly_2023_average}°C')
        break