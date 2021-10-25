'''
students={'kailesh','arvind','akash','sneha','nikita','rahul'}
print(students)
print(type(students))
students={'kailesh':"java",'arvind':'python','akash':"django",
          'sneha':"java advance",'nikita':"c languge",'rahul':"c++"}
print(students)
print(type(students))
print(id(students))
'''
'''
collage={'SISTec':{'Sistec-R':'Ratibdh'},'LNCT':{'LNCt-R':'MP nager'},
         'Akash':['java','3465','c and c++'],'kailesh':('java SE','123','java EE')}
print(collage['SISTec'])
print(collage.get('Akash'))
print(collage.get('kailesh'))
'''
'''
collage = {'SISTec': {'Sistec-R': 'Ratibdh'}, 'LNCT': {'LNCt-R': 'MP nager'},
           'Akash': ['java', '3465', 'c and c++'], 'kailesh': ('java SE', '123', 'java EE')}
# for keys in collage:
#   print(collage.get('Akash'))
print(collage)
'''
#my_dict={""}
#print(my_dict)
'''
my_dict=dict('')
print(type(my_dict))
my_dict1=dict({1:"Akash",2:"Arvind",3:"Kailesh"})
print(my_dict1)
print(type(my_dict1))
'''
my_dict=dict([(1,'Akash'),(2,'arvind')])
my_dict1=dict({1:'io',2:'ui'})
print(my_dict1)
print(my_dict)
print(type(my_dict))