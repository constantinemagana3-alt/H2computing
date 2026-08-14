#task3.1
import random
class Tree():
  def __init__(self,data):
    self.left_pointer = None
    self.right_pointer = None
    self.data = data

  #class methods
  def getleft(self):
    return self.left_pointer

  def setLeft(self,left):
    self.left_pointer = left

  def getRight(self):
    return self.right_pointer

  def setRight(self,right):
    self.right_pointer = right

  def getData(self):
    return self.data

  def setData(self,data):
    self.data = data

  def insert(self,key):
    newleafNode = Tree(key)
    if key < self.data:#key inserted is less than root node
      if self.left_pointer == None:#leaf node is empty
        self.left_pointer = newleafNode

      else:
        self.left_pointer.insert(key)#goes to the left of the left pointer

    else:#key inserted if more than root node
      if self.right_pointer == None:
        self.right_pointer = newleafNode

      else:
        self.right_pointer.insert(key)

  def inorder(self):
    if self.left_pointer is not None:
      self.left_pointer.inorder()
    print(self.data,end= "")
    if self.right_pointer is not None:
      self.right_pointer.inorder()

  def postorder(self):
    if self.left_pointer is not None:
      self.left_pointer.postorder()
    if self.right_pointer is not None:
      self.right_pointer.postorder()
    print(self.data,end ="")

#main program
lst_num = []
for i in range(10):
  num = random.randint(0,999)
  lst_num.append(num)

rootNode = Tree(lst_num[0])
for i in lst_num[1:]:
  rootNode.insert(i)

print(rootNode.postorder())
print(rootNode.inorder())
