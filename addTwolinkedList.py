class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
# Parameters:
#  list1: LinkedList
#  list2: LinkedList
# return type: LinkedList

def addTwoLinkedLists(list1, list2):
    newLinkedList = LinkedList()
    nextA = list1.head
    nextB = list2.head
    head = None
    current = None
    carrieOver = 0
    while nextA is not None or nextB is not None or carrieOver > 0:
        valueA = nextA.data if nextA else 0
        valueB = nextB.data if nextB else 0
        data = valueA + valueB + carrieOver
        carrieOver = data // 10
        cleanData = data % 10
        nextA = nextA.next if nextA else None
        nextB = nextB.next if nextB else None
        newNode = Node(cleanData)

        if current is None:
            current = newNode
        else:
            current.next = newNode
            current = newNode

        if head is None:
            head = current
    
    
        
    newLinkedList.head = head
    
    return newLinkedList

def printLinkedList(linkedList):
    head = linkedList.head
    list = []
    while head is not None:
        list.append(head.data)
        head = head.next
    
    return list

def main():
    list1 = LinkedList( Node(5, Node(2, Node(6, Node(8)))))
    list2 = LinkedList( Node(1, Node(7, Node(5, Node(6)))))
    result = addTwoLinkedLists(list1, list2)
    print(printLinkedList(result))

if __name__ == "__main__":
    main()

# 5 - 2 -6 -8
# 1 - 7 -5 -6
# 6  9 1  5 1
# 6 9 1  