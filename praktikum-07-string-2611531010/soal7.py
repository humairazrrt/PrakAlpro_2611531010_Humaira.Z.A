# Name: <Humaira Zahratul 'Aini>
# NIM: <2611531010>
# Question 7

name = "Humaira Zahratul 'Aini".lower()
nim = "2611531010"

clean = name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name + nim[-3:]

intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)

print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")

print("=" * 30)