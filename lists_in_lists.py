def find_common_elements(list1: list, list2: list) -> list:
    """Function returns a list with common elements of two given lists"""
    common_elements = []
    for element in list1:
        element_quantity_list1 = list1.count(element)
        element_quantity_list2 = list2.count(element)
        if element not in common_elements:
            if element_quantity_list1 > element_quantity_list2:
                for num in range(element_quantity_list2):
                    common_elements.append(element)
            else:
                for num in range(element_quantity_list1):
                    common_elements.append(element)
    return common_elements


list_of_lists = [[1,2,3,4,4,4],[1,2, 4, 4], []]
common_elements = find_common_elements(list_of_lists[0], list_of_lists[1])
for index in range(2, len(list_of_lists)):
    common_elements = find_common_elements(common_elements, list_of_lists[index])
print(common_elements)
