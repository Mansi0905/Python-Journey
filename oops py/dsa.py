# # typecasting
# # s=[1,2222,22,56,12111,4554]
# # print(s)

# # decimal to binary type conversion
# # x=13
# # print(type(x))

# # name = "ashushu"
# # if name =="gaurav" or "html":
# #     print("biaks")
# # else:
# #     print("jijijiji")

# # def fun():
# #     print("hello")

# # fun()    

# #types of argument
# # positional argument, variable length positional arguamnet , keyword argumnet , variable length keyword argumnet , default argument
# # global value can not be updated
# # naming space 
# #  global space --> main memoery
# # local space --> local space created wheb a  functiion is called or vlass is called
# #  enclosing spac e--> space between  two function 
# # built in space -->built in function

# # there are two ways to solve a problem:-
# # iterative solution- loop se
# # recursion - function se

# # def replace(s):
# #     if len(s)==0:
# #      return s
# #     elif s[0]=='a :
# #     return "b"+replace()

# # def replace(s):
# #     if len(s)==0:
# #         return s
    
# #     elif s[0]=="p" and s[1]=="s":
# #        return "3.14" + replace(s[2:])
# #     else:
# #        return 1
    

# # replace("gipipipip")    

# # list = [5,6,7,]

# # lis = [1, 12, 4, 6, 7, 8, 11]

# # row = max(lis)
# # col = len(lis)

# # i = row
# # while i > 0:
# #     j = 0
# #     while j < col:
# #         if lis[j] >= i:
# #             print("*", end=" ")
# #         else:
# #             print(" ", end=" ")
# #         j += 1
# #     print()
# #     i -= 1

# # arr = [1, 12, 4, 6, 7, 8, 11]
# # x = 99

# # n = len(arr)
# # mid = n // 2

# # arr.append(0)         

# # i = n
# # while i > mid:
# #     arr[i] = arr[i-1]
# #     i -= 1

# # arr[mid] = x
 
# # print(arr)


# # arr=[2,3,4,5,8]
# # data=10

# # mid=len(arr)//2
# # print("mid:", mid)

# # arr[len(arr):]=[None]

# # for i in range(len(arr)-2,mid-1,-1):
# #     arr[i+1] =arr[i]

# #     arr[mid]=data
# #     print(arr)

# arr=[1,2,3,4,5]
# pos=3
# ele=11
# new_arr[] =len(arr)+1

# for i in range(1,len(arr)):
#     if i < pos:
#         new_arr[i] =arr[i]

#     elif i==pos:
#         new_arr[i]=ele

#     else:
#         new_arr[i]= arr[i-1] 

#     print (new_arr)   
# 
class Node:
    """A node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        """Add a node to the very beginning of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Remove the first occurrence of a node with the given data."""
        curr = self.head
        
        while curr:
            if curr.data == key:
                # Case 1: Deleting the head node
                if curr == self.head:
                    self.head = curr.next
                    if self.head:
                        self.head.prev = None
                # Case 2: Deleting a middle or last node
                else:
                    if curr.next:
                        curr.next.prev = curr.prev
                    if curr.prev:
                        curr.prev.next = curr.next
                return True # Successfully deleted
            curr = curr.next
        return False # Key not found

    def display_forward(self):
        """Print the list from head to tail."""
        curr = self.head
        nodes = []
        while curr:
            nodes.append(str(curr.data))
            curr = curr.next
        print("None <- " + " <-> ".join(nodes) + " -> None")

    def display_backward(self):
        """Print the list from tail to head using the 'prev' pointers."""
        curr = self.head
        if not curr:
            print("List is empty")
            return
            
        # Move to the last node
        while curr.next:
            curr = curr.next
            
        nodes = []
        while curr:
            nodes.append(str(curr.data))
            curr = curr.prev
        print("None <- " + " <-> ".join(nodes) + " -> None")

# --- Execution / Test Section ---
if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("--- Adding Elements ---")
    dll.append(10)
    dll.append(20)
    dll.prepend(5)
    dll.display_forward()   # Output: None <- 5 <-> 10 <-> 20 -> None

    print("\n--- Verifying Backward Traversal ---")
    dll.display_backward()  # Output: None <- 20 <-> 10 <-> 5 -> None

    print("\n--- Deleting 10 (Middle Node) ---")
    dll.delete(10)
    dll.display_forward()   # Output: None <- 5 <-> 20 -> None      