answer = input("What is the answer to the Great Question of life, the Universe, and everything? ")

if answer == "42":
    print("Yes")
elif answer.lower() == "forty-two":
    print("Yes")
elif answer.lower() == "forty two":
    print("Yes")
else:
    print("No")
