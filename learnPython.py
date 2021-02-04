# 1
# num = float(input('Enter amount:'))
# inrate = float(input('Enter inrate:'))
# period = int(input('Enter period:'))
# value = 0
# year = 1
# while year <= period:
#    value = num * (1 + inrate)
#    print('Year {} Rs. {:.2f}'.format(year,value))
#    num = value
#    year += 1


# 2 caculate average of ints
# n = 10
#list = []
#i = 0
#print('Please enter 10 numbers:')
#while i < n:
#    list.append(int(input()))
#    i += 1
#print(list)

# 3 F to C
# fahrenheit = 0
# print('Fahrenheit Celsius')
# while fahrenheit <= 250:
#    celsius = (fahrenheit - 32) / 1.8
#    print('{:5d} {:10.2f}'.format(fahrenheit, celsius))
#    fahrenheit += 25

# 5 monkey

#PeachNum = 5
#x= 0
#while PeachNum:
#    PeachNum += 1
#    x = PeachNum
#    for n in range(5):
#        if (x - 1) % 5 != 0 or x-1 <= 4:
#            break
#        x = 4 * (x - 1) / 5
#    else:
#        print(PeachNum)
#        break

## 数列计算
#print('数列计算')
#sum = 0
#for i in range(1,11):
#    sum += 1.0 / i
#    print('{:2d} {:6.4f}'.format(i,sum))


# 二次方程求解
#import math
#a = int(input('enter value of a: '))
#b = int(input('enter value of b: '))
#c = int(input('enter value of c: '))
#d = b * b - 4 * a * c
#if d < 0:
#    print('roots are imaginary')
#else:
#    root1 = (-b + math.sqrt(d)) / (2 * a)
#    root2 = (-b - math.sqrt(d)) / (2 * a)
#    print('root 1 = ', root1)
#    print('root 2 = ', root2)

## salesmansalary

#basic_salary = 1500
#bonus_rate = 200
#commission_rate = 0.02
#numberofsale = int(input('enter the number of cameras sold: '))
#price = float(input('enter the price of the cameras: '))
#bonus = bonus_rate * numberofsale
#commission = commission_rate * price * numberofsale
#print('bonus             = {:6.2f}'.format(bonus))
#print('commission        = {:6.2f}'.format(commission))
#print('Gross salary      = {:6.2f}'.format(basic_salary + bonus + commission))


# circleArea
#import math
#d = float(input('enter the diameter of the circle: '))
#area = math.pi * d * d / 4
#print('the area is: {:.10f}'.format(area))

# multiplication

#i = 1
#print('-' * 60)
#while i < 11:
#    n = 1
#    while n <= 10:
#        print('{:5d}'.format(i * n),end=' ')
#        n += 1
#    print()
#    i += 1
#print('-' * 60)

##some print test
#row = int(input('Enter the number of rows: '))
#n = row
#while n >=0:
#    x = '*' * n
#    y  = ' ' * (row - n)
#    print(y + x)
#    n -= 1

## for语句的使用，for语句历遍数列/字符串
#a = [1, 4, 9, 16, 25, 36]
#for x in a[1::2]:
#    print(x)

## 判断学生成绩是否达标
#n = int(input("Enter the number of students: "))
#data = {}
#Subjects = ('Physics', 'Maths', 'History')
## 完成初始变量定义
#for i in range(n):
#    name = input('Enter the name of the student {}: '.format(i + 1))
#    marks = []
#    for x in Subjects:
#        marks.append(int(input('Enter the marks of {}: '.format(x))))
#    data[name] = marks
#for x, y in data.items():
#    total = sum(y)
#    print("{}'s total marks is {:4d}".format(x, total),end= ' ')
#    if total < 120:
#        print("fail")
#    else:
#        print("pass")

##n*n矩阵的hadamard乘积
n = int(input('Enter the value of n: '))
print("Enter the value of Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter the value of Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j]*b[i][j] for j in range(n)])
print("After Matrix multiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)


