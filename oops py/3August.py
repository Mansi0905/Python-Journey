
# n=5
# i=1
# j=5
# while i<= n:
#     if j>= i:
        
#         print("*", end="")
#         j-=1
#     else:
#         print(" ", end="")
#     if j < i:
#         i+=1
#         j=5
#         print()


# i=1
# while i <= 5:
#     j=1
#     while j <= 5:
#         if j >= 6-i:
#             print ("*", end=" ")
#         else:
#             print(" ", end=" ")
#         j+=1
#     print ()
#     i+=1


# i= 1
# while i <= 4:
#     j=1
#     while j <= 7:
#         if j >= 5 -i and j <= i+3:
#          print("*", end = " ")
#         else:
#             print(" ",  end="")
#         j+= 1
#     print()
#     i += 1

# i= 1
# while i <= 4:
#     j=1
#     while j <= 7:
#         if j >= i and j <= 8-i:
#          print("*", end = " ")
#         else:
#             print(" ",  end="")
#         j+= 1
#     print()
#     i += 1

# i= 1
# while i <= 7:
#     j=1
#     while j <= 7:
#         if j >= 5-i and j <= i+3 and j >= i-3 and j<= 11-i:
#          print("*", end = " ")
#         else:
#             print(" ",  end="")
#         j+= 1
#     print()
#     i += 1


arr =[5,4,7,11,3]

for num in arr:
    print(f"{num}:")
    print("*\n" * num)