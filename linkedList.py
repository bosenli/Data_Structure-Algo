#head node , tail node with "null" at its link
#node operation: add, remove, find, traversing

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
            stringlist += str(current_node.get_value()) + "\n"
        current_node = current_node.get_next_node()
    return string_list

 
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
