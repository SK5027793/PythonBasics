"""
Tuples are ordered collection of items that are immutable. They are similar to lists but cannot be modified 
after creation. 
Tuples are defined using parentheses () and can contain elements of different data types.

"""

# Creating a tuple
empty_tuple= ()
print(empty_tuple)
print(type(empty_tuple))

number=tuple([1, 2, 3 , 4, 5, 3, 5]) # we can also create a tuple using the tuple() constructor and passing an iterable (like a list) as an argument.
print(number)
print(type(number))

lst=list((6, 7, 8, 9, 10)) # we can also create a list using the list() constructor and passing an iterable (like a tuple) as an argument.
print(lst)
print(type(lst))

mixed_tuple= (1, "Hello", 3.14, [1, 2, 3], (4, 5, 6))
print(mixed_tuple)

#Accessing elements in a tuple
print(mixed_tuple[2])
print(mixed_tuple[-1])
print(mixed_tuple[2:4])
print(mixed_tuple[::-1]) # reverse the tuple


#tupl operations
# Concatenation

concat = number+ mixed_tuple 
print(concat)
"""
we can concatenate two tuples using the + operator, 
which creates a new tuple that contains all the elements of both tuples.

"""

print(number*3) 
"""
we can also repeat a tuple using the * operator, which creates a new tuple that 
contains the elements of the original tuple repeated a specified number of times.

"""

##Immutable nature of Tuples
# Tuples are immutable, which means that once a tuple is created, its elements cannot be modified.

#number[0] = 10 # This will raise a TypeError because tuples do not support item assignment.

#Tuple methods

print(number.count(3)) # returns the number of occurrences of a specified value in the tuple.
print(number.index(4)) # returns the index of the first occurrence of a specified value in the tuple. 
#If the value is not found, it raises a ValueError.

#Pcking and Unpacking Tuples
# Packing a tuple

packed_tuple= 2, "Hello", True, 3.14
print(packed_tuple)

#Unpacking a tuple
a, b, c, d= packed_tuple
print(a)
print(b)
print(c)
print(d)

#Unpacking with * operator
x, *y, z =packed_tuple
print(x)
print(y)
print(z)

#Nested Tuples

nestedlist= [[1, 2, 3, 4, 5], [True, "Student", 3.15], [8, 'g', 765, "Employee"] ,["Python", "Java", "C++"]]
nested_tuple= ((8, 'g', 765, "Employee") ,("Python", "Java", "C++"), nestedlist)
print(nestedlist)
print(nested_tuple)

print(nestedlist[3][2])
print(nested_tuple[2][3][0])#

for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item, end=" ")
    print()

