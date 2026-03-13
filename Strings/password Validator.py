password = "Abcdef123"

lower = False
upper = False
digit = False

if len(password) > 8 and len(password) < 12:

    for ch in password:
        if ch.islower():
            lower = True
        elif ch.isupper():
            upper = True
        elif ch.isdigit():
            digit = True

    if lower and upper and digit:
        print("Valid Password")
    else:
        print("Invalid Password")

else:
    print("Password length must be between 6 and 12")
