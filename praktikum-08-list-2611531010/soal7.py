menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for d in range(number_of_days):
    row = []
    for m in menus:
        row.append(int(input(f"Day {d + 1}, {m}: ")))
    sales.append(row)

print("Total per day:")
for d in range(number_of_days):
    day_total = 0
    for value in sales[d]:
        day_total += value
    print(f"Day {d + 1}: {day_total}")

menu_totals = []
for c in range(len(menus)):
    col_total = 0
    for r in range(number_of_days):
        col_total += sales[r][c]
    menu_totals.append((menus[c], col_total))
print("Total per menu:", menu_totals)

best_name, best_total = menu_totals[0]
for name, total in menu_totals:
    if total > best_total:
        best_name, best_total = name, total
print(f"Best seller: {best_name} ({best_total})")