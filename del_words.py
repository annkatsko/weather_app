def open_and_read_some_file(some_file_name: str, designation='+') -> list:
    """this function opens and reads file, returns list of words from file's text"""
    list_of_words = open(some_file_name).read().split()
    return list_of_words


def filter_out_words(file1: list, file2: list) -> list:
    """this function removes file2's words from file1 if they exist in file1 """
    for i in file2:
        if i in file1:
            file1.remove(i)
    return file1


def del_words(name_filе1: str, name_filе2: str, new_filе_name: str):
    """this function removes file2's words from file1 if they exist in file1, and writes text into a new file"""
    list_of_words_from_file1 = open_and_read_some_file(name_filе1)
    list_of_words_from_file2 = open_and_read_some_file(name_filе2)
    with open(new_filе_name, 'w') as opened_new_file:
        opened_new_file.write(' '.join(filter_out_words(list_of_words_from_file1, list_of_words_from_file2)))


del_words('text.txt', ' bad_words.txt', 'new_sorted_file')
