file = input("File name: ").lower()

if file.endswith(".jpeg"):
    print("Image/jpeg")
elif file.endswith(".jpg"):
    print("Image/jpg")
elif file.endswith(".gif"):
    print("Image/gif")
elif file.endswith(".png"):
    print("Image/png")
elif file.endswith(".pdf"):
    print("Document/pdf")
elif file.endswith(".txt"):
    print("Text/txt")
elif file.endswith(".zip"):
    print("Zipped/zip")
else:
    print("application/octet-stream")