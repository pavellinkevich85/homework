def get_price(percent, price):
    return round(price * (1 + percent / 100), 2)

prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_percent = int(input('Первое повышение цен: '))
secon_percent = int(input('Второе повышение цен: '))

price_first = [get_price(first_percent, i_price) for i_price in prices_now]
price_secon = [get_price(secon_percent, i_price) for i_price in price_first]

print(price_secon)
print(price_first)

