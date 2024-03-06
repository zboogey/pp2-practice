def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return -1

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    lines = count_lines(filename)
    if lines != -1:
        print(f"Number of lines in {filename}: {lines}")