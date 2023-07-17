n1 = int(input("Enter the first number in range:"))
n2 = int(input("Enter the last number in range:"))


revx2 = 0
if n1>n2:
    print("First number should be less than the last number...")

for x in range(n1,n2):
    revx = 0
    x2 = x**2
    print(x,x2)
    
    while(x>0):
        a = x % 10
        revx = revx*10 + a
        x = x/10
    print(revx)