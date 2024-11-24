class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

class List:
    def __init__(self):
        self.Head = None

    def Append(self, Data):
        if self.Head == None:
            self.Head = Node(Data)
        else:
            Current = self.Head
            while Current != None:
                Current = Current.Next
            
            Current.Next = Node(Data)