Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
3+2
5
3-2
1
3*2
6
3/2
1.5
3//2
1
3%2
1
10/3
3.3333333333333335
10%3
1

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py
3 1

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py
3 1
Traceback (most recent call last):
  File "F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py", line 9, in <module>
    buy_more = row - remaim_tiles
NameError: name 'remaim_tiles' is not defined. Did you mean: 'remain_tiles'?

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py
3 1
มีกระเบื้องทั้งหมมด: 10 แผ่น
1 แถวปูกระเบื้องได้ 3 แผ่น
------คำนวณ------
ต้องปูกระเบื้องทั้งหมด 3 แถว
เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว 1 แผ่น
ลูกค้าต้องซื้อกระเบื้องเพิ่ม 2 แผ่น

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py
27 25
มีกระเบื้องทั้งหมมด: 1456 แผ่น
1 แถวปูกระเบื้องได้ 53 แผ่น
------คำนวณ------
ต้องปูกระเบื้องทั้งหมด 27 แถว
เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว 25 แผ่น
ลูกค้าต้องซื้อกระเบื้องเพิ่ม 28 แผ่น
import math
math.pi
3.141592653589793
math.pi * (3**2)
28.274333882308138
2**2
4
2**3
8

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py
------ โปรแกรมคำนวณกระเบื้อง By CB ------
คุณต้องการปูกระเบื้องทั้งหมมดกี่แผ่น: 10
1 แถวต้องปูกระเบื้องกี่แผ่น: 3
------Calculate------
Traceback (most recent call last):
  File "F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py", line 6, in <module>
    total_row = tiles // row
TypeError: unsupported operand type(s) for //: 'str' and 'str'
a = '10'
b = '3'
a // b
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a // b
TypeError: unsupported operand type(s) for //: 'str' and 'str'
type(a)
<class 'str'>
>>> type(b)
<class 'str'>
>>> int(a)*10
100
>>> a*10
'10101010101010101010'
>>> a/10
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a/10
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> int(a)/3
3.3333333333333335
>>> a=3.5
>>> a*10
35.0
>>> a='3.5'
>>> a*10
'3.53.53.53.53.53.53.53.53.53.5'
>>> float(a)*0.1
0.35000000000000003

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py
------ โปรแกรมคำนวณกระเบื้อง By CB ------
คุณต้องการปูกระเบื้องทั้งหมมดกี่แผ่น: 1890
1 แถวต้องปูกระเบื้องกี่แผ่น: 42
------Calculate------
มีกระเบื้องทั้งหมมด: 1890 แผ่น
1 แถวปูกระเบื้องได้ 42 แผ่น
------คำนวณ------
ต้องปูกระเบื้องทั้งหมด 45 แถว
เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว 0 แผ่น
ลูกค้าต้องซื้อกระเบื้องเพิ่ม 42 แผ่น

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py
------ โปรแกรมคำนวณกระเบื้อง By CB ------
คุณต้องการปูกระเบื้องทั้งหมมดกี่แผ่น: สิบ
กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!
------Calculate------
Traceback (most recent call last):
  File "F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py", line 9, in <module>
    total_row = tiles // row
NameError: name 'tiles' is not defined

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py
------ โปรแกรมคำนวณกระเบื้อง By CB ------
คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น: 15981
1 แถวต้องปูกระเบื้องกี่แผ่น: 54
------Calculate------
มีกระเบื้องทั้งหมมด: 15981 แผ่น
1 แถวปูกระเบื้องได้ 54 แผ่น
------คำนวณ------
ต้องปูกระเบื้องทั้งหมด 295 แถว
เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว 51 แผ่น
ลูกค้าต้องซื้อกระเบื้องเพิ่ม 3 แผ่น

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py
------ โปรแกรมคำนวณกระเบื้อง By CB ------
คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น: สิบ
กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!
คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น: 10
1 แถวต้องปูกระเบื้องกี่แผ่น: 5
------Calculate------
มีกระเบื้องทั้งหมมด: 10 แผ่น
1 แถวปูกระเบื้องได้ 5 แผ่น
------คำนวณ------
ต้องปูกระเบื้องทั้งหมด 2 แถว
เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว 0 แผ่น
ลูกค้าต้องซื้อกระเบื้องเพิ่ม 5 แผ่น
int('สิบ')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int('สิบ')
ValueError: invalid literal for int() with base 10: 'สิบ'
tilecolor = {'red':100,'gold':200,'white':90}
print(tilecolor)
{'red': 100, 'gold': 200, 'white': 90}
print(tilecolor['red'])
100

= RESTART: F:/OneDrive/เดสก์ท็อป/001-Uncle/Python for Everyone/basic-cal1.py
------ โปรแกรมคำนวณกระเบื้อง By CB ------
คุณต้องการปูกระเบื้องทั้งหมดกี่แผ่น: 1587
1 แถวต้องปูกระเบื้องกี่แผ่น: 13
กระเบื้องสีอะไร? [red / gold / white]: red
------Calculate------
มีกระเบื้องทั้งหมมด: 1587 แผ่น
1 แถวปูกระเบื้องได้ 13 แผ่น
------คำนวณ------
ต้องปูกระเบื้องทั้งหมด 122 แถว
เหลือกระเบื้องที่ยังไม่ได้ปูเต็มแถว 1 แผ่น
ลูกค้าต้องซื้อกระเบื้องเพิ่ม 12 แผ่น
ยอดรวมทั้งหมดที่ต้องซื้อกระเบื้องเพิ่ม: 1200 บาท
