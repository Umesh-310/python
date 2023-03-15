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


/////////////////////////////////////////////////////////

== || in python there is no === :(
and  || there is no & :(
or || there is no || :(

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


"""

