greet = input("Greating: ")

if greet.lower().lstrip(" ").startswith("hello"):
    print("$0")
elif greet.lower().lstrip(" ").startswith("h"):
    print("$20")
else:
    print("$100")