#vd1
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        area = round(self.width * self.height ,1)
        return area
    def getPerimeter(self):
        Perimeter =round((self.width * self.height) *2,1)
        return Perimeter

#vd2
f = open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt")
st = f.read()
print("noi dung file:")
print(st)
f = open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt","r")
st1 =f.read(15)
print(st1,"--so ky tu la", len(st1))

#vd3
f = open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt")
print(f.readline())
print(f.readline())
f.close()
f = open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt","r")
for x in f:
    print(x)
    f.close()
#vd4
f1 = open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt","w")
st = "welcome"
f1.write(st)
f1.close()
#vd5
f1 = open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt","a+")
st = "this new line"
f1.write(st)
f1.close()
f1 = open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt","r")
print(f.read)

#vd6
f2 = open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt")
print("1.ten file",f2.name)
print("2.che do mo file",f2.mode)
print("3.trang thai dong file",f2.closed)
#vd7
fo =open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt","w")
fo.write("tobe or not tobe")
fo.closed()
print("ghi chu thanh cong")
obj=open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt","w")
obj.write("chao mung")
obj.close()
obj1=open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt","r")
s=obj1.read()
print(s)
obj1.close()
obj2=open("c:\Users\Admin\Documents\oracle bai tap lon\func.txt","r")
s1=obj2.read(20)
print(s1)
obj2.close()
