month = input()
day = int(input())

if day < 0:
    print("Invalid")
elif month not in ("January","February","March","April","May","June","July","August","September","October","November","December"):
    print("Invalid")
elif month in ("January","March","May","July","August","October","December") and day > 31:
    print("Invalid")
elif month in ("April","June","September","November") and day > 30:
    print("Invalid")
elif month in ("February") and day > 28:
    print("Invalid")
elif month in("April","May") or (month == "March" and day >=20) or (month == "June" and day <=20):
    print("Spring")
elif month in("July","August")or (month == "June" and day >=21) or (month == "September" and day <=21):
    print("Summer")
elif month in("October, November") or (month == "September" and day >=22) or (month == "Decemeber" and day <=20):
    print("Autumn")
else:
    print("Winter")
