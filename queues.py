#linked list application : queue
#three operations: enqueue, dequeue, peek
#enqueue is add data from end
#dequeue is provide and remove data from the beginning
#peek reveal data from the front without removing ti

#operation only for front or back of the queue, so tranversal or modification to other node is not allowed

##### Queues python size
from linkedList import Node


class Queue:
  # Add max_size and size properties within __init__():
  def __init__(self, max_size = None):
    self.head = None
    self.tail = None
    self.max_size = max_size 
    self.size = 0
    
  def peek(self):
    if self.get_size() == 0:
      print("Nothing to see here!")
    else:
      return self.head.get_value()

  # Define get_size() and has_space() below:
  def get_size(self):
    return self.size
  def has_space(self):
    if (self.max_size):
      return self.max_size > self.get_size()
    else:
      return True
  def is_empty(self):
    return True if self.size == 0 else False


# solution

# class Queue:
#   # Add max_size and size properties within __init__():
#   def __init__(self, max_size=None):
#     self.head = None
#     self.tail = None
#     self.max_size = max_size
#     self.size = 0
    
#   def peek(self):
#     if self.size > 0:
#       return self.head.get_value()
#     else:
#       print("Nothing to see here!")
  
#   # Define get_size() and has_space() below:
#   def get_size(self):
#     return self.size
  
#   def has_space(self):
#     if self.max_size == None:
#       return True
#     else:
#       return self.max_size > self.get_size()
    
#   def is_empty(self):
    return self.size == 0