def convert(line: str):
    emot_1 = ":)"
    emot_2 = ":("
    line = line.replace(emot_1, "😊")
    line = line.replace(emot_2, "😒")
    print(line)

def main():
    line = input()
    convert(line)

if __name__ == "__main__":
    main()