print("Введите номер билета (шестизначное число)")
n= int(input())
n1 = n
a = n//100000
n1 = n1//10
e = n1%10
n1 = n1//10
d = n1%10
n1 = n1//10
c = n1%10
n1 = n1//10
b = n1%10
f = n%10 
if(a+b+c == d+e+f):
    print("Билет является счастливым")
else:
    print("Билет не является счастливым")