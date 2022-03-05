#head node , tail node with "null" at its link
#node operation: add, remove, find, traversing
# https://www.youtube.com/watch?v=qp8u-frRAnU
#node

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

  def has_next(self):
      if self.get_next_node() is None:
          return False
      return True

  def to_string(self):
      return "Node value: " + str(self.get_value)

# Create your LinkedList class below:
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node

  def insert_beginning(self,new_value ): #insert to beginning
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while (current_node):
        if (current_node.get_value() != None):
            string_list += str(current_node.get_value()) + "\n"
        current_node = current_node.get_next_node()
    return string_list

  def print_list(self):
    print("list is")
    node = self.get_head_node()
    while node:
        print (node.get_value())
        node = node.get_next_node()
 
  # Define your remove_node method below:
  # def remove_node(self, value_to_remove):
  #   current_node = self.head_node
  #   if (current_node.get_value() == value_to_remove):
  #     self.head_node = self.next_node
  #   current_node = self.next_node

  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()  #if it is current node need to be removed, then auto discard current node 
    else:
      while current_node:
        next_node = current_node.get_next_node()  
        if next_node.get_value() == value_to_remove: # if it is next node, next remove next_node
          current_node.set_next_node(next_node.get_next_node())
          current_node = None #set none to current_node means to stop the while loop
        else:
          current_node = next_node



# def main():
    
#     # a= Node(5)
#     # b= Node(6,a)
#     # c= Node(7,b)
#     # d = LinkedList(c)
#     # print(d.print_list())
#     myList=LinkedList()
#     myList.insert_beginning(5)
#     myList.insert_beginning(9)
#     myList.insert_beginning(3)
#     # print(myList.stringify_list())
#     print(myList.print_list())


#     #print(d.print_list())

# main()
#if __name__ == "__main__":   this line is equivalent with main()
    # myList=LinkedList()
    # myList.insert_beginning(5)
    # myList.insert_beginning(9)
    # myList.insert_beginning(3)
    # print(myList.stringify_list())


    # # defining linked list
    # ll = LinkedList()
 
    # # defining nodes
    # node1 = Node(10)
    # node2 = Node(15)
    # node3 = Node(20)
 
    # # connecting the nodes
    # ll.head = node1
    # node1.next = node2
    # node2.next = node3
     
    # # when print is called, by default
    # #it calls the __str__ method
    # print(ll)