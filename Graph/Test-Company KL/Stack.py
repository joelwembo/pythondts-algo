#Python Program to demonstrate Stack ADT

class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)    
    
PROMPT = "Enter an int value (< 0 to end data entry:)"
myStack = Stack()  # Instance of the Stack Class
value = int(input(PROMPT)) # receive input from the user

while value >= 0:     # Condition to loop the operation entil the user end the program with a negative number
    myStack.push(value)  # push(item) Adds the given item to the top of the stack.
    value = int(input(PROMPT)) # continue the looping of receiving new items...
while not myStack.isEmpty(): # Checking if the stack is not empty, meaning no entries at all
    value = myStack.pop()  #pop(): Removes and returns the top item of the stack, if the stack is not empty.
    print("Index:" , myStack.size(), "  ---> ", value)   # Display the each element with it index on top from to bottom     