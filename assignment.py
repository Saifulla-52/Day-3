N=int(input("Enter number of students:"))
Valid=0
Fail=0
name=input("Enter your name: ")
marks=[0]*N
for i in range(N):
    marks[i]=int(input("Enter marks:"))
for m in marks:
    if m<0 or m>100:
        print(m, "→ Invalid")
    else:
        if len(name)%2==1:
            m+=1
            if m>100:
                m=100
        Valid+=1
        if m>=90:
            print(m, "→ Excellent")
        elif m>=75:
            print(m, "→ Very Good")
        elif m>=60:
            print(m, "→ Good")
        elif m>=40:
            print(m, "→ Average")
        else:
            print(m, "→ Fail")
            Fail+=1
print("Total Valid Students:", Valid)
print("Total Failed Students:", Fail)
