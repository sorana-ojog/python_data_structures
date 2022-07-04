class Queue:
  def __init__(self, arr):
    #__arr is private
    self.__arr = arr
    
  def dequeue(self):
    first = self.__arr[0]
    #[1:] returns all the elements after the first one 
    self.__arr = self.__arr[1:] 
    return first
    
  def enqueue(self, el):
    self.__arr += [el]
    #usual enqueue() from Queue doesn't return anything
    # return self.__arr
    return Queue(self.__arr)
    
  def elements(self):
    return self.__arr
    
  def __repr__(self):
    #__repr__ returns string
    return f'Queue({self.__arr})'

if __name__== "__main__":
  newArr = Queue([1, 2, 3, 4])
  print(newArr.dequeue()) #will remove 1
  print(newArr.elements())
  print(newArr.enqueue(5)) #will add 5 to the end
  print(newArr.dequeue()) #will remove 2
  print(newArr)
  print(newArr.enqueue(1).enqueue(2)) #will add 1 and 2 to the end
