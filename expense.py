import pandas

df = pandas.read_csv('expenses.csv')
df = df.reset_index()
tot = 0
for index, row in df.iterrows():
    # print(row['id'], row['name'], row['price'])
    tot += row['price']

add_prices = [350000, 83160]
for p in add_prices:
    tot += p
accomodation = 4477922
print(f'tot expense: {tot}')
print(f'tot accom: {accomodation}')
print(f'expense + accom: {tot+accomodation}')
print(f'available fund: {10000000-tot-accomodation}')
