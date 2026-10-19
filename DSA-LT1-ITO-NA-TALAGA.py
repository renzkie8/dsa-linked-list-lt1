print("\nDSA - Learning Task 1 (DS List)")

# ref: https://www.geeksforgeeks.org/python-linked-list/
# ref: CCCS 103 Finals project - Activity Tracker 

class Node(): # creating a node with user input as data
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LL(): # creating a blank linked list
    def __init__(self):
        self.head = None

    def ins_start(self, newnode = None):
        # makes it possible to insert at start using Insert at Position Option
        if newnode is None:
            while True:
                newnode = input("\nINSERT AT START. \nWhat do you want to insert? ")
                try: # exception handling*; limiting user input to valid integers
                    int(newnode)
                    newnode = Node(newnode)
                    break
                except:
                    print("PLEASE ENTER AN INTEGER. \n\n***")
        newnode.next = self.head # connects new node to list head  
        self.head = newnode # makes new node the list head
        print(f'\n"{newnode.data}" INSERTED AT START.') # no failure. Can insert at head even on empty lists.

    def ins_end(self, newnode = None):
        # makes it possible to insert at end using Insert at Position Option
        if newnode is None:
            while True:
                newnode = input("\nINSERT AT END. \nWhat do you want to insert? ")
                try: # exception handling*
                    int(newnode)
                    newnode = Node(newnode)
                    break
                except:
                    print("PLEASE ENTER AN INTEGER. \n\n***")
        # CASE 0 : EMPTY LIST
        if self.head is None: 
            self.head = newnode

        else:
            tail = self.head
            while tail.next != None: # finding list tail
                tail = tail.next
            tail.next = newnode # adds new node to end of list
        print(f'\n"{newnode.data}" INSERTED AT END.')

    def ins_pos(self, newnode = None, position = None):
        while True:
            newnode = input("\nINSERT AT POSITION. \nWhat do you want to insert? ")
            try: # exception handling*
                int(newnode)
                newnode = Node(newnode)
                break
            except:
                print("PLEASE ENTER AN INTEGER. \n\n***")
        while True:
            position = input(f'Where do you want to insert "{newnode.data}"?: ')
            if position.isdigit(): # checks if position entered is valid (positive integer)
                position = int(position)
                # CASE : INSERTING AT POSITION 0 OR START OF LIST
                if position == 0:
                    self.ins_start(newnode)
                    break

                ptr = self.head # ptr: pointer of node to the left of specified position
                index = 0
                while ptr != None and index != position-1: 
                    ptr = ptr.next
                    index += 1
                # when node is empty before or on specified position (left of position)
                if ptr is None:
                    print("\nCANNOT INSERT. \nNode does not exist.")
                    break

                else:
                    newnode.next = ptr.next # connects new node to node on specified position
                    ptr.next = newnode # inserts new node
                    print(f'\n"{newnode.data}" INSERTED AT POSITION {position}.')
                    break
            else:
                print("PLEASE ENTER A VALID INTEGER. \n\n***\n")

    def del_start(self):
        ptr = self.head
        # CASE 0 : EMPTY LIST
        if ptr is None:
            print("\nCANNOT DELETE. LINKED LIST IS EMPTY.")
            return
        # CASE : LIST HAS ONLY 1 NODE
        elif ptr.next is None:
            self.head = ptr.next
            print(f'\n"{ptr.data}" DELETED FROM START. \nLinked list is now empty.')
            return
        else:
            self.head = ptr.next # makes second node the head, removing first node from the list
            print(f'\n"{ptr.data}" DELETED FROM START OF LINKED LIST.')

    def del_end(self):
        # CASE 0 : EMPTY LIST
        if self.head is None:
            print("\nCANNOT DELETE. \nLinked list is empty.")
            return
        
        tail = self.head # tail: pointer for node to be deleted

        # CASE 1 : if list has only 1 node
        if tail.next is None: 
            self.head = tail.next # makes None or NULL the list head
            print(f'\n"{tail.data}" DELETED FROM END. \nLinked list is now empty.')
            return
        
        while tail.next != None: # finding the list tail
            tail = tail.next
        ptr = self.head
        while ptr.next != tail:
            ptr = ptr.next
        ptr.next = tail.next
        print(f'\n"{tail.data}" DELETED FROM END OF LINKED LIST.')
        
    def del_pos(self, position = None):
        # CASE 0 : EMPTY LIST
        if self.head is None:
            print("\nCANNOT DELETE. \nLinked list is empty.")
            return
        
        while True:
            position = input("\nEnter position of node to be deleted: ")
            if position.isdigit(): # exception handling*
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
                    print("\nCANNOT DELETE AT POSITION. \nNode does not exist.")
                    break
                else: # node to be deleted is found, with p2 as pointer
                    p1 = self.head
                    index1 = 0
                    while p1 != None and index1 != position-1: #p1: pointer for node positioned before the node to be removed
                        p1 = p1.next
                        index1 += 1
                    p1.next = p2.next # removes p2 from linked list
                    print(f'\n"{p2.data}" DELETED AT POSITION {position}.')
                    break
            else:
                print("PLEASE ENTER A VALID INTEGER. \n\n***")

    def del_num(self, num = None):
        # CASE 0 : EMPTY LIST
        if self.head is None:
            print("\nCANNOT DELETE. \nLinked list is empty.")
            return

        while True:
            num = input("\nDELETE NUMBER. \nWhat number do you want to delete? ")
            try: # exception handling*
                int(num)
                break
            except:
                print("PLEASE ENTER AN INTEGER. \n\n***\n")

        node = self.head # node : node to be checked if it contains the specified number to be deleted
        while node != None and node.data != num: # finding the specified number in each node on the list
            node = node.next
        if node is None: # CASE : all nodes were searched but number is never found
            print(f'\n"{num}" IS NOT IN THE LINKED LIST AND CANNOT BE DELETED.')
        else:
            if self.head is node: # CASE : specified number is the first element
                self.del_start() # calls for delete at start function
                return
            p1 = self.head
            while p1.next != node: # p1: pointer for node before target node
                p1 = p1.next
            p1.next = node.next # removes the node with specified number from the list
            print(f'\n"{node.data}" HAS BEEN SUCCESSFULLY DELETED FROM LINKED LIST.')

    def search_num(self, num = None):
        # CASE 0 : EMPTY LIST
        if self.head is None:
            print("\nCANNOT SEARCH. LINKED LIST IS EMPTY.")
            return
        
        while True:
            num = input("\nSEARCH NUMBER. \nWhat number do you want to search for? ")
            try: # exception handling*
                int(num)
                break
            except:
                print("PLEASE ENTER AN INTEGER. \n\n***\n")

        node = self.head # node : node to be checked if it contains the specified number
        index = 0 # current position of the node being checked
        while node != None and node.data != num: # searching all nodes in the list for the specified number
            node = node.next
            index += 1
        if node is None: # CASE : all nodes were searched but number is never found
            print(f'\nVALUE IS NOT FOUND.')
        else: # CASE : node with specified number is found
            print(f'\nVALUE IS FOUND AT POSITION {index}.')

    def dis_num(self, position = None):
        # CASE 0 : EMPTY LIST
        if self.head is None:
            print("\nCANNOT BE DONE. \nLinked list is empty.")
            return
        
        while True:
            position = input("\nDISPLAY NUMBER AT POSITION. \nEnter the position of the number: ")
            if position.isdigit(): # exception handling*
                position = int(position)

                node = self.head # node: present node being checked for position
                index = 0 # position of current node
                while node != None and index != position: # searching for node at specified position
                    node = node.next
                    index += 1
                if node is None: # CASE : all nodes in the list were passed, but specified position is never reached
                    print(f'\nCANNOT DISPLAY NUMBER. \n Node in position "{position}" is empty/does not exist.')
                    break
                else: # CASE : node in specified position is reached and is not empty 
                    print(f'\n"{node.data}" FOUND IN POSITION "{position}".')
                    break
            else:
                print("PLEASE ENTER AN INTEGER. \n\n***")

    def display_list(self):
        ptr = self.head
        # CASE 0 : EMPTY LIST
        if ptr is None:
            print("\nYour list is empty.")
        else:
            print("\nYour Linked List: ")
            while ptr != None: # goes through each node (and prints contained numbers) until it reaches the end of the list
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
            print("\n------------------------------ ")
            sample.ins_start()
            print("\n------------------------------ ")

        elif chooseOp == '2':
            print("\n------------------------------ ")
            sample.ins_end()
            print("\n------------------------------ ")

        elif chooseOp == '3':
            print("\n------------------------------ ")
            sample.ins_pos()
            print("\n------------------------------ ")

        # D E L E T E  O P T I O N S
        elif chooseOp == '4':
            print("\n------------------------------ ")
            sample.del_start()
            print("\n------------------------------ ")

        elif chooseOp == '5':
            print("\n------------------------------ ")
            sample.del_end()
            print("\n------------------------------ ")

        elif chooseOp == '6':
            print("\n------------------------------ ")
            sample.del_pos()
            print("\n------------------------------ ")

        elif chooseOp == '7':
            print("\n------------------------------ ")
            sample.del_num()
            print("\n------------------------------ ")

        # S E A R C H  O P T I O N 
        elif chooseOp == '8':
            print("\n------------------------------ ")
            sample.search_num()
            print("\n------------------------------ ")

        # D I S P L A Y  O P T I O N 
        elif chooseOp == '9':
            print("\n------------------------------ ")
            sample.dis_num()
            print("\n------------------------------ ")

        elif chooseOp == '10':
            print("\n------------------------------ ")
            sample.display_list()
            print("\n------------------------------ ")

        # E X C E P T I O N : To limit input to the given options
        else:
            print("PLEASE ENTER A VALID NUMBER (0-10) \n\n------------------------------")

main_menu()