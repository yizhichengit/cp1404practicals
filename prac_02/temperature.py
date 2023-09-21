def main() :
 Menu = """C - Convert Celsius to Fahrenheit
 F - Convert Fahrenheit to Celsius
 Q - Quit"""
 print(Menu)
 choice = input(">>> ").upper()
 while choice != "Q":
     if choice == "C":
         fahrenheit=c_to_f()
         print(f"Result: {fahrenheit:.2f} F")
     elif choice == "F":
         celsius = f_to_c()
         print(f"Rsult: {celsius:.2f} F")
     else:
         print("Invalid option")
         print(Menu)
         choice = input(">>> ").upper()
     print("Thank you.")
def c_to_f() :
    celsius1 = float(input("Celsius: "))
    fahrenheit1 = celsius1 * 9.0 / 5 + 32
    return (fahrenheit1)

def f_to_c() :
    f = float(input("fahrenheit: "))
    c =  5 / 9 * (f - 32)
    return (c)

if __name__ == "__main__":
    main()