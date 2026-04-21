class Stack:
    def __init__(self):
        self.stack = [] 
        
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed into stack")

    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            item = self.stack.pop()
            print(f"{item} popped from stack")
            return item


s = Stack()
s.safe_pop()       # Stack is empty
s.push(10)         # Push 10
s.push(20)         # Push 20
s.safe_pop()       # Pops 20
