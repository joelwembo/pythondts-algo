# pythondts-algo
Data Structures and Algorithms Using Python. Computer Science Subject

Summary
Lists, sets, and tuples are the basic data structures in the Python programming language.
One of the differing points among the data structures is mutability, which is the ability to change an object after its creation.
Lists and tuples are the most useful data types, and they can be found in virtually every Python program.
 

Python Data Structures – Lists
A list is defined as an ordered collection of items, and it is one of the essential data structures when using Python to create a project. The term “ordered collections” means that each item in a list comes with an order that uniquely identifies them. The order of elements is an inherent characteristic that remains constant throughout the life of the list.

Since everything in Python is considered an object, creating a list is essentially creating a Python object of a specific type. When creating a list, all the items in the list should be put in square brackets and separated by commas to let Python know that a list has been created. A sample list can be written as follows:

List_A = [item 1, item 2, item 3….., item n]

 

Lists can be nested
A list can be nested, which means that it can contain any type of object. It can include another list or a sublist – which can subsequently contain other sublists itself. There is no limit to the depth with which lists can be nested. An example of a nested list is as follows:

List_A = [item 1, list_B, item 3….., item n]

 

Lists are mutable
Lists created in Python qualify to be mutable because they can be altered even after being created. A user can search, add, shift, move, and delete elements from a list at their own will. When replacing elements in a list, the number of elements added does not need to be equal to the number of elements, and Python will adjust itself as needed.

It also allows you to replace a single element in a list with multiple elements. Mutability also enables the user to input additional elements into the list without making any replacements.

 

For more information about lists and other Python data structures, please see CFI’s Machine Learning for Finance – Python Fundamentals course.

 

Python Data Structures – Tuples
A tuple is a built-in data structure in Python that is an ordered collection of objects. Unlike lists, tuples come with limited functionality.

The primary differing characteristic between lists and tuples is mutability. Lists are mutable, whereas tuples are immutable. Tuples cannot be modified, added, or deleted once they’ve been created. Lists are defined by using parentheses to enclose the elements, which are separated by commas.

The use of parentheses in creating tuples is optional, but they are recommended to create a distinction between the start and end of the tuple. A sample tuple is written as follows:

tuple_A = (item 1, item 2, item 3,…, item n)

 

Empty and One Single Item Tuple
When writing a tuple with only a single element, the coder must use a comma after the item. This is done to enable Python to differentiate between the tuple and the parentheses surrounding the object in the equation. A tuple with a single item can be expressed as follows:

some_tuple = (item 1, )

If the tuple is empty, the user should include an empty pair of parentheses as follows:

Empty_tuple= ( )

 

Why Tuples are Preferred over Lists
Tuples are preferred when the user does not want the data to be modified. Sometimes, the user can create an object that is intended to remain intact during its lifetime. Tuples are immutable, so they can be used to prevent accidental addition, modification, or removal of data.

Also, tuples use less memory, and they make program execution faster, as compared to using lists. Lists are slower than tuples because every time a new execution is done with lists, new objects are created and the objects are not interpreted just once. Tuples are identified by Python as one immutable object. Hence, they are built as one single entity.

 

Python Data Structures – Sets
A set is defined as a unique collection of unique elements that do not follow a specific order. Sets are used when the existence of an object in a collection of objects is more important than the number of times it appears or the order of the objects. Unlike tuples, sets are mutable – they can be modified, added, replaced, or removed. A sample set can be represented as follows:

set_a = {“item 1”, “item 2”, “item 3”,….., “item n”}

 

One of the ways that sets are used is when checking whether or not some elements are contained in a set or not. For example, sets are highly optimized for membership tests. They can be used to check whether a set is a subset of another set and to identify the relationship between two sets.

 
