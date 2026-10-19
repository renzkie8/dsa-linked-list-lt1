print("DSA LT1 Second Phase by Jess")

# ref: https://www.geeksforgeeks.org/python-linked-list/

llist = []

class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LL():
    def __init__(self):
        self.head = None

    def ins_start(self, newdata = None):
        newdata = Node(input("Insert at Start. \nWhat do you want to insert? "))
        newdata.next = self.head
        self.head = newdata

    def ins_end(self, newdata = None):
        newdata = Node(input("Insert at End. \nWhat do you want to insert? "))
        if self.head == None: 
            self.head = newdata
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = newdata

    def ins_pos(self, newdata = None, position = None):
        newdata = Node(input("Insert at Position. \nWhat do you want to insert? "))
        length = len(llist)
        while True:
            position = input(f"Where do you want to insert '{newdata.data}'?: ")
            if position.isdigit():
                if int(position) <= length:
                    break
                else:
                    print("Position not valid. The mentioned node is absent.")
            else:
                print("\nPlease enter a valid position (integer). \n\n***\n")

    def del_num (self, x) :
        #x is the user input or selected node to delete
        if self.head is None:
            print("can't perform delete operation,LL is empty") 
        # check if the LL is empty
            return 
        if x == self.head.data:
        #check if the input node to be deleted is the first data of node.
           self.head = self.head.ref
           return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break 
            n=n.ref
        #when it found the delete x then it stop or doesnt found
        if n.ref is None:
            print ("N is not on the list and cannot be deleted.")
        else: 
            n.ref =n.ref.ref


    
    








    def print_list(self):
        node = self.head
        while node != None:
            llist.append(node.data)
            node = node.next
        print('\nYour Linked List: \n     ' + " -> ".join(llist))






sample = LL()
def main_menu():

    while True:
        sample.print_list()
        chooseOp = input("\n[0] Exit \n[1] Insert At Start \n[2] Insert At End \n[3] Insert At Position \n[4] Delete At Start \n[5] Delete At End \n[6] Delete At Position \n[7] Delete Number \n[8] Search Number \n[9] Display Number At Position \n[10] Display List \n\nChoose an option: ")

        # E X I T  O P T I O N
        if chooseOp == '0':
            print("\n------------------------------ \n")
            exityes_no = input("[0] Yes \n[1] No \n\nExit Program? ")
            if exityes_no == '0':
                print("\n------------------------------ \n\nT H A N K  Y O U !\n")
                break
            elif exityes_no.upper == '1':
                # print("------------------------------ \n")
                return

        # I N S E R T  O P T I O N S
        if chooseOp == '1':
            print("\n------------------------------ \n")
            sample.ins_start()
            sample.print_list()
            print("\n------------------------------ ")

        if chooseOp == '2':
            print("\n------------------------------ \n")
            sample.ins_end()
            sample.print_list()
            print("\n------------------------------ ")

        if chooseOp == '3':
            print("\n------------------------------ \n")
            sample.ins_pos()
            sample.print_list()
            print("\n------------------------------ ")

        #D E L E T E O P T I O N S

        if chooseOp == '7':
            print("/n------------------------------ \n")
            sample.del_num()
            sample.print_list()
            print("\n------------------------------ ")









main_menu()