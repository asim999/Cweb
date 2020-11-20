class Node:
 def __init__(self,data):
     self.next = None
     self.data = data
class List:
    def __init__(self):
        self.head = None
    def insert(self,data):
        print("Inserting",data)
        if self.head is None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def prinlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=' ')
            temp = temp.next


def main():
    list = List()
    for _ in map(list.insert,input("Enter list element").split(" ")):
        pass
    list.prinlist()

if __name__ == '__main__':
    main()
