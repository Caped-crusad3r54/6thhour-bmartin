#Name:
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
superhero_dictionary = {
    "captain america" : "Steve Rogers",
            "ironman" : "tony stark",
             "batman" : [1,2,3]
}
#3. Print the keys of the dictionary from #2.
print(superhero_dictionary.keys())
#4. Print the values of the dictionary from #2
print(superhero_dictionary.values())
#5. Print one of the three numbers from the list by itself
print(superhero_dictionary["batman"][0])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
superhero_dictionary.update({"spider-man" : "peter parker"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(superhero_dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
huxley_dictionary = {
    "huxley_1" : {
        "name" : "nate",
        "year" : 2011,
    "last_name": "shaw",
},
    "huxley_2" : {
        "name" : "huxley",
        "year" : 2010,
        "last_name" : "harmon",
    },
    "huxley_3" : {
        "name" : "owen",
        "year" : 2011,
        "last_name" : "jones",
    }}
#9. Print the names of all three classmates on the same line.
print(huxley_dictionary["huxley_1"]["name"],huxley_dictionary["huxley_2"]["name"],huxley_dictionary["huxley_3"]["name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
huxley_dictionary.pop("huxley_1")
print(huxley_dictionary)