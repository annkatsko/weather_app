lst1 = [[1, 76, 2,  99, 99, 99],
        [1, 99, 99, 99, 76, 2, 52, 23, 22, 77],
        [1, 99, 10, 17, 49, 35, 66, 14],
        [1, 99, 99, 2],
        [1, 99, 99, 99, 99, 2]]
common_elements = []
for element in lst1[0]:
    if element in common_elements:
        continue
    for element2 in lst1[1]:
        if element == element2:
            common_elements.append(element)
print(common_elements)
for index in range(2, len(lst1)):
    for elem in common_elements:
        if elem in lst1[index]:
            continue
        else:
            common_elements.remove(elem)
print(common_elements)











