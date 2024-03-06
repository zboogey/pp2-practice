import re

def match_string(pattern, string):
    match = re.match(pattern, string)

    if match:
        print("String '{}' matches the pattern '{}'.".format(string, pattern))
    else:
        print("String '{}' does not match the pattern '{}'.".format(string, pattern))

if __name__ == "__main__":
    pattern = r'ab*'
    strings = ["a", "ab", "abb", "abbb", "abc", "b", "bb"]

    for string in strings:
        match_string(pattern, string)
