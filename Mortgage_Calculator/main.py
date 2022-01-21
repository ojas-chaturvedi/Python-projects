#!/usr/bin/env python3

import os
import terminaltables

os.system("clear")

Months_Of_The_Year = ["Jan", "Feb", "Mar", "Apr", "May",
                      "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]


class Functions:
    def calc_payment(self, P, r, n):
        M = (P * (r * (1 + r) ** n)) / (((1 + r) ** n) - 1)
        print("Your monthly payments are {:0.2f} dollars.".format(M))
        return M

    def calc_interest(self, balance, interest_rate):
        return balance * interest_rate

    def calc_bal_r(self, pb, principal):
        return pb-principal

    def calc_int_p(self, pti, i):
        return pti + i

    def calc_principal(self, MP, MI, M, Y, E1, E2, E2M, E3, E3M, E3Y):
        if Y == E3Y:
            if M == E3M:
                if M == E2M:
                    return MP-MI+E1+E2+E3
                else:
                    return MP-MI+E1+E3
        if M == E2M:
            return MP-MI+E1+E2
        else:
            return MP-MI+E1


class Extras:
    def __init__(self):
        self.Monthly_Extra = 0
        self.Annually_Extra = 0
        self.Annually_Extra_Month = None
        self.OneTime = 0
        self.OneTime_Month = None
        self.OneTime_Year = None
        self.Choice = True

    def main(self):
        extra_c = input(
            "\nDo you want to add any extra payments (y or n): ").lower()
        if extra_c == "n":
            pass
        elif extra_c == "y":
            print("\nDo you want to add any extra payments??")
            self.Choice = int(input("Options: \n1 = Add money to your monthly mortgage payment \n2 = Add money as an extra yearly mortgage payment occurring in every month of your choice \n3 = Add money as a one time mortgage payment in month and year of your choice \nChoose one: "))
            if self.Choice == 1:
                self.Extra_Monthly()
            elif self.Choice == 2:
                self.Extra_Annually()
            elif self.Choice == 3:
                self.One_Time()
            else:
                print("Please input a number from 1-3 as your choice. Try again.")
                self.main()
        else:
            print("Answer choice not y or n. Please try again.")
            self.main()

    def Extra_Monthly(self):
        self.Monthly_Extra = input(
            "Enter amount of money that you can add per month to your normal monthly payment: ")
        print("Perfect. Every month, you will make an extra payment of {:0.2f} dollars.".format(
            self.Monthly_Extra))
        self.main()

    def Extra_Annually(self):
        self.Annually_Extra_Month = int(input(
            "Which month do you want to make an extra payment every year? \nType the month number: "))
        if self.Annually_Extra_Month <= 12:
            self.Annually_Extra = float(input("Add amount on moneY: "))
            print("Perfect. Every year in",
                  Months_Of_The_Year[self.Annually_Extra_Month - 1], ", you will make an extra payment of", Extra2, "dollars.")
            self.main()
        else:
            print("Make sure that the month number is in the range from 1-12. Try again.")
            self.Extra_Annually()

    def One_Time(self):
        self.OneTime_Year = int(
            input("Which year do you want to make an extra payment? \nType the year: "))
        self.OneTime_Month = int(input(
            "Which month do you want to make an extra payment? \nType the month number: "))
        if self.OneTime_Month <= 12:
            self.OneTime = float(input("Add amount of money: "))
            print("Perfect. In the year", self.OneTime_Year, ", and month",
                  Months_Of_The_Year[self.OneTime_Month - 1], "you will make an extra payment of", self.OneTime, "dollars.")
            self.main()
        else:
            print("Make sure that the month number is in the range from 1-12. Try again.")
            self.One_Time()


class Amortization:
    def __init__(self):
        self.amortization_schedule = [["Month", "Year", "Monthly Payment",
                                       "Interest", "Principal", "Total Interest Paid", "Balance"], ]

    def calc_table(self, Balance_Remaining, Interest_Rate, Total_Interest_Paid, Monthly_Payment, Month, Year, values, extras):
        while Balance_Remaining > 0.1:
            Monthly_Interest = values.calc_interest(
                Balance_Remaining, Interest_Rate)
            Total_Interest_Paid = values.calc_int_p(
                Total_Interest_Paid, Monthly_Interest)
            if Monthly_Payment > Balance_Remaining:
                Monthly_Principal = Balance_Remaining
                Monthly_Payment = Monthly_Principal + Monthly_Interest
            else:
                Monthly_Principal = values.calc_principal(Monthly_Payment, Monthly_Interest, Month, Year, extras.Monthly_Extra,
                                                          extras.Annually_Extra, extras.Annually_Extra_Month, extras.OneTime, extras.OneTime_Month, extras.OneTime_Year)
            Balance_Remaining = values.calc_bal_r(
                Balance_Remaining, Monthly_Principal)
            self.amortization_schedule.append([Months_Of_The_Year[Month - 1], Year, round(Monthly_Payment, 2), round(
                Monthly_Interest, 2), round(Monthly_Principal, 2), round(Total_Interest_Paid, 2), round(Balance_Remaining, 2)])
            if Month >= 12:
                Month = 0
                Year += 1
            Month += 1

    def display_table(self):
        chart = terminaltables.AsciiTable(self.amortization_schedule)
        self.output = int(input(
            "How do you want to view your amortization schedule? \n1 = View in terminal \n2 = Save in a text file for later \n3 = View and save \n4 = Dont view or save \nChoose an option: "))
        if self.output == 4:
            pass
        elif self.output == 1:
            print(chart.table)
        elif self.output == 2:
            self.file_name = input("Enter name of file to be saved: ")
            f = open(self.file_name + ".txt", "w")
            f.write(chart.table)
        elif self.output == 3:
            self.file_name = input("Enter name of file to be saved: ")
            f = open(self.file_name + ".txt", "w")
            f.write(chart.table)
            print(chart.table)
        else:
            print("Invalid option. Try again.")
            self.display_table()


def main():
    values = Functions()
    extras = Extras()

    Mortgage_Amount = float(input("Enter the mortgage amount: "))
    Mortgage_Term = (float(input("Enter the mortgage term in years: "))) * 12
    Interest_Rate = (float(input(
        "Enter the annual interest rate percentage (numbers only): "))) / (12 * 100)

    Month = int(input(
        "Enter the month number between 1 to 12 from when your mortgage will start: "))
    Year = int(input("Enter the year from when your mortgage will start: "))

    Monthly_Payment = values.calc_payment(
        Mortgage_Amount, Interest_Rate, Mortgage_Term)
    Balance_Remaining = Mortgage_Amount
    Total_Interest_Paid = 0

    print("Your monthly payment amount is:",
          round(Monthly_Payment, 2), "dollars")
    print("Your total interest to be paid is",
          round(Total_Interest_Paid, 2), "dollars")
    print("Your estimated payoff date is", Months_Of_The_Year[Month - 2], Year)

    table = Amortization()
    table.calc_table(Balance_Remaining, Interest_Rate, Total_Interest_Paid,
                     Monthly_Payment, Month, Year, values, extras)
    table.display_table()


if __name__ == "__main__":
    main()
