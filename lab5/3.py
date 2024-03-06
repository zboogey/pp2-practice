import re

def find_sequences(pattern, string):
    sequences = re.findall(pattern, string)

    if sequences:
        print("Sequences found:", sequences)
    else:
        print("No sequences found.")

if __name__ == "__main__":
    pattern = r'[a-z]+_[a-z]+'
    strings = [
        "hello_world",
        "Python_is_great",
        "this_is_an_example",
        "123_ABC_456",
        "no_underscores_here"
    ]

    for string in strings:
        print("\nString:", string)
        find_sequences(pattern, string)
