#Class and Function

class Cat:
    #public member varaibles of cat age and cat name
    name = ''
    age = 0
    #init method initializing string member variables to empty strings and numeric vales to 0
    def __init__(self):
        self.name = ''
        self.age = 0
    #method populate() used to assign values to the member variables of the class    
    def populate(self, n,a):
        self.name = n
        self.age = a
    #method display() used to display the member variables of the class    
    def display(self):
        print('Cat name:',self.name)
        print('Cat age:',self.age)
#5class instances
c1 = Cat()
c2 = Cat()
c3 = Cat()
c4 = Cat()
c5 = Cat()

#5class instances
n1 = input('Enter cat name: ')
a1 = input('Enter cat age: ')
c1.populate (n1,a1)

n2 = input('Enter cat name: ')
a2 = input('Enter cat age: ')
c2.populate (n2,a2)

n3 = input('Enter cat name: ')
a3 = input('Enter cat age: ')
c3.populate (n3,a3)

n4 = input('Enter cat name: ')
a4 = input('Enter cat age: ')
c4.populate (n4,a4)

n5 = input('Enter cat name: ')
a5 = input('Enter cat age: ')
c5.populate (n5,a5)

c1.display()
c2.display()
c3.display()
c4.display()
c5.display()
