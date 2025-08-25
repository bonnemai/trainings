n=65535
# nb=8
binary=bin(n)
print(binary)

binary_str=str(binary)
print(binary_str)

binary_str=binary_str[2:]
print(binary_str)

previous = None
max=0
lists=[]
current_list=[]
for binary_digit in binary_str:
    if previous is None:
        previous = binary_digit
        current_list.append(binary_digit)
    else:
        if previous == binary_digit:
            current_list.append(binary_digit)
        else:
            lists.append(current_list)
            current_list=[binary_digit]
            previous=binary_digit
            
if current_list:
    lists.append(current_list)
print(lists)

max=0
for l in lists:
    if len(l) > max:
        max = len(l)
print(max)