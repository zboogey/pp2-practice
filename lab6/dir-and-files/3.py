import os

def test_path_existence_and_extract_parts(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist.")

if __name__ == "__main__":
    specified_path = input("Enter the specified path: ")
    test_path_existence_and_extract_parts(specified_path)
