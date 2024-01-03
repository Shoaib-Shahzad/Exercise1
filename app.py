"""
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
"""

salary = int(input("Enter your salary : "))
years_company = int(input("How many years in company ? "))

if years_company > 5:
    bonus = 0.05 * salary
    print("Amount of net bonus : ", bonus)
else:
    print("No Amount of net bonus for you : ")
