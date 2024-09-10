class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
    
    def push(self, element):
        if self.top == self.size - 1:
            print("Stack is overflow")
        else:
            self.top += 1
            self.stack[self.top] = element
    
    def pop(self):
        if self.top == -1:
            print("Stack is underflow")
        else:
            print(f"{self.stack[self.top]} is deleted")
            self.top -= 1
    
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print(f"The top element is: {self.stack[self.top]}")
    
    def display(self):
        if self.top == -1:
            print("Stack is underflow")
        else:
            print("Elements of stack:")
            for i in range(self.top, -1, -1):
                print(f"{self.stack[i]}")
obj = Stack(3)
obj.push(10)
obj.push(20)
obj.push(30)
obj.pop()
obj.peek()
obj.display()
