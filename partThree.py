def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    for i in d:
        if i == "£":
             new = d.replace("£", "")
    return float(new)

def percent_to_float(p):
    return float(p.strip('%'))/100

main()
