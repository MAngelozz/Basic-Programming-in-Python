def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today-dob).days / 365.25)
    print("Your Age is: ",age)

#y=year m=month d=day
y=int(input("Enter your Birth Year: "))
m=int(input("Enter your Birth Month(1-12): "))
d=int(input("Enter your Birth Date(1-31): "))
ageCalculator(y, m, d)