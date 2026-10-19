print("\nDSA LT1 Fifth Phase by Jess SANA LAST NA TALAGA\n   > Optimization/organizing of ins/del fcn for explanation.\n\n   > ***NO 7-9 YET***")

# ref: https://www.geeksforgeeks.org/python-linked-list/
# ref: CCCS 103 project - Activity Tracker


class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LL():
    def __init__(self):
        self.head = None
        self.llist = None

    def update_list(self):
        self.llist = []
        node = self.head
        while node != None:
            self.llist.append(node.data)
            node = node.next
    
    def ins_start(self, newnode = None):
        # makes it possible to insert at start using Insert at Position Option
        if newnode is None:
            newnode = Node(input("Insert at Start. \nWhat do you want to insert? "))
        newnode.next = self.head # connects new node to list head
        self.head = newnode # makes new node the list head
        self.update_list()
        print(f'\n"{newnode.data}" INSERTED AT START.') # no failure. Can insert at head even on empty lists.

    def ins_end(self, newnode = None):
        # makes it possible to insert at end using Insert at Position Option
        if newnode is None:
            newnode = Node(input("Insert at End. \nWhat do you want to insert? "))
        if self.head == None: 
            self.head = newnode
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = newnode
        self.update_list()
        print(f'\n"{newnode.data}" INSERTED AT END.')

    def ins_pos(self, newnode = None, position = None):
        newnode = Node(input("Insert at Position. \nWhat do you want to insert? "))
        while True:
            position = input(f'Where do you want to insert "{newnode.data}"?: ')
            if position.isdigit():
                position = int(position)
                if position == 0:
                    self.ins_start(newnode)
                    break
                p1 = self.head
                index = 0
                while p1 != None and index != position-1:
                    p1 = p1.next
                    index += 1
                if p1 is None:
                    self.update_list()
                    print("\nCANNOT INSERT. NODE DOES NOT EXIST.")
                    break
                else:
                    newnode.next = p1.next
                    p1.next = newnode
                    self.update_list()
                    print(f'\n"{newnode.data}" INSERTED AT POSITION {position}.')
                    break
            else:
                print("PLEASE ENTER AN INTEGER. \n\n***\n")

    def del_start(self):
        p1 = self.head
        if p1 is None:
            print("CANNOT DELETE. LINKED LIST IS EMPTY.")
            return
        elif p1.next is None:
            self.head = p1.next
            self.update_list()
            print(f'\n"{p1.data}" DELETED FROM START. LINKED LIST IS NOW EMPTY.')
            return
        else:
            self.head = p1.next
            self.update_list()
            print(f'\n"{p1.data}" DELETED FROM START OF LINKED LIST.')

    def del_end(self):
        # CASE 0 : EMPTY LIST
        if self.head is None:
            print("CANNOT DELETE. LINKED LIST IS EMPTY.")
            return
        
        tail = self.head # tail: pointer for node to be deleted

        # CASE 1 : if list has only 1 node
        if tail.next is None: 
            self.head = tail.next # makes None or NULL the list head
            self.update_list()
            print(f'\n"{tail.data}" DELETED FROM END. LINKED LIST IS NOW EMPTY.')
            return
        
        while tail.next != None: # finding the list tail
            tail = tail.next
        p1 = self.head
        while p1.next != tail:
            p1 = p1.next
        p1.next = tail.next
        self.update_list()
        print(f'\n"{tail.data}"NODE DELETED FROM END OF LINKED LIST.')
        
    def del_pos(self, position = None):
        # CASE 0 : EMPTY LIST
        if self.head is None:
            print("\nCANNOT DELETE. LINKED LIST IS EMPTY.")
            return
        
        while True:
            position = input("Enter position of node to be deleted: ")
            if position.isdigit():
                position = int(position)
                # POSITION = ZERO
                if position == 0:
                    self.del_start()
                    break
                
                # POSITION != ZERO
                p2 = self.head # p2: pointer for node to be removed. P2 positioned first to identify if there is a node at position
                index2 = 0
                while p2 != None and index2 != position:
                    p2 = p2.next
                    index2 += 1
                if p2 is None: # when node is empty before or on specified position
                    self.update_list()
                    print("\nCANNOT DELETE AT POSITION. NODE DOES NOT EXIST.")
                    break
                else: # node to be deleted is found, with p2 as pointer
                    p1 = self.head
                    index1 = 0
                    while p1 != None and index1 != position-1: #p1: pointer for node positioned before the node to be removed
                        p1 = p1.next
                        index1 += 1
                    p1.next = p2.next # removes p2 from linked list
                    self.update_list()
                    print(f'\n"{p2.data}" DELETED AT POSITION {position}.')
                    break
            else:
                print("PLEASE ENTER AN INTEGER. \n\n***\n")

    def print_list(self):
        # print('\nYour Linked List: \n     ' + " -> ".join(self.llist))
        ptr = self.head
        if ptr is None:
            print("\nYour list is empty.")
        else:
            print("\nYour Linked List: ")
            while ptr != None:
                print(ptr.data)
                ptr = ptr.next



