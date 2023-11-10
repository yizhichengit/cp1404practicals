#Electricity bill estimator 1.0
def main():
    print(f"Electricity bill estimator")
price_per_kwh= float(input("price per kWh in cents :$"))
daily_use = float(input("daily use in kWh:"))
num_days = float(input("number of billing days :"))
pp = price_per_kwh / 100
Estimated_bill = pp*daily_use*num_days
print(f"Estimated bill: ${Estimated_bill}")

#Electricity bill estimator 2.0
def main_2():
    TARIFF_11 = 0.244618
    TARIFF_31 = 0.136928

    print("\nElectricity bill estimator 2.0")
    tariff = input("Which tariff? 11 or 31: ")

    while tariff not in ["11", "31"]:
        print("Invalid tariff choice. Please choose 11 or 31.")
        tariff = input("Which tariff? 11 or 31: ")

    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))

    if tariff == "11":
        estimated_bill = TARIFF_11 * daily_use * billing_days
    else:
        estimated_bill = TARIFF_31 * daily_use * billing_days

    print(f"Estimated bill: ${estimated_bill:.2f}")

if __name__ == "__main__":
    main()
    main_2()