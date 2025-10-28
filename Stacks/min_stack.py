class minstack:
    def __init__(self):
        self.stack =[]
        self.min_stack =[]

    def push(self,val=int):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]
    
    def getmin(self):
        return self.min_stack[-1]
        