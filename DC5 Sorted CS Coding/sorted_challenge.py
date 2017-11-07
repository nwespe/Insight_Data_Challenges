# coding: utf-8

import sys

"""
Please write a program that takes a list of strings containing
integers and words and returns a sorted version of the list.
The goal is to sort this list in such a way that all words are in
alphabetical order and all integers are in numerical order.
Furthermore, if the nth element in the list is an integer it must
remain an integer, and if it is a word it must remain a word.

In addition, the strings and integers may contain characters that are
ascii symbols that neither belong to letter set nor digit set (i.e. "#", "%", ";", etc).
You are required to remove them during the process so that the output
will contain only letters or digits. For example, if a string is "sym*bo+l",
the output should be "symbol". If an integer is "12%3", the output should be "123".
You don't have to worry about strings or integers that contain only non­letter­non­digit characters,
like "^!?", "&", etc.

For example: 20 cat bi?rd 12 do@g >> should read >> 12 bird cat 20 dog
"""


def read_input(input_file):
    """ Read single line from file into a list of strings """

    with open(input_file, 'r') as f:
        readfile = f.read().split(' ')
    return readfile


def clean_symbols(int_word_list):
    """ Remove any non-alphanumeric symbols from the ints and words in the list """

    for i, x in enumerate(int_word_list):
        if not x.isalnum():
            cleaned_x = [a for a in x if a.isalnum()]
            new_x = ''.join(cleaned_x)

            # special handling for negative integers
            if new_x.isdigit() and '-' in x:  # check for negative sign
                dash_location = x.find('-')
                first_num_location = x.find(new_x[0])
                if dash_location < first_num_location:
                    new_x = '-' + new_x

            int_word_list[i] = new_x
    return int_word_list


def separate_ints_words(int_word_list):
    # separate into two lists, record positions of ints vs. words in original list
    int_list = []
    word_list = []
    indices = []
    for x in int_word_list:
        if x.isdigit():
            int_list.append(int(x))
            indices.append(0)
        elif x[0] == '-' and x[1:].isdigit():  # special handling of negative numbers
            int_list.append(int(x))
            indices.append(0)
        else:
            word_list.append(x)
            indices.append(1)
    return int_list, word_list, indices


def sort_lists(int_list, word_list):
    # use reverse order to use .pop() later
    return sorted(int_list, reverse=True), sorted(word_list, reverse=True)


def reassemble_list(int_list, word_list, indices):
    # recombine sorted lists using position information from original list
    sorted_joined_list = []
    for x in indices:
        if x == 0:
            sorted_joined_list.append(int_list.pop())
        else:
            sorted_joined_list.append(word_list.pop())
    return sorted_joined_list


def save_output(output_list):
    with open('results.txt', 'w') as f:
        f.write(' '.join(str(x) for x in output_list))


def main(input_file):
    print 'received input file ' + input_file
    readfile = read_input(input_file)
    cleaned_list = clean_symbols(readfile)
    int_list, word_list, indices = separate_ints_words(cleaned_list)
    sorted_ints, sorted_words = sort_lists(int_list, word_list)
    output_list = reassemble_list(sorted_ints, sorted_words, indices)
    save_output(output_list)


if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)
