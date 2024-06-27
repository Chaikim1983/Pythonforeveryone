Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'Somsak'
age = 12
age == 12
True
if age == 12:
    print('สามารถเรียนห้อง ป.5')

    
สามารถเรียนห้อง ป.5
if age !=12:
    print('ต้องไปเรียนห้องอื่น')

    
age !=12
False
age = 15
if age !=12:
    print('ต้องไปเรียนห้องอื่น')

    
ต้องไปเรียนห้องอื่น
age = 18
if age  12:
    
SyntaxError: invalid syntax
if age > 12:
    print('คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง')

    
คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง
 age = 12
 
SyntaxError: unexpected indent
age = 12
if age > 12:
    if age > 12:
        print('คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง')

        

if age > 12:
    if age >= 12:
        print('ห้องนี้รับอายุ 12 ขวบขึ้นไป')

        


if age >= 12:
    print('ห้องนี้รับอายุ 12 ขวบขึ้นไป')

    
ห้องนี้รับอายุ 12 ขวบขึ้นไป
age = 7
if age < 12:
    print('ต้องเรียน ป.4 ลงไปเท่านั้น')

    
ต้องเรียน ป.4 ลงไปเท่านั้น
age = 12if age = 12:
    
SyntaxError: expected 'else' after 'if' expression
age = 12if age = 12:
    
SyntaxError: expected 'else' after 'if' expression
age = 12
if age <= 12:
    if age < 12:
        print('อายุ 12 ลงไปสามารถขึ้นรถไปไฟ้าฟรี')

        


    if age < 12:
        print('อายุ 12 ลงไปสามารถขึ้นรถไปไฟ้าฟรี')
        
SyntaxError: unexpected indent
if age < 12:
    print('อายุ 12 ลงไปสามารถขึ้นรถไปไฟ้าฟรี')

    

if age < 12:
    print('อายุ 12 ลงไปสามารถขึ้นรถไปไฟ้าฟรี')if age <= 12:
        if age < 12:
            print('อายุ 12 ลงไปสามารถขึ้นรถไปไฟ้าฟรี')
            
SyntaxError: invalid syntax

if age <= 12:
    if age < 12:
        print('อายุ 12 ลงไปสามารถขึ้นรถไปไฟ้าฟรี')

        
if age <= 12:
    if age < 12:
        print('อายุ 12 ลงไปสามารถขึ้นรถไปไฟ้าฟรี')

        
age = 12
.
if age <= 12:
    print('อายุ 12 ลงไปสามารถขึ้นรถไปไฟ้าฟรี')

    
อายุ 12 ลงไปสามารถขึ้นรถไปไฟ้าฟรี
garage = ['toyota','isuzu','benz']
car = 'toyota'
car in garage
True
if car in garage
SyntaxError: expected ':'
if car in garage:
    print('รถคันนี้อยู่ในโรงรถลุง')

    
รถคันนี้อยู่ในโรงรถลุง
car = 'bmw'
if car in garage:
    print('รถคันนี้อยู่ในโรงรถลุง')

    
student = True
check = False
mobile = {'loong':'0801234455','somsak':'081111'}

'loong' in mobile
True
listcheck = mobile.values()
print(listcheck)
dict_values(['0801234455', '081111'])
'0801234455' in listcheck
True
>>> 'Audi' == 'audi'
False
>>> 'Audi'.lower() == 'audi'
True
>>> True and True
True
>>> True and False
False
>>> True or False
True
>>> True or True
True
>>> money = 200
>>> style = 'japanese'
>>> if money = 200 and style == 'japanese':
...     
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> if money >= 200 and style == 'japanese':
...     print('คุณสามารถเข้าร้านได้จ้าา')
... 
...     
คุณสามารถเข้าร้านได้จ้าา
>>> stylecheck = ['japanese','thai','chinese']
>>> if money >= 200 and style in stylecheck:
...     print('คุณสามารถเข้าร้านได้จ้าา')
... 
...     
คุณสามารถเข้าร้านได้จ้าา
>>> def checkstyle(style,money):
...     stylecheck = ['japanese','thai','chinese']
...     if money >= 200 and style in stylecheck:
...         print('คุณสามารถเข้าร้านได้จ้าา')
...     elif style not in stylecheck and money >= 300:
...         print('คุณต้องซื้อชุดของเราในราคา 100 บาทถึงจะเข้าได้')
...     else:
...         print('ขออภัยค่ะ ทางเราไม่สามารถให้เข้าได้')
... 
...         
>>> checkstyle('japanese',400)
คุณสามารถเข้าร้านได้จ้าา
>>> checkstyle('thai',100)
ขออภัยค่ะ ทางเราไม่สามารถให้เข้าได้
>>> checkstyle('western',600)
คุณต้องซื้อชุดของเราในราคา 100 บาทถึงจะเข้าได้
