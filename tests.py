# tests.py
from functions.get_files_info import get_files_info

def current_test():
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

def pkg_test():
    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

def bin_test():
    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))

def illegal_test():
    print("Result for '../' directory'")
    print(get_files_info("calculator", "../"))

def main():
    current_test()
    pkg_test()
    bin_test()
    illegal_test()
if __name__ == "__main__":
    main()
