def find_common_elements(list1: list, list2: list) -> list:
    """Function removes not common elements of lists from list1"""
    for element in list1:
        n = 1
        if element in list2:
            if list1.count(element) >= list2.count(element):
                while list1.count(element) - list2.count(element) >= n:
                    list1.remove(element)
                    n += 1
        else:
            list1.remove(element)
    return list1


lst1 = [[1, 76, 99, 4, 99, 99],
        [1, 99, 99, 4, 76, 2, 52, 23, 22, 77],
        [99, 99, 17, 4, 2, 76, 66, 14],
        [1, 76, 99, 2, 4],
        [1, 76, 2, 4, 99]]
index = 2
common_elements = find_common_elements(lst1[0], lst1[1])
while index < len(lst1):
    common_elements = find_common_elements(common_elements, lst1[index])
    index += 1
print(common_elements)
