def filter_out_words(data: list, bad_words: list) -> list:
    """Function remove all words from list of bad_words"""
    new_data = []
    for line in data:
        for word in bad_words:
            if word in line:
                line = line.replace(word, '')
        new_data.append(line)
    return new_data


def get_data_from_file(filepath: str) -> list:
    """Convert data from file to list"""
    with open(filepath, encoding="utf-8") as file:
        return list(file.readlines())


def write_data(filepath: str, data: list) -> None:
    """Write data into the file"""
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(data)


def main():
    """Main function"""
    data = get_data_from_file("text.txt")
    words = get_data_from_file("bad_words.txt")
    filtered_data = filter_out_words(data, words)
    write_data("filtered_text.txt", filtered_data)


if __name__ == '__main__':
    main()