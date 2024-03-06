import os

def delete_file(path):
    if os.path.exists(path):
        try:
            if os.access(path, os.F_OK):
                os.remove(path)
                print(f"File {path} has been deleted successfully.")
            else:
                print("File access denied.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
    else:
        print("File does not exist.")

if __name__ == "__main__":
    specified_path = input("Enter the path of the file to delete: ")
    delete_file(specified_path)
