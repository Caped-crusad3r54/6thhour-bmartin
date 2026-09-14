#Name:brody martin
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!
print("hello world")
#1. Create a list with 5 strings containing 5 different names in it.
list_of_names=["Nate", "Brody", "Owen", "Jacob", "Mach"]
#2. Append a new name onto the Name List.
list_of_names.append("cody")
#3. Print out the 4th name on the list.
print(list_of_names[3])
#4. Create a list with 4 different integers in it.
list_of_int=[1,2,3,4,5]
#5. Insert a new integer into the 2nd spot and print the new list.
list_of_int.insert(1,3)
print(list_of_int)
#6. Sort the list from lowest to highest and print the sorted list.
list_of_int.sort()
print(list_of_int)
#7. Add the 1st three numbers on the sorted list together and print the sum.
intVar1=list_of_int[0]+list_of_int[1]+list_of_int[2]
print(intVar1)
#8. Create a list with two strings, two variables, and two boolean values.
cat=[2, 3, "2", "3",True, False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(cat[int(input("give me a number"))])