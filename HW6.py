#Name:Brody martin
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
Dog=[2,1,4,6,8,5,9,7,3]
#2. Sort the list from highest to lowest.
Dog.sort(reverse=True)
#3. Create an empty list.
cat=[]
#4. Remove the median number from the first list and add it to the second list.
Bird=Dog.pop(4)
cat.append(Bird)
#5. Remove the first number from the first list and add it to the second list.
Lion=Dog.pop(0)
cat.append(Lion)
#6. Print both lists.
print(cat, Dog)
#7. Add the two numbers in the second list together and print the result.
Tiger=cat[0]+cat[1]
print(Tiger)
#8. Add the sum from #7 to the first list.
Dog.append(Tiger)
#9. Sort the first list from lowest to highest and print it.
Dog.sort()
print(Dog)