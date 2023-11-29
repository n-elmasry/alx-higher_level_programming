#!/usr/bin/python3
"""  prints a text with 2 new lines after special characters """


def text_indentation(text):
    """  prints a text with 2 new lines after special characters """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    punctuation_marks = [".", "?", ":"]

    for char in text:
        result += char
        if char in punctuation_marks:
            result += "\n\n"

    for line in result.split('\n'):
        print(line.strip())
