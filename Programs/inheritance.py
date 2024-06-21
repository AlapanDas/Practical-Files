class Parent:
     def func1(self):
          print("this is function one")
class Child(Parent):
     def func2(self):
          print(" this is function 2 ")
if __name__ == '__main__':
		ob = Child()
		ob.func1()
		ob.func2()
