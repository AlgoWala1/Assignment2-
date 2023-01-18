s1 = int(input("Enter side length: "))
s2 = int(input("Enter side length: "))
s3 = int(input("Enter side length: "))
if s3>s1+s2 and s2> s1+s3 and s1>s2+s3:
    print("Yes")
else:
    print("No")
    
