Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def hello(friend)
SyntaxError: expected ':'
def hello(friend):
    print('Hi,{}'.format(friend)


hello('John')
          
SyntaxError: '(' was never closed
def hello(friend):
    print('Hi,{}'.format(friend))


hello('John')
SyntaxError: invalid syntax
def hello(friend):
    print('Hi,{}'.format(friend))

    
hello('John')
Hi,John
hello('Robert')
Hi,Robert

def land(width,long):
    cal = width * long
    calwa = cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(width,long(cal))
    
KeyboardInterrupt
def land(width,long):
    cal = width * long
    calwa = cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))

    
land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    land(5,15)
  File "<pyshell#23>", line 6, in land
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
NameError: name 'cal_wa' is not defined. Did you mean: 'calwa'?
def land(width,long):
    cal = width * long
    cal_wa = cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))

    
land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
land(10,80)
ที่ดินผืนนี้กว้าง: 10 เมตร ยาว: 80 เมตร
ที่ดินผืนนี้มีพื้นที่: 800 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 200.0 ตารางวา
res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
print(res)
None
def land(width,long):
    cal = width * long
    cal_wa = cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
    return cal_wa

res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
print(res)
18.75
def land(width,long,price = 999888):
    cal = width * long
    cal_wa = cal/4
    print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
    print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
    return cal_wa * price

res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
print(res)
18747900.0
>>> def land(width,long,price = 999888):
...     cal = width * long
...     cal_wa = cal/4
...     print('ที่ดินผืนนี้กว้าง: {} เมตร ยาว: {} เมตร'.format(width,long))
...     print('ที่ดินผืนนี้มีพื้นที่: {} ตารางเมตร'.format(cal))
...     print('ที่ดินผืนนี้มีพื้นที่: {} ตารางวา'.format(cal_wa))
...     calprice = cal_wa * price
...     return 'ที่ดินผืนนี้ราคา: {:,.2f} บาท'.format(calprice)
... 
>>> res = land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
>>> print(res)
ที่ดินผืนนี้ราคา: 18,747,900.00 บาท
>>> land(5,15)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
'ที่ดินผืนนี้ราคา: 18,747,900.00 บาท'
>>> land(5,15,1000000)
ที่ดินผืนนี้กว้าง: 5 เมตร ยาว: 15 เมตร
ที่ดินผืนนี้มีพื้นที่: 75 ตารางเมตร
ที่ดินผืนนี้มีพื้นที่: 18.75 ตารางวา
'ที่ดินผืนนี้ราคา: 18,750,000.00 บาท'
>>> 1e6
1000000.0
>>> x = Decimal('1000000000')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    x = Decimal('1000000000')
NameError: name 'Decimal' is not defined
>>> '{:.2e}'.format(x)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    '{:.2e}'.format(x)
NameError: name 'x' is not defined
>>> from decimal import Decimal
>>> 1e6
1000000.0
>>> 1e7
10000000.0
>>> x = Decimal('1000000000')
>>> '{:.2e}'.format(x)
'1.00e+9'
