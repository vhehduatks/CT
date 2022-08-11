from mimetypes import init
import sys
read=sys.stdin.readline
N=int(read())
class node():
    def __init__(self,parent,left,right):
        self.parent=parent
        self.left=left
        self.right=right

def preorder(node:node):
    if not node:return
    print(node.parent,end='')
    preorder(tree.get(node.left,None))
    preorder(tree.get(node.right,None))
    pass

def inorder(node:node):
    if not node:return
    inorder(tree.get(node.left,None))
    print(node.parent,end='')
    inorder(tree.get(node.right,None))
    pass

def postorder(node:node):
    if not node:return
    postorder(tree.get(node.left,None))
    postorder(tree.get(node.right,None))
    print(node.parent,end='')
    pass 

tree={}

for _ in range(N):
    P,L,R=map(str,read().strip().split())
    tree[P]=node(P,L,R)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])