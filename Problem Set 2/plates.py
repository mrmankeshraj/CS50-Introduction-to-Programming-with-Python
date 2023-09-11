def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (2 <= len(s) <= 6) and s[:3].isalpha():
        valid = True

    if s.beginswith(isalpha()) and s.endswith(isnum())


if __name__ == "__main__":
    main()