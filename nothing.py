class A ():
    def fun_1 (self) :
        print('hi')
class B (A) :
    def fun_2 (self) :
        print('B')
class C (B) :
    pass    
c=C()
c.fun_1()