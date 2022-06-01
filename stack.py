# Linkedlist implementation of stack.

from collections import deque

class Stack:

    def __init__(self):
        self.container = deque()

    
    def push(self, val):

        self.container.append(val)
    
    def peek(self):
        return self.container[-1]
    
    def pop(self):
        return self.container.pop()
    
    def isEmpty(self):
        return len(self.container) == 0 

    def size(self):
        return len(self.container)

    def display(self):

        for element in self.container:

            print(element, end = " ")


if __name__ == "__main__":

    stack = Stack()


    while True :
        
        print("\n----------\n1. Add the element to the stack\n2. Pop the element from the stack\n3. Display the stack\n4. Current size of the stack\n5. Check if stack is empty or not\n6. Peek the element\n7. Exit\n----------\n")
        
        choice = int(input())

        if choice == 1:
        
            element = input("\nEnter the element you want to add to the stack : ")
            stack.push(element)
        
        elif choice == 2:

            print("\nStack before poping the element : {}".format(stack.display()))

            stack.pop()

            print("\nStack after poping the element : {}".format(stack.display()))

        elif choice == 3:
            
            print(stack.display())
        
        elif choice == 4:

            print("\nCurrent size of the stack is : {}".format(stack.size()))
        
        elif choice == 5:
            
            print("Stack is empty!!!") if stack.isEmpty() == True else print("Stack is not Empty!!!")

        elif choice == 6:

            print("Peeked element is : {}".format(stack.peek()))

        elif choice == 7:
            print("Goodbye friend :)")
            break