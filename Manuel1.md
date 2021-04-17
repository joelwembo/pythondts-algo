Stack
The stack is a last-in, first-out data structure. The developer can use the stack in the following use cases.

Expression evaluation and syntax parsing.
Finding the correct path in a maze using backtracking.
Runtime memory management.
Recursion function.
Queue
The queue is a first in, first-out (FIFO) data structure. The developer can use Queue in the following use cases.

Use a queue when the developer wants an order.
Processed in First In First Out order.
If the developer wants to add or remove both ends, they can use the queue or a double-ended queue.
-----------------------------------------------------------------------------------------------------

A stack is a data structure that stores a linear collection of items with access
limited to a last-in first-out order. Adding and removing items is restricted to one
end known as the top of the stack. An empty stack is one containing no items.
 Stack(): Creates a new empty stack.
 isEmpty(): Returns a boolean value indicating if the stack is empty.
 length (): Returns the number of items in the stack.
 pop(): Removes and returns the top item of the stack, if the stack is not empty.
Items cannot be popped from an empty stack. The next item on the stack
becomes the new top item.
 peek(): Returns a reference to the item on top of a non-empty stack without
removing it. Peeking, which cannot be done on an empty stack, does not
modify the stack contents.
 push( item ): Adds the given item to the top of the stack.

Class and Functions of Stack ADT

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


------------------------------------------------------------------------------------------------------------------
A QUEUE ADT

A queue is a data structure that a linear collection of items in which access is
restricted to a first-in first-out basis. New items are inserted at the back and
existing items are removed from the front. The items are maintained in the order
in which they are added to the structure.
 Queue(): Creates a new empty queue, which is a queue containing no items.
 isEmpty(): Returns a boolean value indicating whether the queue is empty.
 length (): Returns the number of items currently in the queue.
 enqueue( item ): Adds the given item to the back of the queue.
 dequeue(): Removes and returns the front item from the queue. An item cannot be dequeued from an empty queue.