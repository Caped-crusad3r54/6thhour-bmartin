#Name:Brody martin
#Class: 6th Hour
#Assignment: HW14
import random
import math

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i=5
while i >= 1:
    print(i)
    i -= 1
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
x = 1
while x <= 30:
    if x % 2 == 0:
        print(x)
    x += 1
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
b = 1
while b <= 30:
    if b % 3 == 0:
        print(b)
    b += 1
    continue
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
z = random.randint(1, 6)
while True:
    Z = random.randint(1, 6)
    print(z)
    if z == 1:
        break
#5. Create a while loop that asks for a number input until the user inputs the number 0.
u = int(input("Give me a number: "))
while u != 0:
    u = int(input("Give me a number: "))

