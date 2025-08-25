# tests.py
# from functions.get_files_info import get_files_info
from functions.write_file import write_file

def lorem_test():
    return write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")

def morelorem_test():
    return write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")

def temp_test():
    return write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

def main():
    print(lorem_test())
    print(morelorem_test())
    print(temp_test())
              
if __name__ == "__main__":
    main()
