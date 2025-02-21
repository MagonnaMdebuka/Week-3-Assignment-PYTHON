def calc_discount(price,discount_perc):
    if discount_perc >= 20:
        discount_amount = price * (discount_perc / 100)
        final_price = price - discount_amount
        return final_price
    else : 
        return price



price = float(input("Enter the amount : R "))
discount_perc = float(input("Enter the discount  : "))

final_price = calc_discount(price,discount_perc)
print(f"The final price is {final_price}")
discount_amount = price - final_price
print(f"The total discount is {discount_amount}")

