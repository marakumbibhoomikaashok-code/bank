def bankoper(initialBal, deposit, withdraw):
    totalBal = initialBal + deposit
    updateBal = totalBal - withdraw

    return totalBal, updateBal

if __name__ == "__main__":
    initialBal = int(input("Enter am as initial Balance"))
    deposite = int(input("Enter amount to deposite"))
    withdraw = int(input("Enter withdrawal amount"))

    totalBal, updateBal = bankoper(initialBal, deposite, withdraw)

    print("Toatal Balance:", totalBal)
    print("Update Balance:", updateBal)

