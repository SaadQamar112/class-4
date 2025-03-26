#input your amount 
amount=int(input("enter your widrawl amount"))

note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
#printing the amount

print(note1)
print(note2)
print (note3)
