
def main1():
    # Python Program to depict multiple inheritance
    # when method is overridden in both classes
 
    class Class1:
        def m(self):
            print("In Class1") 
        
    class Class2(Class1):
        def m(self):
            print("In Class2")
    
    class Class3(Class1):
        def m(self):
            print("In Class3")  
            
    class Class4(Class2, Class3):
        pass  
        
    obj = Class4()
    print (Class4.mro())
    obj.m()

    #to be noted is 
    #the first class is printed, as no super() is there in for class 2

def main2():
    
    # Python Program to depict multiple inheritance
    # when method is overridden in one of the classes
    
    class Class1:
        def m(self):
            print("In Class1") 
        
    class Class2(Class1):
        pass
    
    class Class3(Class1):
        def m(self):
            print("In Class3")    
        
    class Class4(Class2, Class3):
        pass      
    
    obj = Class4()
    obj.m()

def main3():
    # Python Program to depict multiple inheritance
    # when every class defines the same method
    
    class Class1:
        def m(self):
            print("In Class1") 
        
    class Class2(Class1):
        def m(self):
            print("In Class2")
    
    class Class3(Class1):
        def m(self):
            print("In Class3")     
        
    class Class4(Class2, Class3):
        def m(self):
            print("In Class4")   
    
    obj = Class4()
    obj.m()
    
    Class2.m(obj)
    Class3.m(obj)
    Class1.m(obj)


def main4():
        

    # Python Program to depict multiple inheritance 
    # when we try to call the method m for Class1, 
    # Class2, Class3 from the method m of Class4 
    
    class Class1:
        def m(self):
            print("In Class1")  
        
    class Class2(Class1):
        def m(self):
            print("In Class2")
    
    class Class3(Class1):
        def m(self):
            print("In Class3")     
        
    class Class4(Class2, Class3):
        def m(self):
            print("In Class4")   
            Class2.m(self)
            Class3.m(self)
            Class1.m(self)
    
    obj = Class4()
    obj.m()

    #to note is that, as they are inherited, they are not overriden for the base classes, base class methods can be accessed through inheritance also

def main5():
    

    # Python program to demonstrate
    # super()
    
    class Class1:
        def m(self):
            print("In Class1")
    
    class Class2(Class1):
        def m(self):
            print("In Class2")
            super().m()
    
    class Class3(Class1):
        def m(self):
            print("In Class3")
            super().m()
    
    class Class4(Class2, Class3):
        def m(self):
            print("In Class4")   
            super().m()
        
    obj = Class4()
    obj.m()

def main6():
    # Python Program to depict multiple inheritance
    # when we try to call m of Class1 from both m of
    # Class2 and m of Class3
    
    class Class1:
        def m(self):
            print("In Class1")   
        
    class Class2(Class1):
        def m(self):
            print("In Class2")
            Class1.m(self)
    
    class Class3(Class1):
        def m(self):
            print("In Class3")
            Class1.m(self)   
        
    class Class4(Class2, Class3):
        def m(self):
            print("In Class4")   
            Class2.m(self)
            Class3.m(self)
      
    obj = Class4()
    obj.m()
    #this is different than main5, as there is no super, it's just calling the functions, not an example of mro.
    #The output of the above code has one problem associated with it, the method m of Class1 is called twice. 
    #Python provides a solution to the above problem with the help of the super() function. Let’s see how it works.
    #that was main5

def main6():
    class A:
        def m(self):
            print("A")

    class X(A):

        def m(self):
            super().m()
            print ("X")

    class Y(A):

        def m(self):
            super().m()
            print("Y")

    class Z(X, Y):

        def m(self):
            super().m()

    z = Z()
    z.m()

    #this also follows the order of mro
if __name__ == "__main__":
    # main1()
    # main2()
    # main3()
    # main4()
    main5()
    # main6()    
