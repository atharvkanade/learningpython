""" Convert numbers into list and tuple"""
values = input("Enter numbers seprated by comma  : ")
list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)
