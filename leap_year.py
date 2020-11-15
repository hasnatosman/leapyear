print("I will check leap year in different way")
year = int(input("Input a number: "))
if year % 400 == 0:
    print("Yes")
elif year % 100 == 0:
    print("NO")
elif year % 4 == 0:
    print("Yes")
else:
    print("No")
"""
if year % 4 != 0:
    print("No")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
"""
"""
if year % 100 != 0 and year % 4 == 0:
    print("Yes")
elif year % 100 == 0 and year % 400 == 0:
    print("Yes")
else:
    print("No")
    """