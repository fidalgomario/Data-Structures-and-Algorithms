'''
A node is a data element that consist of three attributes
when dealing with a DoublyLinkedList because in this situation
the node requires to hold the DATA, the address to the NEXT node
in the linked list, and the address to the PREVIOUS node in the 
linked list.
'''

class Node(object):
    def __init__(self,data,prev,next):
        self.data = data
        self.prev = prev
        self.next = next

'''
Now that the Node Class has been defined with its INIT function,
we must create the DoublyLinkedList Class which will allow us 
to append and remove nodes in the list.
'''
class DoublyLinkedList(object):
    #A DoublyLinkedList has both a HEAD and a TAIL to know the endpoints of the list
    head = None
    tail = None

    #Append will allow the addition of a new node to the END of the DoublyLinkedList
    def append(self, data):
        #create a new node using the class defined before
        newNode = Node(data, None, None)
        #if the list is empty make this new node the head and tail of the DoublyLinkedList
        if(self.head == None):
            self.head = self.tail = newNode
        else:
        #otherwise make this new node point to the prev which is the tail
            newNode.prev = self.tail
        #since the new node is at the end it has no next node to point to, set that to none
            newNode.next = None
        #change the old tails next pointer to the new node
            self.tail.next = newNode
        #and set the tail of the DoublyLinkedList to the new node
            self.tail = newNode

    #Remove will allow the deletion of a node from the DoublyLinkedList
    def remove(self,val):
        #since a linked list does not have direct access to the index of a node we must begin from the head
        currentNode = self.head
       
        while(currentNode != None):
            #check for the value to remove
            if(currentNode.data == val):
                #if the node with the value is found has a previous node then fix the pointers
                if(currentNode.prev != None):
                    currentNode.prev.next = currentNode.next
                    currentNode.next.prev = currentNode.prev
                else:
                #otherwise set the head to the next node and remove the pointer to the current node
                    self.head = currentNode.next
                    currentNode.next.prev = None
                    
            #traverse to the next node if not the node being looked for
            currentNode = currentNode.next
