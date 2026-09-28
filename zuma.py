#Zuma Restaurant Shift profit repport
#Adds up Omakase(Omakase are a Chef selection of multiple dishes or combo of food)
#sales for each day, subtracts what each server were paid and saves the result in a text file 

#Import the necessary libraries
from datetime import date

# Omakase type and their prices in a dictionary format to use later
omakase_prices = {
    "Regular Omakase": 100.00,
    "Premium Omakase": 150.00,
    "Seasonal Omakase": 200.00
}

#Servers salary per hour in a dictionary format to use later
server_pay = {
    "Maria": 15.00,
    "Pasha": 16.50,
    "Isabel": 18.00
}

#File where profit repport is submitted
REPORT_FILE = "daily_reports.txt"


#a fuction with a while Loop with try and except
def get_whole_number(message):
    #While Loop asking asking until the message is 0 or more
    while True:
        answer = input(message)
        if answer.isdigit():
            return int(answer)
        print("Please type a whole number (0 or more).")


def get_hours(message):
    while True:
        answer = input(message)
        try:
            hours = float(answer)
            if hours >= 0:
                return hours
            print("Hours can't be negative.")
        except ValueError:
            print("Please type a number, like 8 or 7.5.")


# this fuction lets the user enter the omakase sales during the day
def record_sales():
    #creating a empty dictionary named sold
    sold = {}
    #loop the names of the omakases 
    for name in omakase_prices:
        sold[name] = 0

    menu = list(omakase_prices.keys())

    #Find what omakase was sold and display the name and its quantity
    #return the dictionary
    while True:
        print("\nWhich omakase was sold?")
        for number, name in enumerate(menu, start=1):
            print(f"  {number}. {name} (${omakase_prices[name]:.2f})")
        print("  0. Done entering sales")

        choice = get_whole_number("Choose a number: ")
        if choice == 0:
            break
        if choice > len(menu):
            print("That isn't on the list. Try again.")
            continue

        name = menu[choice - 1]
        quantity = get_whole_number(f"How many {name} were sold? ")
        sold[name] += quantity
        print(f"Added {quantity} {name}.")

    #Return the dictionary
    return sold


#Amount of hours worked per server
def record_hours():
    hours_worked = {}
    print("\nEnter the hours each server worked today.")
    for server in server_pay:
        hours_worked[server] = get_hours(f"Hours for {server}: ")
    return hours_worked


#Calculate everything and make the repport to append all together to the file txt 
def build_report(sold, hours_worked):
    #do the math for sales
    total_sales = 0
    for name, quantity in sold.items():
        total_sales += quantity * omakase_prices[name]

    #doing the math for hours worked per server 
    total_labor = 0
    for server, hours in hours_worked.items():
        total_labor += hours * server_pay[server]

    #calculating the profit
    profit = total_sales - total_labor

    #list where all data will be appended 
    lines = []
    #Making the profit repport more presentable with double lines
    lines.append("=" * 40)
    #profit repport with todays date using the imported library
    lines.append(f"Profit Report for {date.today()}")
    #lines again to make the profit repport more presentable
    lines.append("=" * 40)
    #omakase Sold, labor cost and the profit
    lines.append("Omakase sold:")
    for name, quantity in sold.items():
        lines.append(f"  {name}: {quantity}")
    lines.append(f"Total sales:       ${total_sales:,.2f}")
    lines.append(f"Total labor cost:  ${total_labor:,.2f}")
    lines.append(f"Profit:            ${profit:,.2f}")

    #display the results
    if profit > 0:
        lines.append("Good news: the restaurant made money today.")
    elif profit < 0:
        lines.append("Heads up: the restaurant lost money today.")
    #In case that the numbers are even a else result display that the restaurant is even today
    else:
        lines.append("The restaurant broke even today.")

    return "\n".join(lines)


#Save the repport to REPPORT_FILE and making it presentable
def save_report(report):
    with open(REPORT_FILE, "a") as file:
        file.write(report + "\n\n")
    print(f"\nReport saved to {REPORT_FILE}")


#main fuction of the program 
def main():
    print("Zuma Shift Profit Report")
    sold = record_sales()
    hours_worked = record_hours()
    report = build_report(sold, hours_worked)
    print("\n" + report)
    save_report(report)


#call the program with main()
main()
    
def get_hours(message):
    while True:
        answer = input(message)
        hours = float(answer)
        if hours >= 0:
            return hours
        print("Hours can't be negative.")