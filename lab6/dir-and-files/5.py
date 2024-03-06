def write_list_to_file(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"List has been written to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    my_list = input("Enter the elements of the list (separated by space): ").split()
    write_list_to_file(filename, my_list)
