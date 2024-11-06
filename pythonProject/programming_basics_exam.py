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
min = mov_min % 60

print(f'The duration of the movie was {hours} hour and {min} minutes!')
print()

print('-----> Loops:')
print()

#1. Receives a natural number (positive integer).top and print all numbers in the range from 1 to top(inclusive).

top = int(input("1. Enter a natural number: "))

for _ in range(1, top +1):
    print(_, end=' ')
print()
#2. Take two integers and display all the integers between them (inclusive) in ascending order.
# It is not guaranteed that the second figure is greater than the first.

beg = int(input("2. Enter a number: "))
end = int(input("2. Enter a number: "))

if beg < end:
    for _ in range(beg, end +1):
        print(_, end=" ")
elif beg > end:
    for _ in range(beg, end -1, -1):
        print(_, end=" ")
print()

print('-----> Data processing:')

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
#The answer will be 4 because 99 we will get in the fourth input

fiv_num = []

for _ in range(5):
    fiv_num.append(int(input()))

mx_v = max(fiv_num)
mx_indx = fiv_num.index(mx_v) +1

print(mx_indx)