sample = LL()
def main_menu():
    
    while True:
        chooseOp = input("\n[0] Exit \n[1] Insert At Start \n[2] Insert At End \n[3] Insert At Position \n[4] Delete At Start \n[5] Delete At End \n[6] Delete At Position \n[7] Delete Number \n[8] Search Number \n[9] Display Number At Position \n[10] Display List \n\nChoose an option: ")

        # E X I T  O P T I O N
        if chooseOp == '0':
            print("\n------------------------------ \n")
            while True:
                exityes_no = input("[0] Yes \n[1] No \n\nExit Program? ")
                if exityes_no == '0':
                    print("\n------------------------------ \n\nT H A N K  Y O U !\n")
                    return
                elif exityes_no == '1':
                    print("\n------------------------------ ")
                    break
                else:
                    print("PLEASE ENTER [0] FOR YES OR [1] FOR NO.\n\n------------------------------\n")
            

        # I N S E R T  O P T I O N S
        elif chooseOp == '1':
            print("\n------------------------------ \n")
            sample.ins_start()
            sample.print_list()
            print("\n------------------------------ ")

        elif chooseOp == '2':
            print("\n------------------------------ \n")
            sample.ins_end()
            sample.print_list()
            print("\n------------------------------ ")

        elif chooseOp == '3':
            print("\n------------------------------ \n")
            sample.ins_pos()
            sample.print_list()
            print("\n------------------------------ ")

        elif chooseOp == '4':
            print("\n------------------------------ \n")
            sample.del_start()
            sample.print_list()
            print("\n------------------------------ ")

        elif chooseOp == '5':
            print("\n------------------------------ \n")
            sample.del_end()
            sample.print_list()
            print("\n------------------------------ ")

        elif chooseOp == '6':
            print("\n------------------------------ \n")
            sample.del_pos()
            sample.print_list()
            print("\n------------------------------ ")

        # elif chooseOp == '7':
        #     print("\n------------------------------ \n")
        #     sample.ins_pos()
        #     sample.print_list()
        #     print("\n------------------------------ ")

        # elif chooseOp == '8':
        #     print("\n------------------------------ \n")
        #     sample.ins_pos()
        #     sample.print_list()
        #     print("\n------------------------------ ")

        # elif chooseOp == '9':
        #     print("\n------------------------------ \n")
        #     sample.ins_pos()
        #     sample.print_list()
        #     print("\n------------------------------ ")

        # elif chooseOp == '10':
        #     print("\n------------------------------ \n")
        #     sample.ins_pos()
        #     sample.print_list()
        #     print("\n------------------------------ ")


        # E X C E P T I O N
        else:
            print("PLEASE ENTER A VALID NUMBER (0-10) \n\n------------------------------")


main_menu()