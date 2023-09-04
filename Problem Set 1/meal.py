def main():
    time = input()
    times = convert(time)

    if (times >= 7 and times <= 8):
        meal = "Breakfast Time"
    elif (times >= 12 and times <= 13):
        meal = "Lunch Time"
    elif (times >= 18 and times <= 19):
        meal = "Dinner Time"
    else:
        meal = ""

    print(meal)

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)/60
    return float(hours) + minutes

if __name__ == "__main__":
    main()