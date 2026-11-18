def bankoper(initialBal, deposit, withdraw):
    totalBal = initialBal + deposit
    updateBal = totalBal - withdraw

    return totalBal, updateBal

if __name__ == "__main__":
    initialBal = int("sys.argv[1]")
    deposite = int("sys.argv[2]")
    withdraw = int("sys.argv[3]")

    totalBal, updateBal = bankoper(initialBal, deposite, withdraw)

    print("Toatal Balance:", totalBal)
    print("Update Balance:", updateBal)

