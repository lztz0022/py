import math

def quadratic(a,b,c):
    x1=float((-b+math.sqrt(b*b-4*a*c))/(2*a))
    x2=float((-b-math.sqrt(b*b-4*a*c))/(2*a))
    return x1,x2

a=int(input('%s' %'a='))
b=int(input('%s' %'b='))
c=int(input('c='))
if b**2<4*a*c:
    print('方程：',a,'x^2+',b,'x+',c,'=0无解')
else:
    x1, x2=quadratic(a,b,c)
    print('%s%s%s%s%s%s%s%.1f %.1f' %('方程：',a,'x^2',b,'x',c,'=0的解是：',x1,x2))
