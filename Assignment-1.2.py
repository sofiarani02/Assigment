print("***Python code for List operation***\n")

# declaring a list of integers
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# List slicing operations
# printing the complete list
print('myList: ',myList)
# printing first element 
print('first element: ',myList[0]) 
# printing fourth element 
print('fourth element: ',myList[3]) 
# printing list elements from 0th index to 4th index
print('myList elements from 0 to 4 index:',myList[0: 5]) 
# printing list -7th or 3rd element from the list
print('3rd or -7th element:',myList[-7]) 


# appending an element to the list
myList.append(111)
print('myList after append():',myList)

# finding index of a specified element 
print('index of \'80\': ',myList.index(80))

# sorting the elements of iLIst
myList.sort()
print('after sorting: ', myList);

# popping an element
print('Popped elements is: ',myList.pop())
print('after pop(): ', myList);

# removing specified element
myList.remove(80)
print('after removing \'80\': ',myList)

# inserting an element at specified index 
# inserting 100 at 2nd index 
myList.insert(2, 100)
print('after insert: ', myList)

# counting occurances of a specified element
print('number of occurences of \'100\': ', myList.count(100))

# extending elements i.e. inserting a list to the list
myList.extend([11, 22, 33])
print('after extending:', myList)

#reversing the list
myList.reverse()
print('after reversing:', myList)

#clearing the list
myList.clear()
print('after clearing:', myList)

print("\n*********************************************\n")

print("***Python code for String operation***\n")

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
