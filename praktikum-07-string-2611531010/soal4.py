# Name: <Humaira Zahratul 'Aini>
# NIM: <2611531010>
# Question 4

phone = "082611531010"
masked = phone[:4] + "*" * len (phone[4:-3]) + phone [-3:]
print(masked)