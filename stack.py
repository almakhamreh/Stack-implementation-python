# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:52:00 2021

@author: Ahmad Almakhamreh
"""

"""
   print statements are commented you can always uncomment them to track the operations
"""

class Stack:
   def __init__(self):
      self.__mystack = []
      """
      the leading underscores are simply to indicate that the attribute is inteded to be private and should not be accessed outside the class
      """


   def push(self,item):
      """This method accepts an item as a parameter and appends it to the end of the List. prints the added item.

      appending to the end of a list happens in constant time, so the runtime for this method is O(1)
      """
      self.__mystack.append(item)
      # print(f"push: ---> {item}")


   def pop(self):
      """This method removes, return, and prints the last item in the list, which is the top item of the Stack.

      removing from the end of a list (top) also happens in constant time, so the runtime for this method is O(1)
      """
      if self.__mystack:
         # print(f"pop: ---> {self.__mystack[-1]}" )
         return self.__mystack.pop()
      else:
         print("cannot pop, stack is empty")


   def peek(self):
      """This method prints and returns the last item in the list (top of the stack)

      this method runs in constant time O(1), because indexing into a list is done in constant time. (Random access)
      """
      if self.__mystack:
         print(f"peek: ---> {self.__mystack[-1]} ")
         return self.__mystack[-1]
      else:
         print("cannot peek, stack is empty")


   def size(self):
      """This method prints & retuns the length of the list that is representing the Stack.

      this method runs in constant time O(1), because finding the length of a list also happens in constant time.
      """
      print(f"size: {len(self.__mystack)}")
      return len(self.__mystack)


   def isEmpty(self):
      """This method retuns a boolean value describing weather or not the Stack is empty.

      testing for equality happens in constant time.
      """
      print(f"isEmpty: ---> {self.__mystack == []}")
      return not(self.__mystack)
      # can also use
      # return self.__mystack == []


   def showItems(self):
      """this method prints the items in the list"""
      print(f"{self.__mystack} <---- TOP")


def main():

   """
   Test cases
   """
   stack  = Stack()

   stack.push(5)
   stack.push("ahmed")
   stack.push(7.0)

   stack.showItems()

   stack.push('A')

   stack.showItems()

   stack.pop()
   stack.pop()
   stack.pop()
   stack.peek()
   stack.pop()
   stack.pop()
   stack.isEmpty()

if __name__ == "__main__" : main()
