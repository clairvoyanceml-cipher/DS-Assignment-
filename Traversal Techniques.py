#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Python program to for tree traversals 
  
# A class that represents an individual node in binary tree

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
  
def inorder(root):        # (left, root, right)
  
    if root: 
  
        # First recur on left child 
        inorder(root.left) 
  
        # then print the data of node 
        print(root.val)
  
        # now recur on right child 
        inorder(root.right) 
  
  
def postorder(root):      # (root, left, right)     
  
    if root: 
  
        # First recur on left child 
        postorder(root.left) 
  
        # the recur on right child 
        postorder(root.right) 
  
        # now print the data of node 
        print(root.val)
        
  
def preorder(root):      # (left, right, root)
  
    if root: 
  
        # First print the data of node 
        print(root.val) 
  
        # Then recur on left child 
        preorder(root.left) 
  
        # Finally recur on right child 
        preorder(root.right)
        
        
        
# Test driver code

root = Node(5) 
root.left      = Node(2) 
root.right     = Node(8) 
root.left.left  = Node(18) 
root.left.right  = Node(16)
root.right.left = Node(23)

print("Preorder traversal of binary tree is")
preorder(root) 
  
print("\nInorder traversal of binary tree is")
inorder(root) 
  
print("\nPostorder traversal of binary tree is")
postorder(root)


# In[ ]:




