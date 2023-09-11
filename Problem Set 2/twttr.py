line = input("Input: ")

lst = []

#Append to the list except vowels
for i, ch in enumerate(line):
    if ch  not in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        lst.append(ch)

# Unpacking using "*"
print("Output: ",*lst, sep="")

