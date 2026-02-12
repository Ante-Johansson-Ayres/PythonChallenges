

## Advanced

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


def put(newNode):
    global head
    global nodeNoCounter
    global maxCap
    newNode.next = head
    head = newNode
    nodeNoCounter += 1
    if nodeNoCounter > maxCap:
        deleteNode()
    return newNode

def deleteNode():
    global head
    global nodeNoCounter
    currentNode = head
    while True:
            if currentNode.next.next:
                currentNode = currentNode.next
            else:
                currentNode.next = None
                nodeNoCounter -= 1
                break

    return 1
def get(findKey):
    global head
    global maxCap
    oldNode = head
    currentNode = oldNode.next
    if oldNode.key == findKey:
            value = oldNode.value
            print("** Node found with key " + str(findKey) + " at position 0 with value " + str(value) + "\n")
            return value
    for i in range(maxCap):
        if currentNode and currentNode.key == findKey: 
            value = currentNode.value
            oldNode.next = currentNode.next
            currentNode.next = head 
            head = currentNode
            print("++ Node found with key " + str(findKey) + " at position " + str(i+1) + " with value " + str(value) + "\n")
            return value
        elif i == maxCap-1: #couldn't find the key
            print("-- No node with key " + str(findKey) + " found.\n")
        else:
            oldNode = oldNode.next
            currentNode = currentNode.next
                
def printList():
    currentNode = head
    for i in range(nodeNoCounter):
        print('Key: ' + str(currentNode.key) + ' value: ' + str(currentNode.value), end = ' => ')
        currentNode = currentNode.next
    print('END, listlength: ' + str(nodeNoCounter) + '\n')


#### TESTING ####
maxCap = 3 #Total size of the linkedlist / cache
#initalizing the linked list#
nodeNoCounter = 1 
node0 = Node(0, 0)
node0.next = None
head = node0

#Generating new nodes
node1 = Node(1, 1)
node2 = Node(2, 2)
node3 = Node(3, 3)
node4 = Node(4, 4)
node5 = Node(5, 5)
node6 = Node(6, 6)

#Testing the list
printList()

put(node1)
printList()

_ = get(node1.key)

put(node2)
printList()
_ = get(node2.key)

put(node3)
printList()
_ = get(node1.key)
printList()

put(node4)
printList()
_ = get(node4.key)

put(node5)
printList()
_ = get(node3.key)

put(node6)
printList()
_ = get(node0.key)

