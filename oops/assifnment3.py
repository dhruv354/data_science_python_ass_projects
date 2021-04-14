class Super():
    
    def fun1(self):
        print('This is function1 inside the Super class')
    
class Modified_Super(Super):
    
    def fun1(self):
        print('This is function1 in Modified Super Class')

    def fun2(self):
        print('This is  2nd function  in Modified Super Class')
        

obj1 = Modified_Super()
obj1.fun1()
