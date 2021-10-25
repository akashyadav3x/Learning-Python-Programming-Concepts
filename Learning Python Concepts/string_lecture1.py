my_string='Akash Yadav'
#print(my_string)
#print(my_string[0])
#print(my_string[-1])
#print(my_string[0:12])
#print(my_string[:])
#print(my_string[1])
#print(my_string[2])
#print(my_string[34])

#USING WHILE LOOP
'''
my_string="pal";
i=0
print(len(my_string))
while len(my_string)>i:
    print(my_string)
    i=i+1
'''
#using for loop
'''
my_string='Muskan'
for characters in my_string:
    print((characters))
    #print(my_string)

'''
# PRINT THE STRING IN REVERSE ORDER
'''
my_string='Muskan'
i=-1
while -len(my_string)>=-i:
    print(my_string[-i])
    i=i+1
'''
'''
my_string='Sneha'
i=len(my_string)
while len(my_string)>=i:
    print(i)
    i=i-1
'''
'''
my_string='Sneha'
for x in range(len(my_string)-1,-1,-1):
    print(my_string(x))
'''
'''
print(my_string)
print('Yadav' in my_string)#searching
#print('Akash' is 'Akash')
a='Akash'
b='Yadav'
#print(a is b)
print(a>b)
'''

'''
name='Akash'
age=20
print("my name is",name,"my age is",age)
print("my name is "+name+" my age is "+''+str(age))
print("my name is {0} and my age is {1}".format(name,(age)))
print("my name is %s and my age is %d"%(name,age))
print(f"my name is {name} and my age is {age}")
'''
'''
import math
a,b=10,5
print(f"factorial of {a} is {math.factorial(a)}\nvalue of {b} is {b}")
print(f"max is {a} and {b} is {a,b}")
'''
'''
vowels=['a','e','i','o','u']
ch='a'
print(f"{ch} is accouring in {vowels} {vowels.count(ch)} times")
'''
'''

my_string='muski'
my_string1="K".join(my_string)
print(my_string1)
'''
a='akash'
ans='a'.count(a)
print(ans)