from functools import reduce

def multiply_list(numbers):
    product = reduce(lambda x, y: x * y, numbers)
    return product

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = multiply_list(numbers)
    print("List:", numbers)
    print("Product:", result)
