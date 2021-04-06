# A complete working Python program to find sum of node values
# Linked List iteratively

# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.

    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #	 Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.

    def sum_of_nodes(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while (temp):
            count += temp.data
            temp = temp.next
        return count


# Code execution starts here
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(22)
    llist.push(121)
    llist.push(232)
    llist.push(132)
    print("Sum of values of nodes is :", llist.sum_of_nodes())
