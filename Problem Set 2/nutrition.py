line = input("Item: ")

if line.lower() == "apple":
    c = 130
elif line.lower() == "avocado":
    c = 50
elif line.lower() == "banana":
    c = 110
elif line.lower() == "cantaloupe":
    c = 50
elif line.lower() == "grapefruit":
    c = 60
elif line.lower() == "grapes":
    c = 90
elif line.lower() == "honeydew melon":
    c = 50
elif line.lower() == "kiwifruit":
    c = 90
elif line.lower() == "lemon":
    c = 15
elif line.lower() == "lime":
    c = 20
elif line.lower() == "nectarine":
    c = 60
elif line.lower() == "orange":
    c = 80
elif line.lower() == "peach":
    c = 60
elif line.lower() == "pear":
    c = 100
elif line.lower() == "pineapple":
    c = 50
elif line.lower() == "plums":
    c = 70
elif line.lower() == "strawberries":
    c = 50
elif line.lower() == "sweet cherries":
    c = 100
elif line.lower() == "tangerine":
    c = 50
elif line.lower() == "watermelon":
    c = 80
else:
    c = " "

print(f"Calories: {c}")