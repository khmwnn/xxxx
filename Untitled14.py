
# coding: utf-8

# In[57]:


import math
class Rectangle:
    def _init_(self,x1,x2,y1,y2,a,b):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.a=abs(self.x1-self.x2)
        self.b=abs(self.y1-self.y2)
    def width(self):
        self.a=abs(x1-x2)
        return self.a
    def height(self):
        self.b=abs(y1-y2)
        return self.b
    def area(self):
        return self.a*self.b
    def circumference(self):
        return 2*(self.a+self.b)
    def is_valid(x1,x2,y1,y2):
        return abs(x1-x2) != abs(y1-y2) !=0
class Square(Rectangle):
    def mmm(x1,x2,y1,y2):
        return abs(x1-x2)==abs(y1-y2)
if __name__ == '__main__':
    x1=float(input())
    x2=float(input())
    y1=float(input())
    y2=float(input())
    if Rectangle.is_valid(x1,x2,y1,y2):
        rec = Rectangle()
        print('构成矩形')
        print('长为：',rec.width())
        print('宽为：',rec.height())
        print('面积为：',rec.area())
        print('周长为：',rec.circumference())
    elif Square.mmm(x1,x2,y1,y2):
        squ = Square()
        print ('构成正方形')
        print('边长 =长=',squ.width(),'=宽=',squ.height())
        print('面积为：',squ.area())
        print('周长为：',squ.circumference())
    else :
        print('无法构成矩形或正方形')
    

