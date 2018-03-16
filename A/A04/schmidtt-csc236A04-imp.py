##################################################################################
# Author: Tradd Schmidt
# Username: schmidtt
#
# read_words adapted from
# http://stackoverflow.com/questions/13259288/returning-a-list-of-words-after-reading-a-file-in-python
#
# binary_search based off of code from Data Structures and Algorithms Using Python and C++ by David M. Reed and John
# Zelle on page 22
#
#
#
#
# Assignment: A04 Implementation
#
# Purpose: Take a text file and a given word, and search through the file to count the amount of times that word appears
##################################################################################

import time

def read_words(words_file_name):
    '''This function opens a file with the name in 'words_file', reads in
    the contents and returns a list of the words, stripped of whitespace.
    pre: none, as this function handles IOError for when the file is not there gracefully
    post: returns the list of words in the file, which is empty on an open fail. '''
    words_list =[]
    try:
        open_file = open(words_file_name, 'r')
        contents = open_file.readlines()

        # replace punctuation with a blank space
        punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
        for i in punctuation:
            for j in range(len(contents)):
                contents[j] = contents[j].replace(i,"")

        for i in range(len(contents)):
            contents[i].lower()
            words_list.extend((contents[i].lower()).split())
        open_file.close()
    except IOError:
        print("File does not exist! Try again.")
    return words_list


def linear_iteration(list_of_words, target_word):
    """
    This function iterates through a list and counts how many times a specific word appears. It also counts how long
    this takes.
    :param list_of_words: A list of strings
    :param target_word: A string
    :return: The amount of times a word appears as an integer and the time it took as an integer
    """
    t_one = time.time()
    word_count = 0
    for i in list_of_words:     # Iterates through the entire list linearly to check all words
        if i == target_word:
            word_count += 1
    t_two = time.time()
    run_time = t_two - t_one    # Checks the run time
    return word_count, run_time


def binary_search(list_of_words, target_word):
    """
    WIll sort a list of strings into alphabetical order and then use binary search to search for a target word. Both of
    these processes are timed and returned.
    :param list_of_words: A list of strings
    :param target_word: A string
    :return: The amount of times a word appears as an integer, how long it takes to sort as an integer, and the time it
    took to search as an integer.
    """
    word_count = 0
    t_one = time.time()
    l = sorted(list_of_words)
    t_two = time.time()
    sort_time = t_two - t_one   # Checks the time it took to sort
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        item = l[mid]
        if target_word == item:
            temp_mid = mid - 1        # This is a place holder for where the target word was found, but back one element
            while target_word == item:  # Goes one way and counts the amount time the word appears
                word_count += 1
                mid += 1
                item = l[mid]
                if target_word != item:  # This is for when the item is no longer in the area of the target_word
                    item = l[temp_mid]      # This starts the iteration to the other half of grouping of the target_word
                    while target_word == item:  # This continues moving left in the list until you run out of words
                        word_count += 1
                        temp_mid -= 1
                        item = l[temp_mid]
            t_three = time.time()           # This checks the run time
            search_time = t_three - t_two
            return word_count, sort_time, search_time
        elif target_word < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    file = input("Please input what file you would like to search.")
    word = input("Please input what file you would like to search.")
    list_of_words = read_words(file)
    count, run_time = linear_iteration(list_of_words, word)
    if count == 1:
        print("Linear Search: Your target word appeared " + str(count) + " time, and it took " + str(run_time) +
              " seconds to complete.")
    else:
        print("Linear Search: Your target word appeared " + str(count) + " times, and it took " + str(run_time) +
              " seconds to complete.")
    count, sort_time, run_time = binary_search(list_of_words, word)
    if count == 1:
        print("Binary Search: Your target word appeared " + str(count) + " time, it took " + str(sort_time) + " to sort, and it took "
              + str(run_time) + " seconds to complete.")
    else:
        print("Binary Search: Your target word appeared " + str(count) + " times, it took " + str(sort_time) + " to sort, and it took " +
              str(run_time) + " seconds to complete.")

if __name__ == '__main__':
    main()
