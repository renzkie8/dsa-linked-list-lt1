print("DSA LT1 First Draft by Jess")

def main_menu():
  
    while True:
       
       chooseOperation = input("\n[0] Exit \n[1] Insert at Start \n[2] Insert At End
        \n[3] Insert At Position \n [4] Delete At Start \n [5] Delete At End \n [6]
        Delete At Position \n[7] Delete Number \n [8] Search Number \n[9] Display 
        Number At Position \n[10] Display List \n\nChoose an option: ")

main_menu()

class LL():
   def __init__(self) -> None:
      self.head = None
   
   def print_list(self):
      node = self.head
      llist = []
      while node != None:
         llist.append(node.data)
         node = node.next
      print(str(llist))

   def ins_start(self, newdata = None):
      newdata = Node(input("Insert at Start"))
      newdata.next = self.head
      self.head = newdata

   def ins_end (self,newdata = None):
   newdata = Node(input("Insert at End."))
   if self.head == None:
      self.head = newdata
   else:
        tail = self.head
        while tail.next != None:
           tail = tail.next
        tail.next = newdata