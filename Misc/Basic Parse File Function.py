def parse_file(words_file_name):
    """
    Parses a text file line by line and adds it to a list to be returned
    :param words_file_name: The file that will be parsed
    :return: The lines of the text file minus the first line
    """
    words_list = []
    try:
        open_file = open(words_file_name, 'r')
        contents = open_file.readline()
        contents = contents[:-1]
        while contents:
            words_list.append(contents.split())
            contents = open_file.readline()
            contents = contents[:-1]
        open_file.close()
    except IOError:
        print("File does not exist! Try again.")
    words_list = words_list[1:]
    return words_list
