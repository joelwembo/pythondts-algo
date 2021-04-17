class LinkedStack:
    # LIFO Stack implementation using a singly linked list for storage
    class _Node:
        #Lightweight nonpublic class for storing a singly linked node
        __slots__ = '_element', '_next'

        def __init__(self,element, next):
            self._element = element
            self._next    = next

    def __init__(self):
            # Create an empty
            self._head = None
            self._size = 0
    def __len__(self):
            return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
            # Add element e to the top of stack
        self._head = self._Node(e, self._head) # create and link a new node
        self._size += 1
        
    def top(self):
        """Return (but do not remove) the ement at the top of stack
        Raise EMpty exception of the stack is empty """

        if self.is_empty():
            raise ('Stack is empty')
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack """
        if self.is_empty():
            raise ('Stack is empty')
        answer = self._head._element 
        self._head = self._head._next
        self._size -= 1
        return answer
        
        




