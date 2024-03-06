import re

def insert_spaces(string):
    spaced_string = re.sub(r'(?<!^)(?=[A-Z])', ' ', string)
    return spaced_string

if __name__ == "__main__":
    input_string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
    spaced_string = insert_spaces(input_string)
    print("Original string:", input_string)
    print("Spaced string:", spaced_string)
