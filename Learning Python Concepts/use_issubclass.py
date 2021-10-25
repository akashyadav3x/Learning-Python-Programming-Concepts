class Baseclass(object):
    pass
class Deriveclass(Baseclass):
    pass
class myclass(Deriveclass):
    pass
class heyclass(myclass):
    pass
print(issubclass(Deriveclass,myclass))
print(issubclass(Baseclass,Deriveclass))
v1=Baseclass
v2=Deriveclass
v3=heyclass
print(isinstance(v3,Deriveclass))
print(isinstance(v2,Baseclass))