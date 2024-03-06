import re

def replace_characters(string):

    pattern = r'[ ,.]'
    
    new_string = re.sub(pattern, ':', string)
    
    return new_string

if __name__ == "__main__":
    input_string = "This is a sample, string. With spaces and dots."
    replaced_string = replace_characters(input_string)
    print("Original string:", input_string)
    print("Replaced string:", replaced_string)
