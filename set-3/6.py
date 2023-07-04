# 7. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, value):
        self.q1.put(value)

    def pop(self):
        if self.q1.empty():
            return None
        
        # Move elements from q1 to q2, except the last one
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        # Remove and return the last element from q1
        popped = self.q1.get()

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

        return popped

# Main program
stack = Stack()

stack.push(1)
stack.push(2)
print(stack.pop())
stack.push(3)
print(stack.pop())
print(stack.pop())
