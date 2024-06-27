Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao1 = {'color':'green','dis':100}
tao.color(tao1['color'])
def rect(tao_oject,tdict):
    for i in range(4):
        tao_object.forward(tdict['dis']
        tao_object..left(90)
                           
SyntaxError: '(' was never closed
def rect(tao_oject,tdict):
    for i in range(4):
        tao_object.forward(tdict['dis'])
        tao_object..left(90)
        
SyntaxError: invalid syntax
def rect(tao_oject,tdict):
    for i in range(4):
        tao_object.forward(tdict['dis'])
        tao_object.left(90)

        
rect(tao,tao1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    rect(tao,tao1)
  File "<pyshell#14>", line 3, in rect
    tao_object.forward(tdict['dis'])
NameError: name 'tao_object' is not defined. Did you mean: 'tao_oject'?
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def rect(tao_object,tdict):
...     for i in range(4):
...         tao_object.forward(tdict['dis'])
...         tao_object.left(90)
... 
...         
>>> rect(tao,tao1)
>>> tao2 = turtle.Pen()
>>> tao2dict = {'color':'green','dis':50}
>>> tao2.color(tao2dict['color'])
>>> rect(tao2,tao2dict)
>>> tao2dict = {'color':'red','dis':50}
>>> tao2.color(tao2dict['color'])
>>> rect(tao2,tao2dict)

>>> 
>>> 
>>> 
>>> rect(tao2,tao2dict)
