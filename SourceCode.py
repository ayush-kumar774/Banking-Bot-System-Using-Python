'''
     Author              :- AAYUSH KUMAR
     SECTION             :- K18MS
     ROLL NUMBER         :- B 60
     REGISTRATION NUMBER :- 11803263
'''
print("===================================================================================================================================================================================================================")
print()
print("                                                           WELCOME TO BANKING BOT SYSTEM                                                                      ")
print()
print("==========================================================================================================================================================================================================================")
print("Say Hello! to Start Chatting")
val = input()
val2 = "Hello"
val3 = "hello"
if(val == val2 or val == val3):
    print("Hi, nice to meet you:)")
    print("How can I help you?")
    print("Type any of the task below :- ")
    print("1. Add beneficiary")
    print("2. Fund Transfer")
    print("3. Mini Statement")
    print("4. Balance Check")
    print()
    print("I want to add beneficiary")
    print("I want to trasfer money")
    print("I want to check my account balance")
    print("I want to get mini-statement")
    print("Please input a task :- ")
    input1 = input()

    input2 = "I want to add beneficiary"
    input3 = "i want to add beneficiary"

    input4 = "I want to transfer money"
    input5 = "i want to transfer money"

    input6 = "I want to check my account balance"
    input7 = "i want to check my account balance"

    input8 = "i want to get mini-statement"
    input9 = "I want to get mini-statement"

    if(input1 == input2 or input1 == input3):
        print("Enter your beneficiary name:- ")
        Name = input()
        print("Your beneficiary name is", Name)
        print("Enter beneficiary account number:- ")
        Account_number = input()
        print("Your beneficiary account number is ", Account_number)
        print("Benificiary Successfuly Added.")
        print("Press 1 to quit:- ")
        choice = int(input())
        if(choice == 1):
            print("Thanks For Using Our Boting Service!!")
            print("Hope You Liked Our Services.")

    if(input1 == input4 or input1 == input5):
        print("Quick Pay")
        print("Please enter the amount:- ")
        amount = int(input())
        print("Please enter the beneficiary account holder name:- ")
        name = input()
        print("Please enter the beneficiary account number:- ")
        Account_number2 = int(input())
        print("Please enter the beneficiary IFSC code:- ")
        IFSC_code = input()
        print("Enter linked account registered mobile number? ")
        Mobile_Number = input()
        print("Please type the OTP in Correct Format ")
        OTP = input()
        print("Savings No xxxxxxxxxxxxx7 Debited with INR ", amount , " towards NEFT Transfer to NEFT/", name)
        print("Press 1 to quit:- ")
        choice = int(input())
        if(choice == 1):
            print("Thanks For Using Our Boting Service!!")
            print("Hope You Liked Our Services.")

    if(input1 == input6 or input1 == input7):
        print("Enter your linked account mobile number:- ")
        mobile_number = input()
        print("Please type the OTP in correct Format:- ")
        otp = input()
        print("Welcome Mr. Aayush Singh Rajput!")
        print("Greeting from SBI!!")
        print("Account No. SBI001789454141")
        print("Current Balance = INR 15,000")
        print("Press 1 to quit:- ")
        choice = int(input())
        if(choice == 1):
            print("Thanks For Using Our Boting Service!!")
            print("Hope You Liked Our Services.")


    if(input1 == input8 or input1 == input9):
        print("Enter your linked account mobile number:- ")
        mobile_number = input()
        print("Please type the OTP in correct Format:- ")
        otp = input()
        print("Welcome Mr. Aayush Singh Rajput!")
        print("Greeting from SBI!!")
        print("Account No. SBI001789454141")
        print("TRANXCUB00000000001 | CREDIT | 75000  | 2019 - 25 - 12   04 : 34 : 16")
        print("TRANXCUB00000000002 | CREDIT | 75000  | 2020 - 25 - 01   05 : 30 : 10")
        print("TRANXCUB00000000003 | DEBIT  | 100000 | 2020 - 28 - 01   12 : 55 : 17")
        print("TRANXCUB00000000004 | DEBIT  | 5000   | 2020 - 25 - 02   21 : 41 : 10")
        print("TRANXCUB00000000005 | CREDIT | 75000  | 2020 - 25 - 02   20 : 28 : 05")
        print("TRANXCUB00000000006 | DEBIT  | 15000  | 2020 - 20 - 03   14 : 36 : 01")
        print("TRANXCUB00000000007 | DEBIT  | 4500   | 2020 - 21 - 03   16 : 45 : 30")
        print("TRANXCUB00000000008 | CREDIT | 4000   | 2020 - 22 - 03   18 : 39 : 59")
        print("TRANXCUB00000000009 | CREDIT | 55000  | 2020 - 23 - 03   06 : 12 : 55")
        print("TRANXCUB000000000010 | DEBIT | 45000  | 2020 - 24 - 03   08 : 46 : 40")

        print("Press 1 to quit:- ")
        choice = int(input())
        if(choice == 1):
            print("Thanks For Using Our Boting Service!!")
            print("Hope You Liked Our Services.")
