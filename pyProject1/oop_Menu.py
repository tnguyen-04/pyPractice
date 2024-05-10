class menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price


food_menu = [
    menu('Fried-rice with seafood', 80000),
    menu('Pizza with sausage', 50000),
    menu('Mixed Pizza', 40000, ),
    menu('Fried chicken wings', 35),
    menu('bread with pork', 18000),
    menu('Sping rolls', 3000),
    menu('Beef Hamburger', 30000),
    menu('Beef steak', 90000),
    menu('Chicago hotdog', 15000),
    menu('Tokoyaki', 25000),
    menu('Ice cream', 8000),
    menu('Sandwich', 32000)
]

beverage_menu = [
    menu('Coke', 12000),
    menu('Pepsi', 14000),
    menu('7-up', 10000),
    menu('Fanta', 12000),
    menu('Cafe', 18000),
    menu('Milk tea', 20000),
    menu('Lemonade', 14000),
    menu('Orange juice', 18000),
    menu('Avocado smoothie', 22000),
    menu('Mineral water', 6000),
    menu('Watermelon juice', 18000)
]

topping_menu = [
    menu('Tapioca pearls', 5000),
    menu('Boba', 5000),
    menu('Raisin', 6000),
    menu('Almond', 7000),
    menu('Sliced peach', 10000),
    menu('Soup', 8000)
]

checkMenu_Customer = input('What kind of menu do you want to check [Food/Beverage/Topping] ?').lower()
ana_checkMenu_Customer = list((menu.strip() for menu in checkMenu_Customer.split(',')))

for check in ana_checkMenu_Customer:
    if check == 'food':
        for display in food_menu:
            print(f'{display.name}: {display.price}đ')
    elif check == 'beverage':
        for display in beverage_menu:
            print(f'{display.name}: {display.price}đ')
    elif check == 'topping':
        for display in topping_menu:
            print(f'{display.name}: {display.price}đ')
    else:
        raise ValueError("Invalid input! Please enter correct menu.")

order_customer = input('Please, order your favorite with name and quantity [name:quantity]!').lower()
analyze_order = list(dish.strip() for dish in order_customer.split(','))
list_menu = (food_menu, topping_menu, beverage_menu)


def calculation_Bill(analyze_order, *list_menu):
    not_found_dish = []
    for orders in analyze_order:
        orders = orders.split(':')
        name_dish = orders[0]
        quantity_dish = int(orders[1])

        dish_price = 0
        found = False
        for check_catergory in list_menu:
            for check_dish in check_catergory:
                if check_dish.name.lower() == name_dish:
                    dish_price += quantity_dish * check_dish.price
                    found = True
                    break
            if found: break
        if not found:
            not_found_dish.append(name_dish)
    if not_found_dish:
        print(f'The following dishes were not found, please check again: {", ".join(not_found_dish)}')

    if dish_price <= 200000:
        discount = 3
    elif dish_price in [500000, 999999]:
        discount = 10
    elif dish_price in [1000000, 2999999]:
        discount = 16
    elif dish_price > 3000000:
        discount = 25
    price_discount = dish_price - (dish_price * discount / 100)
    print(f'You\'ll be discounted {discount}% and have to pay {price_discount:,.0f}đ'.replace(',', '.'))


announce = calculation_Bill(analyze_order, *list_menu)

thank_file = open('thankCustomer.txt', )
print(thank_file.read())
thank_file.close()

# Sping rolls:3, Fried chicken wings:2, Beef Hamburger:2
