# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem

def fibonacci(n): return round((((1+(5**0.5))/2)**n)/(5**0.5))
n = int(input())
print(fibonacci(n))