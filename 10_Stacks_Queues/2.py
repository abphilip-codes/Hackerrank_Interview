# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

class MyQueue(object):
    def __init__(self):
        self.one = []
        self.two = []
    def peek(self): return self.two[-1] 
    def pop(self): return self.two.pop()  
    def put(self, value): self.one.append(value)  
    def check(self):
        if not len(self.two):
            while self.one: self.two.append(self.one.pop())

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    queue.check()
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())