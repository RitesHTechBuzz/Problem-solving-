#take input from a list can be done via two steps :
#directly form the list , normal appending converting the string into int
# or via list and map functions where we it is not required to input the size of the list already given 

my_list = []
elements_size = int(input("Enter the size of numbers"))
for i in range(elements_size):
    element  = input(f"Enter the element ")
    my_list.append(element)

print(my_list)