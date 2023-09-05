def coke(amount: int):
    total = 50

    while True:
    
        if amount in [25, 10, 5]:
            due = total - amount
            total = due
            continue
        else:
            due = 50
        return due

def main():
    print("Amount Due: 50")
        
    while True:
        
        amount = int(input("Insert Coin: "))
        new = coke(amount)

        if new == 0:
            print(f"Chanege Owed: {new}")
            break
        else:
            print(f"Amount Due: {new}")

if __name__ == "__main__":
    main()
        