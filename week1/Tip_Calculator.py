def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    no_sign = d.replace("$", "")
    return float(no_sign)

def percent_to_float(p):
    no_perc = p.replace("%", "")
    no_perc_float = float(no_perc)
    return no_perc_float / 100


main()