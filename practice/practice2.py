# or via list and map functions where we it is not required to input the size of the list already given 
inputs = input("Enter the elements separated by space:")
List_elements = list(map(int,inputs.split()))
print(List_elements)