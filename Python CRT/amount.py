amount=int(input("enter the Amount:"))
notes=amount//2000
print("No of 2000 Notes",notes)
amount=amount%2000
notes=amount//500
print("No of 500 Notes :",notes)
amount=amount%500
notes=amount//200
print("No of 200 Notes :",notes)
amount=amount%200
notes=amount//100
print("No of 100 Notes :",notes)
amount=amount%100
notes=amount//50
print("No of 50 Notes :",notes)
amount=amount%50
notes=amount//20
print("No of 20 Notes :",notes)
amount=amount%20
notes=amount//10
print("No of 10 Notes :",notes)
amount=amount%10
notes=amount//5
print("No of 5 rupee coins :",notes)
amount=amount%5
notes=amount//2
print("No of 2 rupee coins :",notes)
amount=amount%2
notes=amount//1
print("No of 1 rupee coin :",notes)