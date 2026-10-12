#Name:Brody martin
#Class: 6th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("hello world")
#2. Create a list with three values that each randomly generate a number between 1 and 100
numb_list=[random.randint(1,100),random.randint(1,100),random.randint(1,100)]
#3. Print the list.
print(numb_list)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if numb_list[0]>numb_list[1] and numb_list[0]>numb_list[2]:
    print("0 is higher")
elif numb_list[1]>numb_list[0] and numb_list[1]>numb_list[2]:
    print("1 is higher")
elif numb_list[2]>numb_list[0] and numb_list[2]>numb_list[1]:
    print("2 is higher")
#5. Tie the result (the largest number) from #4 to a variable called "num".
num=max(numb_list[0],numb_list[1],numb_list[2])
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    print("num is divisible by 2")
elif num % 3 == 0:
    print("num is divisible by 3")
elif num % 2 == 0 and num % 3 == 0:
    print("num is divisible by both")