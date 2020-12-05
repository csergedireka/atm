def change_pin():
    new_pin = int(input("Enter your new PIN:"))
    return new_pin


pin = 1234
sum = 1800

k = False
i = 0
while True:
    k = False
    message = "Dear Customer! Please enter your PIN:"
    while i < 3 and not k:
        entered_pin = int(input(message))
        if entered_pin == pin:
            k = True
        else:
            message = "PIN is invalid. Please enter again:"
            i += 1
        if k:
            print("Select an option:")
            print("1.Change PIN")
            print("2.Withdraw money")
            selected_option = int(input("Select an option:"))

            if (selected_option == 1):
                pin = change_pin()
                print("You're PIN code was succesfully modified!")
                i = 0
                k = False
            elif (selected_option == 2):
                l = False
                print("Account balance: ", sum)
                message = "Enter the sum:"
                while not l:
                    withdraw_sum = int(input(message))
                    if withdraw_sum <= sum:
                        sum = sum - withdraw_sum
                        print("The transaction was completed succesfully, your account balance is: ", sum)
                        l = True
                    else:
                        message = "The amount you're asking for is exceeding the total of your account. Please reenter the sum:"
        elif i == 3:
            print("Your accout has been blocked. Please call the customer service to unblock it: +495679427052")