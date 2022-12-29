#!/usr/bin/python3
"""
Module for indenting a text by adding new lines after certain characters.

Example:
    >>> text_indentation("Hello. This is a test: 1, 2, 3?")
    Hello.
    <BLANKLINE>
    This is a test:
    <BLANKLINE>
    1, 2, 3?
"""


def text_indentation(text):
    """
    Indent a text by adding new lines after certain characters.

    Args:
        text (str): The text to indent.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Add new lines after ., ?, and : characters
    text = text.replace(
        ".", ".\n\n"
    ).replace(
        "?", "?\n\n"
    ).replace(
        ":", ":\n\n"
    )

    arr = text.split("\n")

    # Split the text into lines and print each line
    for idx, line in enumerate(arr):
        if idx + 1 == len(arr):
            print(line.strip(), end="")
        else:
            print(line.strip())
