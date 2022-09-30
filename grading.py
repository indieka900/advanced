import time

def sum (cat,ca1t,ca2t,fin):
    total = cat + ca1t +ca2t + fin
    print("\nTotal marks scored is " +str(total))
    time.sleep(1)
    print("\nYour grade is: ",end='')
    if total <= 100 and total >=70:
        print("A")
    elif total < 70 and total >=60:
        print("B")
    elif total < 60 and total >=50:
        print("C")
    elif total <= 50 and total >=40:
        print("D")
    else:
        print("E")

cat1 = int(input("Enter cat one marks: "))
if cat1 <= 10:
    cat2 = int(input("Enter cat two marks: "))
    if cat2 <= 10:
        cat3 = int(input("Enter cat three marks: "))
        if cat3 <= 10:
            exam = int(input("Enter finall exam marks: "))
            if exam <= 70:
                time.sleep(1)
                sum(cat1,cat2,cat3,exam)
            else:
                print("Invalid marks")
        else:
            print("Invalid marks")
    else:
        print("Invalid marks")
else:
    print("Invalid marks")