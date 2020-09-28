# Create a BST Node class
class BSTNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

# write the insert method 

    def insert(self,value):
        if value<=self.value:
            if self.left is None:
                self.left=BSTNode(value)
            else:
                self.left.insert(value)
        elif value>=self.value:
            if self.right is None:
                self.right =BSTNode(value)
            else:
                self.right.insert(value)

# write the contains method 

    def contains(self,target):
        if self.value == target:
            return True
        if target <= self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)


