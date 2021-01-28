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

PeachNum = 5
x= 0
while PeachNum:
    PeachNum += 1
    x = PeachNum
    for n in range(5):
        if (x - 1) % 5 != 0 or x-1 <= 4:
            break
        x = 4 * (x - 1) / 5
    else:
        print(PeachNum)
        break




