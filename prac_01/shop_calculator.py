
def main():
    num_items = int(input("number of items ："))
    while num_items < 0:
        print("Invalid number of items!")
        num_items = int(input("number of items ："))

    total_price = 0
    for i in range(num_items):
        # 输入每个商品的价格
        item_price = float(input("price of items ："))
        total_price += item_price


    if total_price > 100:
        total_price *= 0.9


    print(f"{num_items}items price are ${total_price:.2f}")

if __name__ == "__main__":
    main()


