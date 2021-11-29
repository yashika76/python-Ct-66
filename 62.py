list1 = [11, 5, 17, 18, 23]
total=0
for i in range(0, len(list1)):
    total = total + list1[i]
 
print("Sum of all elements in given list: ", total)
Sum of all elements in given list:  74
  
  
  #63)Python program to insert a number to given position in a list.
print("Enter 10 Elements of List: ")
nums = []
for i in range(10):
    nums.insert(i, input())
print("Enter an Element to Insert at End: ")
elem = input()
nums.append(elem)
print("\nThe New List is: ")
print(nums)