import re

def split_at_uppercase(string):
    split_string = re.findall('[A-Z][^A-Z]*', string)
    return split_string

if __name__ == "__main__":
    input_string = "SplitThisStringAtUppercaseLetters"
    split_string = split_at_uppercase(input_string)
    print("Original string:", input_string)
    print("Split string:", split_string)
