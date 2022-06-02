import re
def read_some_file(some_file_name: str) -> list:
    """this function reads file, returns list of lines from file's text"""
    data = open(some_file_name).readlines()
    return data


def filter_out_words(data: list, bad_words_file: str) -> str:
    """this function removes file2's words from file1 if they exist in file1"""
    bad_words = open(bad_words_file).read().split()
    new_data = []
    for line in data:
        for word in bad_words:
            if word in line:
                line = line.replace(word, '')
        new_data.append(line)
    return ''.join(new_data)


def write_text_into_file(data: list, bad_words_file: str, new_filе_name: str) -> None:
    """this function writes text into a new file"""
    with open(new_filе_name, 'w') as opened_new_file:
        opened_new_file.write(filter_out_words(data, bad_words_file))


write_text_into_file(read_some_file('text.txt'), ' bad_words.txt', 'new_sorted_file')



