# Name: <Humaira Zahratul 'Aini>
# NIM: <2611531010>
# Question 6

full_name = "Humaira Zahratul 'Aini"
nim = "2611531010"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
username = first_name.lower() + nim[-3:]
print(username)