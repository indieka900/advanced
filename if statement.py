#name = 'joseph ali'
#print(name.capitalize())
#last_name = name[7:10]
#reversed_name = name[::2]
#print(first_name)
#print(reversed_name)
#website = "http://youtube.com"
#slice = slice(3,-4)
#print(name[slice])
'''
age = int(input("Enter your old"))
if age>= 20:
    years=int(input("You are an adult"))
    if years>=100:
        print('You are older than expected '+ str(years)+' are many')
elif age<=0:
    print("Still in a womb")
else:
    print('you are still a child')
'''
def currancy(Ksh):
    dollars = Ksh / 102.2
    Euros = Ksh / 116.3
    Ush = Ksh / 0.55
    Tsh = Ksh / 0.2
    print('In dollars is {:.2f} in Euros is  {:.2f} in Ugandan shilling is {:.2f} in Tanzanian shilling is {:.2f}'.format(dollars,Euros,Ush,Tsh))
#currancy(200)
#currancy(1872)
ksh = int(input("Enter the Ksh to convert: "))
choice = int(input('\n1. dollars\n2. Tanzania\n3. GBP\n4. Rand\n5. Yen\nChange into: '))
usd=ksh/155
tz=40.75*ksh
gbp=ksh/140.75
rand=ksh/7.75
yen=ksh/75
if choice == 1:
    print('{:.2f}'.format(usd))
elif choice == 2:
    print('{:.2f}'.format(tz))
elif choice == 3:
    print('{:.2f}'.format(gbp))
elif choice == 4:
    print('{:.2f}'.format(rand))
elif choice == 5:
    print('{:.2f}'.format(yen))
else:
    print("Invalid input!!")

#print('In dollars is {:.2f} in TZ is  {:.2f} in GBP is {:.2f} in RAND is {:.2f} in Yen is {:.2f}'.format(usd,tz,gbp,rand,yen))