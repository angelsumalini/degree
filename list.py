Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> students='jhon,mary,steve'
>>> students=['jhon','mary','steve']
>>> type(students)
<class 'list'>
>>> len(students)
3
>>> students[0]
'jhon'
>>> students[2]
'steve'
>>> students[-1]
'steve'
>>> students[:2]
['jhon', 'mary']
>>> months=('january','february','march')
>>> type(months)
<class 'tuple'>
>>> months[0]
'january'
>>> students
['jhon', 'mary', 'steve']
>>> students[0]
'jhon'
>>> students[0]='george'
>>> stdents
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    stdents
NameError: name 'stdents' is not defined
>>> students
['george', 'mary', 'steve']
>>> students.append('kate')
>>> students
['george', 'mary', 'steve', 'kate']
>>> students.insert(0,'peter')
>>> students
['peter', 'george', 'mary', 'steve', 'kate']
>>> students.pop()
'kate'
>>> students
['peter', 'george', 'mary', 'steve']
>>> students.pop(1)
'george'
>>> students
['peter', 'mary', 'steve']
>>> students.remove('mary')
>>> students
['peter', 'steve']
>>> students2=['paul','jhon']
>>> students1+students2
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    students1+students2
NameError: name 'students1' is not defined
>>> students2+students
['paul', 'jhon', 'peter', 'steve']
>>> 