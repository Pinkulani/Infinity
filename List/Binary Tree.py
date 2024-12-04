# © Pinkulani 2024

class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Left = None
        self.Right = None

    def SearchInorder(self, Thing):
        if self.Left != None and self.Left.SearchInorder(Thing):
            return True
        if self.Data == Thing:
            return True
        if self.Right != None and self.Right.SearchInorder(Thing):
            return True
        
        return False
    
    def SearchPreorder(self, Thing):
        if self.Data == Thing:
            return True
        if self.Left != None and self.Left.SearchPreorder(Thing):
            return True
        if self.Right != None and self.Right.SearchPreorder(Thing):
            return True
        
        return False
    
    def SearchPostorder(self, Thing):
        if self.Left != None and self.Left.SearchPostorder(Thing):
            return True
        if self.Right != None and self.Right.SearchPostorder(Thing):
            return True
        if self.Data == Thing:
            return True
        
        return False

class Tree:
    def __init__(self):
        self.Root = None