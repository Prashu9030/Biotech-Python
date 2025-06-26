sum_odd=0
sum_even=0
total=0
card_number=input("Enter the credit card number :")
card_number =card_number.replace("-","")
card_number =card_number.replace(" ","")
card_number =card_number[::-1]

for i in card_number[::2]:
    sum_odd += int(i)

for i in card_number[1::2]:
    x = int(i) * 2
    if x > 9:
        x -= 9
    sum_even += x

total = sum_odd + sum_even

if total % 10 == 0:
    print("Valid credit card ")
else:
    print("Invalid credit card")