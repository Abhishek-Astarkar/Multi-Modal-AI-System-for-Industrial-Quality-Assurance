ipl=["Teams",7,True,"Thala",19.1]
print(ipl)
print("Thala" in ipl ) # Used to check if an element is in the list, returns true or false
ipl[3]="Dhoni"
print(ipl)
num=[1,8,3,3,9,367,74,8,16,97]
num.sort()#sorts numbers list and changes the initial list, i.e, lists are mutable
print(num)
num.append(39)
print(num)#adds the element to the end
num.reverse()
print(num)#reverses the list
num.insert(3,89)#inserts no. at that index
print(num)
print(num.pop(1))#prints popped number or element at that index
print(num)#prints list without that popped element
num.remove(8)#deletes that element from list, NOTE: it only delets one element at a time, according to index
print(num)
print(type(num))#lists is a type
sl=num[2:8]#slicing same as in strings and tuples
print(sl)
b=[2,3]
print(num+b)#concatenation is allowed as in string and tuple
print(b*111)#repetiton same as was for strings and tuples
