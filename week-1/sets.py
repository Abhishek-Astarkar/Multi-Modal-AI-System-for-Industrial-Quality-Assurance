d={} # empty dictionary
print(type(d))
empty = set() # this is an empty set
print(type(empty))
# set is unordered
myset = {"car","chair",37,True} # set is dict without keys
print(myset)
print(len(myset)) # prints length of set

# Set methods:

myset.add("okay") # adds an element
print(myset)

myset.remove("okay") # deletes that element
print(myset)

myset.pop() # randomly drops any element of the set
print(myset)

myset.clear() # formats the set
print(myset) # prints set()

# Union and Intersection

s1={1,2,3}
s2={3,4,5}

print(s1.union(s2)) # prints the union of two sets

print(s1.intersection(s2)) # prints the intersection of two sets
