print("Subject Codes")
print ("1. ITE 260")
print ("2. ITE 366")
print ("3. GEN 002")
print ("4. NST 021")
print ("5. PED 030")

import calendar
from colorama import Fore, Style
def display_calendar(year, month, highlighted_days):
    cal = calendar.monthcalendar(year, month)
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")
    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end=" ")
            elif day in highlighted_days:
                print(f"{Fore.RED}{day:2}{Style.RESET_ALL}", end=" ")
            else:
                print(f"{day:2}", end=" ")
        print()
highlighted_days = [5, 6, 12, 13, 19, 20]  # Example weekends to highlight

year = 2023
month = 9  # September
display_calendar(year, month, highlighted_days)
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
choice = input("Enter Subject Code Number:")
if choice in ("1", "2", "3", "4", "5", "6", "7", "8"):
    if choice == ('1'):
        print("")
        print("Computer Programming 1")
        print("Destura, Jimuel")
        print("September 4 - October 28 2023")
        print("Tuesday/Friday")
        print("9am/8am - 12pm")
        print("1pm - 4pm")
        print("")
    elif choice == ('2'):
        print("")
        print("Introduction to Computing")
        print("(Including IT Fundamentals)")
        print("Tabon, Jerry")
        print("July 31 - August 29 2023")
        print("Monday/Wednesday/Friday")
        print("8am - 12pm")
        print("1pm - 4pm")
        print("")
    elif choice == ('3'):
        print("")
        print("Understanding The Self")
        print("Degamo, Joy Tiffany")
        print("September 4 - September 30 2023")
        print("Wednesday/Saturday")
        print("9am - 12pm")
        print("1pm - 4pm")
        print("")
    elif choice == ('4'):
        print("")
        print("National Service Training Program 1")
        print("Bolso, Roland N.")
        print("July 31 - October 28 2023")
        print("Monday/Thursday")
        print("4pm - 5:30pm")
        print("")
    elif choice == ('5'):
        print("")
        print("Physical Activities Toward Health and Fitness", "(PATHFit 1)")
        print("Movement Competency Training")
        print("Garcia, Marino")
        print("July 31 - October 28 2023")
        print("Saturday")
        print("7am - 9am")
        print("")


print(calendar.month(yy,mm)) 