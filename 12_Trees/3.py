# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def check(root, min_, max_):
    return (root is None or (min_ < root.data < max_ and check(root.left, min_, root.data) and check(root.right, root.data, max_)))

def checkBST(root):
    return check(root, -float('inf'), float('inf'))