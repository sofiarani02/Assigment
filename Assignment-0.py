"""
**Write Algorithm for finding x and y from the given sequence:
10 1 8 3 6 5 4 7 x y **

Step 1: Start.
Step 2: All elements are assigned to variable lst[], which is list.
        lst = [['10','1','8','3','6','5','4','7','x','y']
Step 3: Use linearsearch function, where lst and element to be searched as parameters.
        def linearsearch(lst, a):
Step 4: Use for loop to iterate till the length of lst.
        for i in range(len(lst)):
Step 5: If a matches with any of the element, return the index value.
Step 6: If a doesn’t match with any of elements in lst[] ,
        print("The element not found.")
Step 7: End.
"""


def linearsearch(lst, a):
   for i in range(len(lst)):
      if lst[i] == a:
         return i
   print("The element not found.")
   return -1
lst = ['10','1','8','3','6','5','4','7','x','y']
a = input("Enter element to search: ")
print("Element found at index "+str(linearsearch(lst,a)))
