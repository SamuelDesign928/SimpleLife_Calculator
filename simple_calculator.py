def simple_calculator():
    print(" ")
    print("> Press E to exit")

    while True:
        user_input = input("> Enter a calculation: ")

        if user_input.lower() == 'e':
            break
        try:
            result = eval(user_input)
            print(f"> Result: {result}")
            print(" ")
        except Exception as e:
            print(3)
    print(" ")
    print("> Calculator closed")



def main():
    global VAT
    VAT = 0.20
    INCOME = 21570
    BRACKET = 0.20
    running = True
    options = {"1":"VAT", "2":"Tax", "3":"Calculator", "4":"READ ME"}
    print("> Welcome to Finance Calculator")
    print(" ")
    while running:
        for key, value in options.items():
            print(f"{key}., {value}")
        choice = input("> Press E to exit: ")
        if choice.upper() == "E":
            quit()
        if choice == "1":
            print("> As of August 2024, Standard VAT in UK is 20%\n"
                  "> Some goods and services, (eg children’s car seats and home energy) are 5%\n"
                  "> Most food and children’s clothes are 0%\n")
            try:
                print(" ")
                VAT = float(input(">> Enter the VAT <e.g 0.2 for 20%>: "))
                cost = float(input(">> Enter the cost of product: "))
            except Exception as e:
                print(e)
                pass
            else:
                print(f"> The VAT is {cost * VAT} making the total\n>>{cost + (cost*VAT)}")
                pass
        if choice == "2":
            print("> Personal Allowance	Up to £12,570 0%\n"
                  "> Basic rate	£12,571 to £50,270	20%\n"
                  "> Higher rate    £50,271 to £125,140 40%\n"
                  "> Additional rate	over £125,140	45%")
            try:
                INCOME = float(input(">> Enter your annual income <e.g 30500>: £"))
                BRACKET = float(input(">> Enter a your tax bracket <e.g 0.2 for 20%>: "))
            except Exception as e:
                print(e)
                pass
            else:
                print(f"> Tax owed is £{(INCOME-12570) * BRACKET}")
        if choice == "3":
            simple_calculator()
        if choice == "4":
            print("> Note from author\n"
                  "> This was a coding challenge, I made this in 30 minutes so whilst I try to be accurate\n"
                  "> Take the calculations with a grain of salt\n"
                  "\n"
                  "V Press Any key to go back to the menu V")
            if input():
                pass



if __name__ == "__main__":
    main()
