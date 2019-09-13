Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> type()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    type()
TypeError: type() takes 1 or 3 arguments
>>> type(8)
<class 'int'>
>>> Type(4)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Type(4)
NameError: name 'Type' is not defined
>>> type(3.4)
<class 'float'>
>>> type(helloe)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    type(helloe)
NameError: name 'helloe' is not defined
>>> type(hello)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    type(hello)
NameError: name 'hello' is not defined
>>> type("hello")
<class 'str'>
>>> type('hello')
<class 'str'>
>>> type('hello2')
<class 'str'>
>>> beep(5., 523)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    beep(5., 523)
NameError: name 'beep' is not defined
>>> type('c')
<class 'str'>
>>> type('')
<class 'str'>
>>> type('bumboclaaute")
     
SyntaxError: EOL while scanning string literal
>>> type('bumboclaaute')
<class 'str'>
>>> 17,000
(17, 0)
>>> type((17,2))
<class 'tuple'>
>>> type('this is a string')
<class 'str'>
>>> type("And so is this")
<class 'str'>
>>> type("""and this""")
<class 'str'>
>>> type('''and even this...''')
<class 'str'>
>>> '"Run" Shouted Jane'
'"Run" Shouted Jane'
>>> print('hello world')
hello world
>>> print('hello',,,,,,'world')
SyntaxError: invalid syntax
>>> print('hello','world')
hello world
>>> print("Nash","Marcus")
Nash Marcus
>>> print("Nash",,"Marcus")
SyntaxError: invalid syntax
>>> print("Nash Marcus")
Nash Marcus
>>> print("NashMarcus")
NashMarcus
>>> print('''"Oh no", she exclaimed, "Ben's bike is broken!"''') 
"Oh no", she exclaimed, "Ben's bike is broken!“
SyntaxError: multiple statements found while compiling a single statement
>>> print('''"Oh no", she exclaimed, "Ben's bike is broken!"''') 
"Oh no",she exclaimed, "Ben's bike is broken!“
SyntaxError: multiple statements found while compiling a single statement
>>> print('"Oh no", she exclaimed, "Ben's bike is broken!"') 
"Oh no", she exclaimed, "Ben's bike is broken!“
      
SyntaxError: invalid syntax
>>> print('''"Oh no", she exclaimed, "Ben's bike is broken!"''')
"Oh no", she exclaimed, "Ben's bike is broken!"
>>> print('"Oh no", she exclaimed, "Ben's bike is broken!"')
      
SyntaxError: invalid syntax
>>> print('"Oh no", she exclaimed, "Ben\'s bike is broken!"')
"Oh no", she exclaimed, "Ben's bike is broken!"
>>> message="""This message will...span several...lines."""
>>> print(message)
This message will...span several...lines.
>>> message="""This message will...span several...lines."""
>>> message="""This message will...span several...lines."""
>>> message="""This message will
...span several
...lines."""
>>> print(meassage)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print(meassage)
NameError: name 'meassage' is not defined
>>> print(message)
This message will
...span several
...lines.
>>> message="""'hello
I "said" do not touch this.
I\d much rather you 'not'."""
>>> print(message)
'hello
I "said" do not touch this.
I\d much rather you 'not'.
>>> 
