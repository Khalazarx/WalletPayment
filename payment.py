    # script payment
addressWallet= str(input("Insert Address Wallet: "))
nameWallet= str(input("Insert Your Name: "))
recvAddress= str(input("Insert Receiver Address: "))

    # prosesDeposit

while True:
    amountPay = float(input("Insert Deposit: "))
    try:
        value = int(amountPay)
        if amountPay >= 10000:
            print ("--------------------------------Deposit Success------------------------------------------------")
            print ("Wallet receiver : " + recvAddress)
            print ("Status : Success")
            print ("Wallet Name : " + nameWallet)
            print ("Wallet Address : " + addressWallet)
            print (f"Total Deposit : {amountPay}")
            print ("--------------------------------Description------------------------------------------------")
            print (f"{nameWallet} your deposit successfully {amountPay} to {recvAddress}")
            break
        else:
            print ("-------------------------------Deposit Failed-------------------------------------------------")
            # menampilkan proses jika gagal harus transer lebih dari 10.000
            print (f"Deposit must be more than 10.000")
    except ValueError:
                print("Deposit must be a number")


