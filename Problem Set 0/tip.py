def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollars: str):
    dollars = dollars.lstrip("$")
    dollars = float(dollars)
    return dollars

def percent_to_float(percent: str):
    percent = percent.rstrip("%")
    percent = (float(percent)/100)
    return percent

if __name__ == "__main__":
    main()