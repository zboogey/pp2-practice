import re

def camel_to_snake(camel_case_string):
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_string).lower()
    return snake_case_string

if __name__ == "__main__":
    camel_case_string = "ConvertThisCamelCaseStringToSnakeCase"
    snake_case_string = camel_to_snake(camel_case_string)
    print("Camel case string:", camel_case_string)
    print("Snake case string:", snake_case_string)
