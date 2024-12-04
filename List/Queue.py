# © Pinkulani 2024

class Node:
    def __init__(self, Data):
        self.Data = Data
        self.Next = None

class Queue:
    def __init__(self):
        self.Head = None

    def Enqueue(self, Data):
        if self.Head == None:
            self.Head = Node(Data)
        else:
            Current = self.Head
            while Current.Next != None:
                Current = Current.Next

            Current.Next = Node(Data)

    def Dequeue(self):
        if self.Head == None:
            print("Queue is empty")
        else:
            self.Head = self.Head.Next

    def Display(self):
        if self.Head == None:
            print("Queue is empty")
        else:
            Current = self.Head
            print(Current.Data)
            while Current.Next != None:
                Current = Current.Next
                print(Current.Data)