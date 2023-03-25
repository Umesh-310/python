"""
########## Number
a = 5
b = 4

print(5+4)
print(12/3) # return float value only -> 4.0
print(12//3) # return int value only -> 4
print(12/5) # return float value only -> 2.4
print(12//5) # return int value only -> 2
print(12%5) # return reminder only -> 2

########## String

print(str)
print("Don't say bye")
print('hello "you are amazing"')
print('hello\'s')
print("hello\"s")

str = "Aku!"
print('hello Akku')
######### String formeting

print('Hello ' + str)
Aku = f'Hello , {str}'
print(Aku)

str3 = 'Hello, {str}'
print(str3)

st4 = 'how are you {}'

print(st4.format(str))

your_input = input('What is your name: ')
print(f'Hello, {your_input}')
age = int(input('Yore Age : '))
print(f'your Age {age * 2}')

age = 22
print(f'your age is {age}')

int(val)  |
str(val)  | converting function
float(val)|

multipel Assinging

name , age = 'Aku' , 22 # name = 'Aku' , age = 22

a=b=c=1  # a=1,b=1,c=1

name,age = input(Enter your Name and Age).split()

a,b,c = input('enter three number: ').split(',')

print(f'{a} + {b} + {c} = {a+b+c}')

print(input('Enter your Name :- ')[:: -1])


########## string method #################################################

U = 'what you want to count'
len(val)            || length of string
val.lower()         || convert into lowerCase
val.upper()         || convert into upperCase
val.title()         || convert into title ex- (UmEsh sAinI).title() ==> Umesh Saini
val.count('U')      || (Umesh Saini).count('s') ==> 1 # only same output case
val.strip()         || there is more lstrip rstrip

val.replace(' ','', 1-9) || first vale what you want to replace and second which val you gona insert and last one how many you want to replace

val.find('h' , 1) || return index as soon as this find first element and second val start finde aftre the given argument

val.center(len , '*') || length and what you want to put outside


#############################################################################

name, letter = input(
    'Enter your nameand which letter you want to find:- ').split(',')

print(name.lower().count(letter.lower()))

print(('umesh ').center(8 , "%"))

age = 3
age += 3
age -= 3
age *= 2
age /= 2
print(age)


"""
# ////////////////////////////////////////////////////////////////////////////////

"""
CHPTER 2

age = int(input('enter your age:- '))
if age > 14:
    pass # you can pass block
    # print('your Above 14')
else:
    print('less than 14')


# /////////////////////////////////////////////////////////

# == || in python there is no === :(
# and  || there is no & :(
# or || there is no || :(

name,age = input('Enter youre name and age:- ').split()

if name.lower()[0] == 'a' and int(age) > 10:
    print('hehhe :)')
else:
    print(':(')

i=0
while i<10:
    print(f'Hello Aku {i}')
    i += 1

n = int(input('Enter ant number:- '))

i = 1
total = 0
while i<=n:
    total += i
    i += 1
print(total)

n = input('Enter any number:- ')
i = 0
t = 0
while i<len(n):
    t += int(n[i])
    i += 1
print(t)

name = input('Enter your name :- ')
l = len(name)
i = 0
while i < l:
    if name[i] != '#':
        print(f'# {name[i]} : {name.count(name[i])}')
        name = name.replace(name[i], '#')
    i += 1

for i in range(1, 11): # thet said this is clean syntax :(
    print(f'Hello Aku {i}')

n = int(input("Enter number:- "))
t = 0
for i in range(1, n+1):
    t += i
print(t)

n = input('enter any number:- ')

t = 0
for i in range(len(n)):
    t += int(n[i])
print(t)

n = input('enter your name:- ')
ts = ''

for i in range(len(n)):
   if n[i] not in ts:
       print(f'# {n[i]} : {n.count(n[i])}')
       ts += n[i]

import random
for i in range(1,10 ,2):
    print(random.randint(1,10) , i)

for i in "Aditi Pathak":
    print(i)


"""

