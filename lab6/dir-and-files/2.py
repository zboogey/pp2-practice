import os

def check_path_access(path):
    print("Path:", path)
    print("Existence:", os.path.exists(path))
    print("Readability:", os.access(path, os.R_OK))
    print("Writability:", os.access(path, os.W_OK))
    print("Executability:", os.access(path, os.X_OK))

if __name__ == "__main__":
    specified_path = input("Enter the specified path: ")
    check_path_access(specified_path)
