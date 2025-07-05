
####################################################python easy questions####################################################

"1)"

print("hello world")

'''
hello world  *******
HELLO WORLD
Hello World
error

2)'''
x=5
print(x)

'''55
5 *****
x=5
error

3)'''

x=5
print(x+1)

'''7
6 *****
5+1
error

4)'''

x=5
y=10
print(x*y)

'''10
5
15
50 *****

5)'''

x=5
y=10
print(x+y)

'''15 *****
50
5+10
error

6)'''

x=5
y=10
print x-y 

'''10
syntax error *****
logic error
runtime error


7)'''

a = 7
b = "3"
print(a + b)

'''10
type error *****
7+3
7 + "3"

8)'''

value = int("abc")

'''abc
value error *****
"abc"
value = "abc"

9)'''

name = "Sara"
print(nam)

'''Sara
name error *****
name = "Sara"
nam

10)'''

a=4.5
b=2.0
print(a//b)

'''2.25
2.0 *****   
4
error'''
####################################################python medium questions####################################################

"1)"

bool([])


'''
a) True
b) False
c) []
d) None
✅ Answer: b


2)'''

list("abc")

'''a) ['abc']
b) ('a', 'b', 'c')
c) ['a', 'b', 'c']
d) 'abc'
✅ Answer: c


3)'''

a = [1, 2, 3]
print(a[-1])

'''
a) 1
b) 3
c) -1
d) Error
✅ Answer: b

4)'''

set([1, 2, 2, 3])

'''
a) [1, 2, 3]
b) (1, 2, 3)
c) {1, 2, 3}
d) {1, 2, 2, 3}
✅ Answer: c

5)'''

x = [1, 2, 3]; print(x[3:])

'''a) [3]
b) Error
c) []
d) None
✅ Answer: c

6)'''

strip()

'''a) Removes all whitespace
b) Removes leading/trailing spaces
c) Removes specific characters
d) Splits the string
✅ Answer: b

7)'''

print([i**2 for i in range(3)])

'''a) [0, 1, 2]
b) [1, 2, 3]
c) [0, 1, 4]
d) [1, 4, 9]
✅ Answer: c

8)'''

any([0, "", None, 1])

'''
a) True
b) False
c) None
d) Error
✅ Answer: a

9)'''

'abc'.upper()

'''
a) ABC
b) abc
c) aBc
d) error
✅ Answer: a

10)'''

len(set("hello"))

'''
a) 4
b) 5
c) 1
d) 3
✅ Answer: a
'''

####################################################python hard questions####################################################

"1)"

def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))

'''
a) [1], [2], [3]
b) [1], [1, 2]
c) [1, 2, 3], [1, 2, 3], [1, 2, 3]
d) Error
✅ Answer: b

2)'''

a = {1, 2}
b = {2, 3}
print(a & b)

'''a) {1, 3}
b) {2}
c) {}
d) Error
✅ Answer: b

3)'''

globals()

'''a) Global variables in current module
b) Global constants
c) A string
d) Local scope
✅ Answer: a


4)'''
'''What is a Python decorator?
a) A string wrapper
b) A class modifier
c) A function that modifies another function
d) A GUI tool
✅ Answer: c

5)'''

print(all([]))


'''a) True
b) False
c) None
d) Error
✅ Answer: a

6)'''

'''What is the complexity of searching in a Python set?
a) O(n)
b) O(log n)
c) O(1)
d) O(n log n)
✅ Answer: c


7)'''

[x for x in range(5) if x % 2 == 0]

''' [1, 2, 3, 4]
b) [0, 2, 4]
c) [2, 4]
d) [0, 2]
✅ Answer: b


8)'''

bool('False')


''' True
b) False
c) Error
d) None
✅ Answer: a

9)'''

not (True and False)

'''True
b) False
c) None
d) Error
✅ Answer: a

10)'''
'''What is the default encoding in Python 3?
a) ASCII
b) UTF-16
c) UTF-8
d) ISO-8859-1
✅ Answer: c'''





