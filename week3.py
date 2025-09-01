price = int(input("Enter original price:"))
discount = float(input("Enter discount percentage in decimals:"))

# function to calculate discounted price


def calculate_discount(price, discount):
    discounted_price = price - (price * discount)
    return discounted_price


if discount > 0.2:
    print(f"Price after discount is:{calculate_discount(price, discount)}")
else:
    print(f"Price is:{price}")
