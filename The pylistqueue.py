# Implementatin of the Queue ADT using a python list

class Queue:
    # Creates en empty queue
    def __init__(self):
        self._qList = list()
    # Returns True if the queue is empty
    def isEmpty(self):
        return len(self) == 0
    # Returns the numbers of items in the queu

    def __len__(self):
        return len(self._qList)

    # Adds the given item to the queue

    def enqueue(self, item):
        self._qList.append(item)

    # Removes and returns the first item ithe queur

    def deque(self):
        assert not self.isEmpty(), "Cannot dequeu from an empty queue"
        return self._qList.pop( 0 )    
        

PROMPT = "Enter an int value (< 0 to end data entry:)"
myQueue = Queue() 
value = int(input(PROMPT)) 

while value >= 0:    
    myQueue.enqueue(value)  
    value = int(input(PROMPT))
while not myQueue.isEmpty(): 
    value = myQueue.deque() 
    print("  ---> ", value)