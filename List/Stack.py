# © Pinkulani 2024

class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

class Stack:
    def __init__(self):
        self.Head = None

    def Push(self, Data):
        Current = self.Head
        self.Head = Node(Data)
        self.Head.Next = Current

    def Pop(self):
        if self.Head == None:
            print("Stack is empty")
        else:
            Next = self.Head.Next
            self.Head = Next
    
    def Display(self):
        if self.Head == None:
            print("Stack is empty")
        else:
            Current = self.Head
            print(Current.Data)
            while Current.Next != None:
                Current = Current.Next
                print(Current.Data)