"""
CHAPTER 3

def add(a,b,c):
    return a+b+c

print(add(2,2,2))

def grater(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c

print(grater(10, 22 , 25))
print(grater(10, 2 , 5))
print(grater(1, 22 , 5))

def sumtwo(a, b):
    return a+b

def sumall(a, b, c, d):
    return sumtwo(a, b) + sumtwo(c, d)

print(sumall(1, 1, 1, 1))

def big(a, b):
    if a > b:
        return a
    return b

def bigger(a,b,c):
    return big(big(a,b),c)

print(bigger(10, 20, 30 ))

def is_palindrome(name):
    return name[::-1] == name

print(is_palindrome('madam'))

list = [1, 2, 3, 4, 'five', 'six', 7.0, None]
print(list)
print(list[1])
print(list[:2])
print(list[::-1])
list[1:] = 'Aditi'
list[2:] = ['Aku' , 'umesh']
print(list)


######### List

list = ['any' , 'aku']
list.append('umesh')
list.insert(2 , 'umesh')
list2 = ['Aditi' , 'moon']
list1 = list + list2
list.extend(list2)
list.index('aku')

list.pop(0) #'this take a index arg also)
del list[1]
list.remove('umesh') #first one

list.count('aku')
list.sort() # this Also work on number work on orignal list for make code use

sorted(list) return new list
list_copy = list.copy()
# list_copy.clear()

diff btw 'is' and == 

is return ture when list is same place in memory and == return ture when both list are equal
user = 'umesh saini'.split() return a list ['umesh' , 'saini']
user = ['umesh' , 'saini']
name = ' '.join(user)

def listSquar(l):
    sqlist  = []
    for i in l:
        sqlist.append(int(i)*int(i))
    return sqlist

list = input('Enter Some number "," sepret:- ').split(',')
print(listSquar(list))

# def reversList(l):
#     tlist = []
#     i = len(l)
#     for i in range(i-1 , -1 , -1 ):
#         tlist.append(l[i])
#     print(tlist)
# def reversList(l):
#     tlist = []
#     lenth = len(l)
#     for i in range(lenth):
#         poped = l.pop()
#         tlist.append(poped)
#     print(tlist)
    
# def reversList(l):
#     tlist = []
    # for i in l:
        # tlist.insert(0 , i)
 
    # return l[::-1]
    # return tlist
        

# print(reversList(input('Enter list :- ').split(',')))


def strrev(l):
    tl = []
    for i in l:
        tl.append(i[::-1])
    print(tl)

strrev(['ukA', 'hsemU'])




def twoList(l):
    odl = []
    evl = []
    for i in l:
        if i % 2 == 0:
            evl.append(i)
        else:
            odl.append(i)
    print([odl, evl])


twoList([1, 2, 3, 4, 5, 6, 7, 8, 9])
# 105


set_one = {1, 2, 7, 3, 9, 4}
print(set_one)
set_two = {0, 6, 3, 5, 6, 2, 1, 7, 3, 6, 8}
print(set_two)

# print(set_one.union(set_two))
print(set_one & set_two)
# print(set_one.intersection(set_two))
print(set_one | set_two)
# print(set_one.difference(set_two))
print(set_one - set_two)

player = {
    'hello': {'name' : 'umesh'},
}
print(player['hello']['name'])

for n in range(1,10):
    for x in range(1,n):
        if n==x:
            print(x , 'x')
            break
    else:
        print(n ,'n')

# num = list(range(1,11))
# print(num)

name = ['Aku', 'Umesh', ':(']
val = [5, 6, 7]

print(dict())
print(zip(['name', 'Aku'] , [ 1, 22]))

add = lambda x,y : x+y
print(add(2,2))

class Person:
    def __init__(self , name , patnerName , cars):
        self.name = name
        self.patnerName = patnerName
        self.cars = cars
    def printName(self):
        print(f'{self.name} is {self.patnerName} patner')
    def __len__(self):
        return len(self.cars)

person1 = Person('Aku','Umesh',[1,2,3,4,5,6])
person2 = Person('Umesh','Aku' , [2,3,4,5,7,1])
person1.printName()
person2.printName()
print(len(person1))

# user = {
#     'name': 'Umesh',
#     'subject': "Mca",
#     'age': 22
# }

# user['add'] = 'mandsour'
# user.pop('age')
# user.popitem()
# print(user)

# def starArg(*args):  # * star in python
#     print(args)

# convert as a tupal

# starArg({
#     'name': 'Umesh'
# }, 1, 2, 3)


# ** kwargs (keyword arguments)

# convert in to Disctiory

# def twoStararg(**kwargs):
#     print(kwargs)


# name = 'Aku'
# age = 22

# twoStararg(name = name, age = age)

# def twoStararg(name, age):
#     print(f'{name} age is {age}')


# me = {'name': 'Aku',
#       'age': 22}

# twoStararg(**me)

# l = [2, 4, 7, 4, 8, 4, 9]
# print(max(l))
# print(min(l))

# names = ['Umesh', 'Saini', 'a','Aku', 'z' ,'Z']

# print(max(names , key= lambda i : len(i)))
# print(min(names, key= lambda i : len(i)))



"""

# std = {
#     'umesh': {'scr': 90, 'age': 21},
#     'Aku': {'scr': 75, 'age': 19},
#     'mohit': {'scr': 76, 'age': 23}
# }

# print(max(std, key=lambda i: std[i]['scr']))
