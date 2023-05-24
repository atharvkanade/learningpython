total = 0

n1 = int(input("Enter first element of list :"))
n2 = int(input("Enter second element of list :"))
n3 = int(input("Enter third element of list :"))
n4 = int(input("Enter fourth element of list :"))
n5 = int(input("Enter fifth element of list :"))

list1 = [n1, n2, n3, n4, n5]

for ele in range(0, len(list1)):

    total = total + list1[ele]

print("Sum of all elements in given list: ", total)

