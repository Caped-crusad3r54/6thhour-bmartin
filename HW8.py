#Name: Brody Martin
#Class: 6th Hour
#Assignment: HW8


#1. Import the "random" library
import random
#2. print "Hello World!"
print("Hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
owl=random.randint(1,10)
crow=random.randint(1,10)
birds=random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(owl, crow, birds)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
owl=owl+2
crow=crow-4
birds=birds*1.5
#6. Print each result from #5 on the same line.
print(owl, crow, birds)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
list_of_var=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
list_of_var.sort()
print(list_of_var)
#9. Add together the highest three numbers in the list from #7 and print the result.
list_of_var=list_of_var[1]+list_of_var[2]+list_of_var[3]
print(list_of_var)
#10. Create a list with 5 names of other students in this class and print the list.
name_list=["hux", "brody", "nate", "owen", "jacob"]
print(name_list)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(name_list)
print(name_list)
#12. Print a random choice from the list of names from #10.
print(random.choice(name_list))
