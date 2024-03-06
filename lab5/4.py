import re

def find_sequences(pattern, string):
    sequences = re.findall(pattern, string)

    if sequences:
        print("Sequences found:", sequences)
    else:
        print("No sequences found.")

if __name__ == "__main__":
    pattern = r'[A-Z][a-z]+'
    strings = [
        "Hello World",
        "PythonIsGreat",
        "ThisIsAnExample",
        "123_ABC_456",
        "NoLowercaseLettersHere"
    ]

    for string in strings:
        print("\nString:", string)
        find_sequences(pattern, string)
