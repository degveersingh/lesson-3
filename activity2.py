amount=input("please enter amount for withdrawel")
amount=int(amount)
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notes of 100 rupees",note1)
print("notes of 50 ruppes",note2)
print("notes of 10 rupees",note3)