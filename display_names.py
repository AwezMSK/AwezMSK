import sys

def main():
    if len(sys.argv) >= 3:
        first_name, middle_name = sys.argv[1], sys.argv[2]
    else:
        first_name = input("Enter first name: ")
        middle_name = input("Enter middle name: ")
    print("First name:", first_name)
    print("Middle name:", middle_name)

if __name__ == "__main__":
    main()
