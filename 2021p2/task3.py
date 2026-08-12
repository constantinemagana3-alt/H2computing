#task3.1
class Node():
  def __init__(self,data):
    self.data = data
    self.next = None

  def setData(self,new):
    self.data = new

  def getData(self):
    return self.data

  def setNext(self,new):
    self.next = new

  def getNext(self):
    return self.next

class linkedlist():
  def __init__(self):
    self.head = None


  def isEmpty(self):
    if self.head == None:
      return True
    return False

  def insertAtHead(self,data):
    newNode = Node(data)
    if self.isEmpty():
      self.head = newNode
    else:
      temp = self.head
      self.head = newNode
      newNode.next = temp

  def deleteNode(self,integer_value):
    if self.isEmpty() == True:
      return "LL is empty"

    current = self.head
    previous = None
    while current is not None:
      if current.data == integer_value:
        if previous is None:
          self.head = current.next
        else:
          previous.next = current.next
        return
      previous = current
      current = current.next

    return None

  def search(self,integer_value):
    if self.isEmpty():
      return "Linked list is empty"

    current = self.head
    found = False
    while current != None:
      if current.data == integer_value:
        found = True
        return found
      current = current.next

    return found

  def count(self):
    counter = 0
    current = self.head
    while current is not None:
      counter += 1
      current = current.next

    return counter

  def to_String(self):
    values = []
    current = self.head
    while current is not None:
      values.append(str(current.data))
      current = current.next
    return ("[" + ','.join(values) + "]")
