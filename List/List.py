# © Pinkulani 2024

class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

class LinkedList:
    def __init__(self):
        self.Head = None

    def Add(self, Data):
        if self.Head == None:
            self.Head = Node(Data)
        else:
            Current = self.Head
            while Current.Next != None:
                Current = Current.Next
            
            Current.Next = Node(Data)

    def Remove(self, Index: int):
        if self.Head == None:
            print("List is empty")

        if Index == 0:
            self.Head = self.Head.Next
        else:
            Current = self.Head
            Counter = 0
            while Current.Next != None and Counter != (Index - 1):
                Counter += 1
                Current = Current.Next
        
            Current.Next = Current.Next.Next
            
    def Display(self):
        if self.Head == None:
            print("List is empty")
        else:
            Current = self.Head
            print(Current.Data)
            while Current.Next != None:
                Current = Current.Next
                print(Current.Data)
