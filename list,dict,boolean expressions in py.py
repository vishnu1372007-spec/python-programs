Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
b=2.6
c=3+5j
print(type(a))
<class 'int'>
print(type(b))
<class 'float'>
print(type(c))
<class 'complex'>
>>> #list
>>> list=[1,2,3,"hello",4.8]
>>> print(list)
[1, 2, 3, 'hello', 4.8]
>>> print(list[3])
hello
>>> 
>>> list[2]="python"
>>> print(list)
[1, 2, 'python', 'hello', 4.8]
>>> 
>>> #tuple
>>> tuple=("girls","boys","students")
>>> print(tuple)
('girls', 'boys', 'students')
>>> 
>>> #dictionary(dict)
>>> dict={1:"hello",2:"python",3:"programming"}
>>> print(dict)
{1: 'hello', 2: 'python', 3: 'programming'}
>>> 
>>> #set
>>> set=([1,2,3,4])
>>> print(set)
[1, 2, 3, 4]
>>> 
>>> #boolean expressions
>>> a=10
>>> print(bool(a))
True
>>> b=10.4
>>> print(bool(b))
True
>>> c="python"
>>> print(bool(c))
True
>>> d=[]
>>> print(bool(d))
False
>>> print(bool([]))
False
