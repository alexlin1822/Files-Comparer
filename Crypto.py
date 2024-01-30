import re
from collections import Counter


def clean_up_string(input_str):
    """Remove all non-alphanumeric characters from a string."""
    return re.sub('[^a-zA-Z]+', '', input_str.upper())


def sort_key(row):
    """
    Custom sort key function for the sorted() function.

    Args:
        row: A list representing a row in the array.

    Returns:
        A tuple containing the first element of the row and the second element.
    """
    return (row[0], row[1].upper())


def count_words(input_str):
    """Count the number of words in a string."""
    results = []

    char_counts = Counter(input_str)
    for char, count in char_counts.items():
        results.append([count, char])

    # results = sorted(results, key=lambda x: x[0], reverse=True)
    results = sorted(results, key=sort_key, reverse=True)
    return results
    # for result in results:
    #     print(result[1], result[0])


def read_file_to_string(filename):
    """Reads the contents of a file into a string.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The entire contents of the file as a string.
    """

    with open(filename, 'r') as file:
        text = file.read()
    return text


def find_char_position_in_first_column(array, char_to_find):
    """Finds the position (row index) of the first occurrence of the given character in the first column of the 2D array.

    Args:
        array: The 2D array to search.
        char_to_find: The character to find.

    Returns:
        The row index of the first occurrence of the character, or -1 if not found.
    """

    for i, row in enumerate(array):
        if row[1] == char_to_find:
            return i
    return -1


if __name__ == "__main__":
    # input_str = "Helloabcdefghijklmnopqrstuvwxyz99832749287World!"
    input_str = clean_up_string(read_file_to_string("646053.txt"))

    ciphertext = "PBFPVYFBQXZTYFPBFEQJHDXXQVAPTPQJKTOYQWIPBVWLXTOXBTFXQWAXBVCXQWAXFQJVWLEQNTOZQGGQLFXQWAKVWLXQWAEBIPBFXFQVXGTVJVWLBTPQWAEBFPBFHCVLXBQUFEVWLXGDPEQVPQGVPPBFTIXPFHXZHVFAGFOTHFEFBQUFTDHZBQPOTHXTYFTODXQHFTDPTOGHFQPBQWAQJJTODXQHFOQPWTBDHHIXQVAPBFZQHCFWPFHPBFIPBQWKFABVYYDZBOTHPBQPQJTQOTOGHFQAPBFEQJHDXXQVAVXEBQPEFZBVFOJIWFFACFCCFHQWAUVWFLQHGFXVAFXQHFUFHILTTAVWAFFAWTEVOITDHFHFQAITIXPFHXAFQHEFZQWGFLVWPTOFFA"
    ciphertext = clean_up_string(ciphertext)

    # print(count_words(clean_up_string(input_str)))
    # print(count_words(clean_up_string(ciphertext)))
    key_frq = count_words(input_str)
    ciphertext_frq = count_words(ciphertext)

    # for text in key_frq:
    #     if text != None:
    #         print(text[1])

    # print("=============================================")
    # for text in ciphertext_frq:
    #     if text != None:
    #         print(text[1])

    # i = 0

    # print(i)

    # print(len(key_frq))
    # print(len(ciphertext_frq))

    # for text1, text2 in zip(key_frq, ciphertext_frq):
    #     print(text1[1]+" = " + text2[1])
    # i += 1

    print("=============================================")

    new_string = ""
    for c in ciphertext:
        position = find_char_position_in_first_column(ciphertext_frq, c)
        new_string += key_frq[position][1]

    print(new_string)
