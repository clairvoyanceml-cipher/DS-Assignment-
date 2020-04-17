#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Breadth First

# A node structure 
class Node: 
  
    # A utility function to create a new node 
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None
  
  
# Function to  print level order traversal of tree 
def BreadthFirst(root): 
    h = height(root) 
    for i in range(1, h+1): 
        Level(root, i) 
  
  
# Print nodes at a given level 
def Level(root , level): 
    if root is None: 
        return
    if level == 1: 
        print("%d" %(root.data)) 
    elif level > 1 : 
        Level(root.left , level-1) 
        Level(root.right , level-1) 
  
  
"""Compute the height of a tree--the number of nodes 
    along the longest path from the root node down to 
    the farthest leaf node 
"""

def height(node): 
    if node is None: 
        return 0 
    else : 
        # Compute the height of each subtree  
        lheight = height(node.left) 
        rheight = height(node.right) 
  
        #Use the larger one 
        if lheight > rheight : 
            return lheight+1
        else: 
            return rheight+1
  
# Test driver code

root = Node(5) 
root.left = Node(2) 
root.right = Node(8) 
root.left.left = Node(10) 
root.left.right = Node(16)
root.right.right = Node(23)
  
print("Breadth First traversal of binary tree is :")
BreadthFirst(root) 


# In[ ]:




