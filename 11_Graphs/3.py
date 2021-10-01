# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

import queue
from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.e = defaultdict(lambda: [])
        
    def connect(self,x,y):
        self.e[x].append(y)
        self.e[y].append(x)
        
    def find_all_distances(self, r):
        d = [-1 for i in range(self.n)]
        u = set([i for i in range(self.n)])
        q = queue.Queue()
        d[r] = 0
        u.remove(r)
        q.put(r)

        while(q.empty()!=True):
            node = q.get()
            c = self.e[node]
            h = d[node]
            for z in c:
                if z in u:
                    d[z] = h+6
                    u.remove(z)
                    q.put(z)
        d.pop(r)
        print(" ".join(map(str,d)))
        
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)