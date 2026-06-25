a=(1,3,"straight",28.2,3.14159,3) # This is a tuple, its immutable like string
print(type(a)) # prints tuple
print(a)
count=a.count(3)
print(count) # prints the frequency of occurence of that element
index=a.index(3)
print(index) # prints the index of first occurence of that element
print(len(a)) # length can be find as in list and string
print(a[2]) # elements can be accessed
sl=a[3:5] # slicing is same as was in string and list
print(sl)
print(a+sl) # concatenation is allowed as in strings and lists
print(sl*3) # repetition is done by product sign
b=(j)
print(type(b)) # reads int
c=(2,)
print(type(c)) # singleton tuple needs comma to understand
