Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello World')
Hello World
>>> print('Hello chock')
Hello chock
>>> 

>>> name = 'chock'
>>> lastname = 'chai'
>>> fullname = name+''+lastname
>>> print(fullname)
chockchai
>>> fullname = name+ ''+lastname
>>> fullname = name+ '' +lastname
>>> print(fullname)
chockchai
>>> fullname = name+''+lastname
>>> fullname = name+' '+lastname
>>> print(fullname)
chock chai
>>> fullname = name+lastname
>>> print(fullname)
chockchai
>>> type(name)
<class 'str'>
>>> age=10
>>> type(age)
<class 'int'>
>>> name.upper()
'CHOCK'
>>> name.lower()
'chock'
>>> name = name.upper()
>>> print(name)
CHOCK
>>> print('ลุงครับผมชื่อ {} นามมสกุล {} อายุ {} ขวบ' .format(name,lastname,age))
ลุงครับผมชื่อ CHOCK นามมสกุล chai อายุ 10 ขวบ
>>> print(f'ลุงครับผมชื่อ {name} นามมสกุล {lastname} อายุ {age} ขวบ')
ลุงครับผมชื่อ CHOCK นามมสกุล chai อายุ 10 ขวบ
