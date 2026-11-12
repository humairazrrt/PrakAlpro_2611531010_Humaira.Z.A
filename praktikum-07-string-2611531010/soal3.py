# Name: <Humaira Zahratul 'Aini>
# NIM: <2611531010>
# Question 3

# A
text = "Informatika"
print(text[11])
print(text.upper)
print(text[0:20])

# B
text = "Humaira Zahratul 'Aini"
count = 0
for char in text:
    if char in "aiueo":
        count += 1
print("Vowels:", count)