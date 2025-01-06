#vd1
def hello_MDC(str):
    print("Hi",str,"how are you")
    print("nice day!")
hello_MDC("MDC")


#vd2
def giai_thua(n):
    tich=1
    for i in range(1,n+1):
        tich=tich*i
        return tich
n = int(input("nhap vao so nguyen n:"))
print(n,"!=",giai_thua(n))

#vd3
n = int(input("nhap vao so nguyen n:"))
print(n,"!=",giai_thua(n))
print("12! =",giai_thua(12))

#vd4
def hello_MDC(str):
    print("Hi",str,"how are you")
    print("nice day!")
hello_MDC("MDC")

def giai_thua(n):
    tich=1
    for i in range(1,n+1):
        tich=tich*i
        return tich

#vd5
def all_ab(a,b):
    add=a+b
    sub=a-b
    multi=a*b
    div=a/b
    return add,sub,multi,div
a =10
b =6
add,sub,multi,div=all_ab(a,b)
print("tong:",add)
print("hieu:",sub)
print("tich:",multi)
print("thuong:",div)

#vd6
def giai_thua(n):
    tich=1
    for i in range(1,n+1):
        tich=tich*i
        return tich
print("12! =",giai_thua(12))
print("12! =",giai_thua())

#vd7
def sum_ab(a=5, b=7):
    total = a+b
    return total
print(sum_ab(8,13))
print(sum_ab())

#vd8
def get_sum(*num):
    tmp=0
    for i in num:
        tmp = tmp+i
    return tmp
result = get_sum(1,2,3,4,5)
print("ketqua",result)

#vd9
x=300
y=800
def myfunc():
    x=200
    total = x +y
    print("(local)x:",x)
    print("total:",total)
myfunc()
print("------")
print("(global)x:",x)

#vd10
x =lambda a : a+10
print(x(5))
print(x(7))
x =lambda a, b :a *b
print(x(5,6))
    