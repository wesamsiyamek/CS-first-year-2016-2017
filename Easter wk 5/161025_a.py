Python 3.4.4 |Anaconda 2.3.0 (x86_64)| (default, Jan  9 2016, 17:30:09) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> x = 12
>>> print(x)
12
>>> x = "bob"
>>> print(x)
bob
>>> 
>>> 
>>> 19 % 4 # % remainder
3
>>> 21 % 5
1
>>> 19 // 4 # quoitent
4
>>> 19 / 4
4.75
>>> # Changed from Python 2
... 
>>> 
>>> a = "bob"
>>> a % 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not all arguments converted during string formatting
>>> 
>>> 
>>> y = 2016
>>> a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32
>>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 
>>> 
>>> print(n)
3
>>> print(p)
27
>>> 8 * b + 13 // 25
160
>>> (8 * b + 13) // 25
6
>>> y = 2010
>>> 
>>> a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32
>>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> >>> 
>>> n
4
>>> p
4
>>> 