import os

def generate_text_files():
    for char in range(65, 91):  # ASCII codes for A-Z
        filename = chr(char) + ".txt"
        with open(filename, 'w') as file:
            file.write(f"This is file {filename}")

if __name__ == "__main__":
    generate_text_files()
    print("Text files generated successfully.")
