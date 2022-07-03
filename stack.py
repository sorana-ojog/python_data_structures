class Stack:
  def __init__(self, arr):
    #__arr is private
    self.__arr = arr
    
  def pop(self):
    last = self.__arr[-1]
    #[:-1] returns all the elements up until the last one 
    self.__arr = self.__arr[:-1] 
    return last
    
  def push(self, el):
    self.__arr += [el]
    #usual push() from stack doesn't return anything
    return self.__arr
    
  def elements(self):
    return self.__arr
    
  def __repr__(self):
    #__repr__ returns string
    return f'Stack({self.__arr})'

if __name__== "__main__":
  newArr = Stack([1, 2, 3, 4])
  print(newArr.pop())
  print(newArr.elements())
  print(newArr.push(5))
  print(newArr)
