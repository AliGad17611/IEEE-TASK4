n = input()
num = list(map(int,n))
num1= int(n)
c = 0
s1 = s2 = ""
while num1 != 6174:
    num = sorted(num)
    for i in range(0,len(num)):
        s1 = s1 + str(num[i])
        s2 = s2 + str(num[len(num)-i-1])
    num1 = int(s2)-int(s1)
    num = list(map(int, str(num1)))
    c += 1
    s1 = s2 = ""
print(c)

