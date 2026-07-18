random={
   "Abhishek": 7.3,
   "Kamal": 7.2,
   "thala":[2010,2011,2018,2021,2023],
   2013:"Rohit"
}
# We can add any variable type elements in dictionary
# The biggest advantage of a dictionary is that we can pair/associate things
# The indexing is different here, its defined by keys i.e, by Abhishek,Kamal, thala etc.

# Dictionaries are UNORDERED,MUTABLE,INDEXED,CANT CONTAIN DUPLICATE KEYS

print(type(random)) # prints dict class

print(random["Abhishek"]) # prints 7.3, KEY ERROR IF KEY ISNT PRESENT
print(random["thala"]) # prints list

print(random) # prints dictionary 
print(random.items()) # prints dict_items, after that prints dictionary in tuple form

print(random.keys()) # prints dict_keys, after that prints keys

print(random.values()) # prints dict_values, after that prints values of keys

random.update({ "thala" : 7, 2018: "Russel"}) # updates the dict by changing existing keys and adding new keys if not present
print(random) # confirms mutability of dict

print(random.get(2013)) # prints the value corresonding to that key
print(random.get(0)) # PRINTS None

print(len(random)) # prints length of dict


