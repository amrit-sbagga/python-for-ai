temperature = 10

if(temperature > 30):
    print("It's hot outside")
elif temperature > 20:
    print("It's warm outside")
else:
    print("It's cold outside")



age = 25
has_license = True
has_ticket = True

if has_ticket:
    if age >= 18 and has_license:
        print("You can drive")
    elif age < 18:
        print("You are too young")
    else:
        print("You don't have a license")   