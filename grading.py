import time

def sum (cat,ca1t,ca2t,fin):
    total = cat + ca1t +ca2t + fin
    print("Tota marks scored is " +str(total))
cat1 = int(input("Enter cat one marks: "))
if cat1 <= 10:
    cat2 = int(input("Enter cat two marks: "))
    if cat2 <= 10:
        cat3 = int(input("Enter cat three marks: "))
        if cat3 <= 10:
            exam = int(input("Enter finall exam marks: "))
            if exam <= 70:
                sum(cat1,cat2,cat3,exam)
            else:
                print("Invalid marks")
        else:
            print("Invalid marks")
    else:
        print("Invalid marks")
else:
    print("Invalid marks")