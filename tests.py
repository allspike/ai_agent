# tests.py
# from functions.get_files_info import get_files_info

from functions.get_file_content import get_file_content
# def current_test():
#    print("Result for current directory:")
#    print(get_files_info("calculator", "."))

# def pkg_test():
#    print("Result for 'pkg' directory:")
#    print(get_files_info("calculator", "pkg"))

# def bin_test():
#    print("Result for '/bin' directory:")
#    print(get_files_info("calculator", "/bin"))

# def illegal_test():
#    print("Result for '../' directory'")
#    print(get_files_info("calculator", "../"))

# def main():
#    current_test()
#    pkg_test()
#    bin_test()
#    illegal_test()

def main_test():
    print(get_file_content("calculator", "main.py"))
        
def pkg_calc_test():
    print(get_file_content("calculator", "pkg/calculator.py"))

def cat_test():
    print(get_file_content("calculator", "/bin/cat"))

def dne_test():
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

def lorem_test():
    print(get_file_content("calculator", "lorem.txt"))

def main():
    main_test()
    pkg_calc_test()
    cat_test()
    dne_test()
    lorem_test()
        
if __name__ == "__main__":
    main()
