'''
my_dict={1:'Akash',2:'Kailesh',3:'arvind',4:'Rahul'}
print(my_dict)
print(my_dict[3])
print(my_dict.get(4))
print(my_dict.get(78))
'''
#ITRATE ONLY ON KEYS USING FOR LOOP
'''
my_dict={1:'akash',2:'Arvind',3:'Kailesh',4:'Sneha'}
for x in my_dict:
    print(x)
'''
'''

student={1:'computer science',2:'mechanical',3:'civil',4:'auto mobile'}
print(student)
# only acces a key from the dict
for x in student:
    print(x)
'''
'''
my_dict={1:'Akash',2:'Arvind',3:'Kailesh',4:'sneha'}
print(my_dict.keys())
for data in my_dict.keys():
    print(data)
'''
'''
my_dict={1:'Akash',2:'Arvind',3:'Kailesh',4:'sneha'}
for x in my_dict:
    print("Key is",x,"And their value is",my_dict[x])
'''
'''
my_dict={1:'Akash',2:'Arvind',3:'Kailesh',4:'muskan'}
print(my_dict.items())
for x in my_dict.items():
    print(my_dict.keys())
'''
'''


student={1:'Akash',2:'Arvind',3:'Kailesh',4:'muskan'}
for key,value in student.items():
    print("key is",key,"And vaue is",value)
    #print('Akash'+'Kailesh')
'''
student_data={1:'Akash',2:'Arvind',3:'himanshu'}
for data in student_data.values():
    print(data)