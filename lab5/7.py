import re

def snake_to_camel(snake_case_string):
    camel_case_string = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case_string)
    return camel_case_string

if __name__ == "__main__":
    snake_case_string = "hello_world_this_is_snake_case"
    camel_case_string = snake_to_camel(snake_case_string)
    print("Snake case string:", snake_case_string)
    print("Camel case string:", camel_case_string)
