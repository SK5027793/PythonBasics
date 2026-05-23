##Lists are ordered and mutable collection of items allows duplicates
##They can contain items of different data types

lst=[]
print(type(lst)) #Emptylist

mixed_lst1=["Swati", 567, 9.898, True ]
print(mixed_lst1)
print(type(mixed_lst1))

##Accessing list items using index
print(mixed_lst1[0]) #First item

print(mixed_lst1[2]) #Third item
print(mixed_lst1[-1])#Last item

print(mixed_lst1[1:3])


fruits= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits)
print(fruits[2:5]) ##From index 2 to 4

fruits[3]="watermelon"

print(fruits)

fruits[1:4]=["blueberry", "grape", "peach"]
print(fruits)

fruits[5:7]="papaya" #This will replace the items at index 5 and 6 with papaya and remove the extra item

print(fruits)

fruits= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

fruits.insert(3, "strawberry") #This will insert strawberry at index 3 and shift the rest of the items to the right
print(fruits)

fruits.append("pineapple") #This will add pineapple at the end of the list
print(fruits)

popped_fruit= fruits.pop() #This will remove the last item from the list and return it
print(popped_fruit)
print(fruits)

indexch=fruits.index("cherry")
print("Index of cherry:", indexch)

fruits. insert(2, "banana")
print(fruits)

fruits.count("banana") #This will count the number of times banana appears in the list
print("Count of banana:", fruits.count("banana"))

fruits.reverse() #This will reverse the order of the items in the list
print("Fruits after reversing:", fruits)

fruits.sort() #This will sort the items in the list in ascending order
print(fruits)

for index, fruit in enumerate(fruits):
    print(index, fruit)

fruits.clear() #This will remove all the items from the list
print("Fruits after clearing:", fruits)

##=====================================Slicing Of Lists =======================================================

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[2:7]) #From index 2 to 6
print(numbers[:5]) #From the beginning to index 4
print(numbers[5:]) #From index 5 to the end
print(numbers[:]) #All items
print(numbers[::2]) #Every second item
print(numbers[1:8:2]) #From index 1 to 7, every second item
print(numbers[::-1]) #Reverse the list


##=====================List Iteration========================================================

for number in numbers:
    print(number)

for index, number in enumerate(numbers):
    print(index, number)    


##=====================List Comprehension========================================================
lst=[]
for x in range(10):
    lst.append(x**2)
print(lst)

##Basic Syntax [expression for item in iterable]

squaredlist=[x**2 for x in range(10)]
print(squaredlist)    

##with condition [expression for item in iterable if condition]

even_squares=[x**2 for x in range(20) if x%2==0]
print(even_squares)

even_num=[x for x in range(100) if x%2==0]
print("Even numbers from 1 to 100:", even_num)

odd_num=[x for x in range(100) if x%2!=0]
print("Odd numbers from 1 to 100:", odd_num)


##=====================Nested List Comprehension========================================================

lst1=[1, 2, 3, 4]
lst2=['a', 'b', 'c', 'd']

pair=[(i, j) for i in lst1 for j in lst2]
print(pair)


##========================List comprehension with functions call===========

words=["hello", "swati", "Good", "Morning"]
lengths=[len(word) for word in words]       
print(lengths)

"""
Conclusion: Lists are versatile data structures in Python that allow us
to store and manipulate collections of items. They support various operations 
such as indexing, slicing, appending, inserting, and more. 
List comprehensions provide a concise way to create new lists based on existing
iterables, making code more readable and efficient.
"""

