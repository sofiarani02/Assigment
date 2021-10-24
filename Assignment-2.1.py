# get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26}


print(my_dict['name'])
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# Output None
print(my_dict.get('address'))

#update value
my_dict['age'] = 27
print(my_dict)

# add item
my_dict['address'] = 'Downtown'
print(my_dict)

# remove a particular item, returns its value
print(my_dict.pop('age'))
print(my_dict)

# add item
my_dict['gender'] = 'Female'
print(my_dict)

#copy of dictionary
print(my_dict.copy)

# remove an arbitrary item, return (key,value)
print(my_dict.popitem())
print(my_dict)

# Dictionary Comprehension with if conditional
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)
      
print(1 in odd_squares)
print(2 not in odd_squares)
print(40 in odd_squares)

# Printing keys of dictionary
print(odd_squares.keys())

#setdefault()
value=odd_squares.setdefault('3')
print(value)

#values()
print(odd_squares.values())

#my-dict()
my_dict.update(odd_squares)
print(my_dict)

# remove all items
my_dict.clear()
print(my_dict)

# delete the dictionary itself
del my_dict

#for loop step function
print("____Step function____")
step = int(input('Enter step value : '))
 
list_1 = [9, 5, 7, 2, 5, 3, 8, 14, 6, 11, 75, 24, 55, 98]
 
for i in range(0, len(list_1), step) :
    print(list_1[i])

#To print Full Pyramid Pattern of Stars(*)
for i in range(4):
    for s in range(-5, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()
