n = int(input())
kas = {}

for _ in range(n):
    data = input().split()
    nama = data[0]
    nominal = int(data[1])
    
    if nama in kas:
        kas[nama] += nominal
    else:
        kas[nama] = nominal

total_cash = 0
top_nama = ""
top_nominal = -1

for nama, total in kas.items():
    print(f"{nama}: {total}")
    total_cash += total
    if total > top_nominal:
        top_nominal = total
        top_nama = nama

print(f"Total cash: {total_cash}")
print(f"Top contributor: {top_nama} ({top_nominal})")