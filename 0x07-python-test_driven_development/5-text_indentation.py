def text_indentation(text):
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
